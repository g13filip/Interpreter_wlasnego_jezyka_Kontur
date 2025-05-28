import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import math
from antlr4.tree.Tree import TerminalNode

from .KonturVisitor import KonturVisitor
from .KonturParser import KonturParser

class BreakException(Exception): pass
class ContinueException(Exception): pass

class KonturInterpreter(KonturVisitor):
    def __init__(self, output_func):
        self.variables = {}
        self.output_func = output_func
        self.functions = {}

    def visitProgram(self, ctx: KonturParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitAssignment(self, ctx: KonturParser.AssignmentContext):
        name = ctx.IDENTIFIER().getText()
        line_number = ctx.start.line


        explicit_type = ctx.typeName().getText() if ctx.typeName() else None
        value = self.visit(ctx.expression()) if ctx.expression() else None

        type_mapping = {
            "int": int,
            "float": float,
            "string": str,
            "matrix": np.ndarray
        }

        if not explicit_type and name not in self.variables:
            raise NameError(f"Line {line_number}: Variable '{name}' does not exist. ")

        target_type = type_mapping.get(explicit_type)

        if explicit_type:
            try:
                value = self._cast_value(value, explicit_type)
            except Exception:
                raise TypeError(f"Line {line_number}: Wrong type of value for {explicit_type}.")

        if not explicit_type:
            expected_type = self.variables[name]["type"]
            try:
                value = self._cast_value(value, expected_type)
            except Exception:
                raise TypeError(f"Line {line_number}: Wrong type of value for {name}.")

        var_type = explicit_type if explicit_type else self.variables[name]["type"]
        value = self._cast_value(value, var_type)

        self.variables[name] = {"type": var_type, "value": value}

    def visitReassignment(self, ctx: KonturParser.ReassignmentContext):
        name = ctx.IDENTIFIER().getText()
        op = ctx.getChild(1).getText()
        value = self.visit(ctx.getChild(2))
        line_number = ctx.start.line

        old_value = self.variables[name]["value"]
        old_type = self.variables[name]["type"]

        if name not in self.variables:
            raise NameError(f"Line {line_number}: Variable '{name}' not defined")

        if op == "+=":
            if isinstance(old_value, str) and isinstance(value, str):
                self.variables[name]["value"] = old_value + value
            elif isinstance(old_value, (int, float)) and isinstance(value, (int, float)):
                self.variables[name]["value"] = old_value + value
            else:
                raise TypeError(
                    f"Line {line_number}: Operator '+=' can only be used on two ints/float or two strings. "
                )
        elif op in ("-=", "*=", "/="):
            if not (isinstance(old_value, (int, float)) and not (isinstance(value, (int, float)))):
                raise TypeError(
                    f"Line {line_number}: Operator '{op}' can only be used on numeric types (int/float). "
                )

        if op == "-=":
            self.variables[name]["value"] = old_value - value
        elif op == "*=":
            self.variables[name]["value"] = old_value * value
        elif op == "/=":
            if value == 0:
                raise ValueError(f"Line {line_number}: Division by zero")
            self.variables[name]["value"] = old_value / value

        if isinstance(self.variables[name]["value"], float):
            self.variables[name]["type"] = "float"

    def visitOperation(self, ctx:KonturParser.OperationContext):
        name = ctx.IDENTIFIER().getText()
        op = ctx.getChild(1).getText()
        if self.variables[name]["type"] != "int":
            raise TypeError("Line " + str(ctx.start.line) + ": Increment and Decrement can be only done on type int")

        if op == "++":
            self.variables[name]["value"] += 1
        elif op == "--":
            self.variables[name]["value"] -= 1

    def visitDisplayDecl(self, ctx: KonturParser.DisplayDeclContext):
        value = self.visit(ctx.expression())
        self.output_func.write(value)

    def visitExpression(self, ctx: KonturParser.ExpressionContext):
        if ctx.NUMBER():
            text = ctx.NUMBER().getText()
            return float(text) if '.' in text else int(text)
        elif ctx.STRING():
            return ctx.STRING().getText().strip('"').strip("'")
        elif ctx.IDENTIFIER():
            name = ctx.IDENTIFIER().getText()
            return self.variables.get(name, {}).get("value", f"<undef {name}>")
        elif ctx.numExpression():
            return self.visit(ctx.numExpression())
        elif ctx.boolExpression():
            return self.visit(ctx.boolExpression())
        elif ctx.stringExpression():
            return self.visit(ctx.stringExpression())
        elif ctx.matrixExpression():
            return self.visit(ctx.matrixExpression())
        elif ctx.indexedVar():
            return self.visit(ctx.indexedVar())
        elif ctx.funcCall():
            return self.visit(ctx.funcCall())
        return None

    def visitNumExpression(self, ctx: KonturParser.NumExpressionContext):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            op = ctx.getChild(1).getText()
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
        return self.visit(ctx.getChild(0))

    def visitTerm(self, ctx: KonturParser.TermContext):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            op = ctx.getChild(1).getText()

            if op == '*':
                if isinstance(left, np.ndarray) and isinstance(right, np.ndarray):
                    return np.dot(left, right)
                elif isinstance(left, np.ndarray) or isinstance(right, np.ndarray):
                    return left * right
                else:
                    return left * right

            elif op == '/':
                return left / right
            elif op == '%':
                return left % right

        return self.visit(ctx.getChild(0))

    def visitFactor(self, ctx: KonturParser.FactorContext):
        if ctx.NUMBER():
            text = ctx.NUMBER().getText()
            return float(text) if '.' in text else int(text)
        elif ctx.IDENTIFIER():
            return self.variables.get(ctx.IDENTIFIER().getText(), {}).get("value", 0)
        elif ctx.LEFT_PAREN():
            return self.visit(ctx.numExpression())
        elif ctx.indexedVar():
            return self.visit(ctx.indexedVar())
        return 0

    def visitStringExpression(self, ctx: KonturParser.StringExpressionContext):
        result = self._resolve_string_part(ctx.getChild(0))
        for i in range(2, ctx.getChildCount(), 2):
            result += self._resolve_string_part(ctx.getChild(i))
        return result

    def _resolve_string_part(self, token):
        text = token.getText()
        if text.startswith('"') or text.startswith("'"):
            return text.strip('"').strip("'")
        elif text in self.variables:
            return str(self.variables[text]["value"])
        return str(text)

    def visitMatrixExpression(self, ctx: KonturParser.MatrixExpressionContext):
        matrix = self.visit(ctx.matrixAtom())
        if ctx.TRANSPOSITION():
            matrix = matrix.T
        if ctx.INVERT_MATRIX():
            try:
                matrix = np.linalg.inv(matrix)
            except np.linalg.LinAlgError:
                return f"Matrix not invertible"
        return matrix

    def visitMatrixConstruction(self, ctx: KonturParser.MatrixConstructionContext):
        rows = []
        for row_ctx in ctx.row():
            row = [self.visit(val) for val in row_ctx.value()]
            rows.append(row)
        return np.array(rows)

    def visitMatrixAtom(self, ctx: KonturParser.MatrixAtomContext):
        if ctx.IDENTIFIER():
            name = ctx.IDENTIFIER().getText()
            return self.variables.get(name, {}).get("value", None)
        elif ctx.matrixConstruction():
            return self.visit(ctx.matrixConstruction())
        return None

    def visitIndexedVar(self, ctx: KonturParser.IndexedVarContext):
        name = ctx.IDENTIFIER().getText()
        indexes = [self.visit(e) for e in ctx.indexList().expression()]
        matrix = self.variables.get(name, {}).get("value", None)
        if isinstance(matrix, np.ndarray):
            try:
                return matrix[tuple(indexes)]
            except IndexError:
                return f"Index error in {name}"
        return f"{name} is not a matrix"

    def visitIndexedAssignment(self, ctx):
        name = ctx.indexedVar().IDENTIFIER().getText()
        indexes = [self.visit(e) for e in ctx.indexedVar().indexList().expression()]
        value = self.visit(ctx.expression())
        line_number = ctx.start.line

        if name not in self.variables:
            raise NameError(f"Line {line_number}: Matrix '{name}' is not defined")

        matrix = self.variables[name]["value"]
        if not isinstance(matrix, np.ndarray):
            raise TypeError(f"Line {line_number}: Variable '{name}' is not a matrix")

        try:
            matrix[tuple(indexes)] = value
        except IndexError:
            raise IndexError(f"Line {line_number}: Index out of bounds for matrix '{name}'")
        except Exception as e:
            raise RuntimeError(f"Line {line_number}: Error while assigning to matrix '{name}': {e}")

    def visitValue(self, ctx: KonturParser.ValueContext):
        if ctx.NUMBER():
            text = ctx.NUMBER().getText()
            return float(text) if '.' in text else int(text)
        elif ctx.IDENTIFIER():
            name = ctx.IDENTIFIER().getText()
            return self.variables.get(name, {}).get("value", f"<undef {name}>")
        elif ctx.matrixExpression():
            return self.visit(ctx.matrixExpression())
        return None

    def visitIfStatement(self, ctx: KonturParser.IfStatementContext):
        try:
            n_conditions = len(ctx.boolExpression())
            n_statements = len(ctx.statement())
            n_blocks = len(ctx.block())

            for i in range(n_conditions):
                condition = self.visit(ctx.boolExpression(i))
                if bool(condition):
                    if i < n_statements:
                        return self.visit(ctx.statement(i))
                    else:
                        return self.visit(ctx.block(i - n_statements))

            if ctx.ELSE_INSTR():
                if n_statements > n_conditions:
                    return self.visit(ctx.statement(n_statements - 1))
                elif n_blocks > (n_conditions - n_statements):
                    return self.visit(ctx.block(n_blocks - 1))
        except Exception as e:
            print("BŁĄD w visitIfStatement:", e)

    def visitBoolExpression(self, ctx: KonturParser.BoolExpressionContext):
        try:
            if ctx.getChildCount() == 3:
                left = self.visit(ctx.getChild(0))
                op = ctx.getChild(1).getText()
                right = self.visit(ctx.getChild(2))

                if op == '==': return left == right
                if op == '!=': return left != right
                if op == '<':  return left < right
                if op == '<=': return left <= right
                if op == '>':  return left > right
                if op == '>=': return left >= right
                if op == '&&': return bool(left) and bool(right)
                if op == '||': return bool(left) or bool(right)
            elif ctx.TRUE_VALUE():
                return True
            elif ctx.FALSE_VALUE():
                return False
            elif ctx.NOT():
                return not self.visit(ctx.getChild(1))
            elif ctx.IDENTIFIER():
                return bool(self.variables.get(ctx.IDENTIFIER().getText(), {}).get("value", False))
            else:
                return bool(self.visitChildren(ctx))
        except Exception as e:
            print("Błąd w boolExpression:", ctx.getText(), "→", e)
            return False

    def _infer_type(self, val):
        if isinstance(val, int): return "int"
        if isinstance(val, float): return "float"
        if isinstance(val, str): return "string"
        if isinstance(val, np.ndarray): return "matrix"
        return "unknown"

    def _cast_value(self, val, typ):
        if isinstance(val, np.generic):
            val = val.item()
        if typ == "int": return int(float(val))
        if typ == "float": return float(val)
        if typ == "string": return str(val)
        if typ == "matrix": return np.array(val) if not isinstance(val, np.ndarray) else val
        return val

    def visitWhileLoop(self, ctx):
        while self.visit(ctx.boolExpression()):
            try:
                if ctx.statement():
                    self.visit(ctx.loopStatement())
                else:
                    for stmt in ctx.loopStatements():
                        try:
                            self.visit(stmt)
                        except ContinueException:
                            raise
                        except BreakException:
                            raise
            except ContinueException:
                continue
            except BreakException:
                break

    def visitForLoop(self, ctx: KonturParser.ForLoopContext):

        if ctx.assignment():
            self.visit(ctx.assignment())

        while self.visit(ctx.boolExpression()):
            if ctx.statement():
                self.visit(ctx.statement())
            else:
                if ctx.loopStatements():
                    for stmt in ctx.loopStatements():
                        try:
                            self.visit(stmt)
                        except ContinueException:
                            raise  # przerywa natychmiast – wraca do pętli
                        except BreakException:
                            raise
            if ctx.reassignment():
                self.visit(ctx.reassignment())
            elif ctx.operation():
                self.visit(ctx.operation())

        # if ctx.statement():
        #     while self.visit(ctx.boolExpression()):
        #         self.visit(ctx.statement())
        #         if ctx.assignment():
        #             self.visit(ctx.assignment())
        #         elif ctx.reassignment():
        #             self.visit(ctx.reassignment())
        #         elif ctx.operation():
        #             self.visit(ctx.operation())
        # else:
        #     body = ctx.getChild(8)  # { ... }
        #     while self.visit(ctx.boolExpression()):
        #         for child in body.children[1:-1]:
        #             self.visit(child)
        #         if ctx.assignment():
        #             self.visit(ctx.assignment())
        #         elif ctx.reassignment():
        #             self.visit(ctx.reassignment())
        #         elif ctx.operation():
        #             self.visit(ctx.operation())

    def visitBreakStatement(self, ctx):
        raise BreakException()

    def visitContinueStatement(self, ctx):
        raise ContinueException()

    def visitPlotDecl(self, ctx: KonturParser.PlotDeclContext):
        try:
            # Argument 1: macierz danych
            if ctx.IDENTIFIER(0):
                var_name = ctx.IDENTIFIER(0).getText()
                matrix_data = self.variables.get(var_name, {})
                matrix = matrix_data.get("value")
                if matrix is None:
                    self.output_func.write(f"Error: Variable '{var_name}' not found")
                    return
            else:
                matrix = self.visit(ctx.matrixExpression())

            # Argument 2: tytuł wykresu
            title_node = ctx.getChild(4)  # 5. dziecko: IDENTIFIER lub STRING
            title = "Plot"
            if isinstance(title_node, TerminalNode) and title_node.getSymbol().type == KonturParser.STRING:
                title = title_node.getText().strip('"').strip("'")
            else:
                title_var = title_node.getText()
                title_data = self.variables.get(title_var, {})
                title = str(title_data.get("value", title_var))

            if not isinstance(matrix, np.ndarray):
                matrix = np.array(matrix)
            if matrix.ndim == 2 and matrix.shape[0] == 1:
                matrix = matrix.flatten()

            # Generowanie wykresu
            if matrix.ndim == 1:
                x_values = np.arange(1, len(matrix) + 1)
                fig = px.line(x=x_values, y=matrix, title=title, labels={'x': 'Index', 'y': 'Value'})
            elif matrix.shape[0] == 2:
                fig = px.line(x=matrix[0], y=matrix[1], title=title, labels={'x': 'X', 'y': 'Y'})
            elif matrix.shape[0] == 3:
                fig = go.Figure(data=[go.Scatter3d(
                    x=matrix[0], y=matrix[1], z=matrix[2],
                    mode='lines+markers', marker=dict(size=4), line=dict(width=2)
                )])
                fig.update_layout(title=title, scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))
            elif matrix.shape[1] == 2:
                fig = px.scatter(x=matrix[:, 0], y=matrix[:, 1], title=title)
            elif matrix.shape[1] == 3:
                fig = px.scatter_3d(x=matrix[:, 0], y=matrix[:, 1], z=matrix[:, 2], title=title)
            else:
                self.output_func.write("Error: Unsupported matrix format. Expected: 1D, 2xN, 3xN, Nx2 or Nx3 matrix")
                return

            # Renderowanie
            if hasattr(self.output_func, 'plotly_chart'):
                self.output_func.plotly_chart(fig)
            else:
                self.output_func.write(fig.to_html(include_plotlyjs='cdn'))

        except Exception as e:
            self.output_func.write(f"Plot error: {str(e)}")

    def visitFuncCall(self, ctx:KonturParser.FuncCallContext):
        if ctx.builtInFunctions():
            return self.visit(ctx.builtInFunctions())



    def visitBuiltInFunctions(self, ctx: KonturParser.BuiltInFunctionsContext):
        try:
            if ctx.POWER_FUNC():
                # Obsługa funkcji potęgującej pow(x,y)
                base = self.visit(ctx.numExpression(0))
                exponent = self.visit(ctx.numExpression(1))

                if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
                    raise TypeError("Function 'pow' expects numeric arguments")

                result = base ** exponent
                # Zwróć int jeśli wynik jest całkowity
                return int(result) if isinstance(result, float) and result.is_integer() else result




            elif ctx.SIN_FUNC() or ctx.COS_FUNC() or ctx.TAN_FUNC() or ctx.CTAN_FUNC():
                # Obsługa funkcji trygonometrycznych
                angle = self.visit(ctx.numExpression(0))

                if not isinstance(angle, (int, float)):
                    raise TypeError("Trigonometric functions expect numeric argument")

                angle_rad = math.radians(angle)  # Konwersja stopni na radiany
                func_type = ctx.getChild(0).getText().lower()

                if ctx.SIN_FUNC():
                    result = math.sin(angle_rad)
                elif ctx.COS_FUNC():
                    result = math.cos(angle_rad)
                elif ctx.TAN_FUNC():
                    result = math.tan(angle_rad)
                elif ctx.CTAN_FUNC():
                    tan_val = math.tan(angle_rad)
                    if abs(tan_val) < 1e-10:
                        raise ValueError("Cotangent is undefined for this angle")
                    result = 1 / tan_val

                # Zaokrąglenie wyników bliskich 0, 1 lub -1
                if abs(result) < 1e-10:
                    return float(0)
                elif abs(result - 1) < 1e-10:
                    return float(1)
                elif abs(result + 1) < 1e-10:
                    return float(-1)
                return float(result)



            elif ctx.MATRIX_FROM_LOOP_FUNC():

                exprs = ctx.expression()

                ids = ctx.IDENTIFIER()

                nums = ctx.numExpression()

                expr = exprs[-1]  # Ostatnie to ciało pętli (np. i * j)

                if len(ids) == 1:

                    var1 = ids[0].getText()

                    start1 = self.visit(nums[0])

                    end1 = self.visit(nums[1])

                    result = []

                    for i in range(int(start1), int(end1)):
                        self.variables[var1] = {"type": "int", "value": i}

                        result.append(self.visit(expr))

                    return np.array([result])


                elif len(ids) == 2:

                    var1 = ids[0].getText()

                    start1 = self.visit(nums[0])

                    end1 = self.visit(nums[1])

                    var2 = ids[1].getText()

                    start2 = self.visit(nums[2])

                    end2 = self.visit(nums[3])

                    result = []

                    for i in range(int(start1), int(end1)):

                        self.variables[var1] = {"type": "int", "value": i}

                        row = []

                        for j in range(int(start2), int(end2)):
                            self.variables[var2] = {"type": "int", "value": j}

                            row.append(self.visit(expr))

                        result.append(row)

                    return np.array(result)


            elif ctx.VSTACK_FUNC():
                a = self.visit(ctx.expression(0))
                b = self.visit(ctx.expression(1))
                if not isinstance(a, np.ndarray):
                    a = np.array(a, dtype=float)
                if not isinstance(b, np.ndarray):
                    b = np.array(b, dtype=float)
                if a.ndim == 1:
                    a = np.expand_dims(a, axis=0)
                if b.ndim == 1:
                    b = np.expand_dims(b, axis=0)
                try:
                    result = np.vstack([a, b])
                    return result
                except ValueError as e:
                    raise ValueError(f"Matrix dimension mismatch in vstack: {e}")

        except ValueError as ve:
            self.output_func.write(f"Math error: {str(ve)}")
            raise
        except TypeError as te:
            self.output_func.write(f"Type error: {str(te)}")
            raise
        except Exception as e:
            self.output_func.write(f"Error in built-in function: {str(e)}")
            raise

    def visitFuncDecl(self, ctx):
        name = ctx.IDENTIFIER().getText()
        return_type = ctx.typeName().getText() if ctx.typeName() else "void"
        parameters = []

        if ctx.parameters():
            for i in range(len(ctx.parameters().IDENTIFIER())):
                param_type = ctx.parameters().typeName(i).getText()
                param_name = ctx.parameters().IDENTIFIER(i).getText()
                parameters.append((param_type, param_name))

        self.functions[name] = {
            "return_type": return_type,
            "parameters": parameters,
            "block": ctx.block()
        }