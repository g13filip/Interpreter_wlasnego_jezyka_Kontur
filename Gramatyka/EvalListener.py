import numpy as np

from Gramatyka.KonturListener import KonturListener
from Gramatyka.KonturParser import KonturParser


class EvalListener(KonturListener):
    def __init__(self):
        self.memory = {}
        self.stack = []
        self.output = []

    # -------------Assignment--------------
    def exitAssignment(self, ctx: KonturParser.AssignmentContext):
        var_name = ctx.IDENTIFIER().getText()
        if ctx.expression():
            value = self.stack.pop()
            self.memory[var_name] = value
        else:
            self.memory[var_name] = None

    # -------------Display------------------
    def exitDisplayDecl(self, ctx: KonturParser.DisplayDeclContext):
        value = self.stack.pop()
        self.output.append(str(value))

    # -------------Expression---------------
    def exitExpression(self, ctx: KonturParser.ExpressionContext):
        if ctx.IDENTIFIER():
            name = ctx.IDENTIFIER().getText()
            if name not in self.memory:
                raise Exception(f"Zmienna {name} nie istnieje")
            self.stack.append(self.memory[name])
        elif ctx.NUMBER():
            text = ctx.NUMBER().getText()
            self.stack.append(float(text) if '.' in text else int(text))
        elif ctx.STRING():
            self.stack.append(ctx.STRING().getText()[1:-1])
        elif ctx.boolExpression() or ctx.numExpression() or ctx.matrixExpression():
            pass

    # -------------NumExpression--------------
    def exitNumExpression(self, ctx: KonturParser.NumExpressionContext):
        if ctx.getChildCount() == 3:
            right = self.stack.pop()
            left = self.stack.pop()
            op = ctx.getChild(1).getText()
            result = {
                '+': left + right,
                '-': left + right,
            }[op]
            self.stack.append(result)
        elif ctx.getChildCount() == 1:
            pass

    def exitTerm(self, ctx: KonturParser.TermContext):
        if ctx.getChildCount() == 3:
            right = self.stack.pop()
            left = self.stack.pop()
            op = ctx.getChild(1).getText()
            result = {
                '*': left * right,
                '/': left / right,
            }[op]
            self.stack.append(result)

    def exitFactor(self, ctx: KonturParser.FactorContext):
        if ctx.NUMBER():
            text = ctx.NUMBER().getText()
            self.stack.append(float(text) if '.' in text else int(text))
        if ctx.IDENTIFIER():
            name = ctx.IDENTIFIER().getText()
            if name not in self.memory:
                raise Exception(f"Zmienna {name} nie istnieje")
            self.stack.append(self.memory[name])
        elif ctx.LEFT_PAREN():
            pass

    # -------------Bool Expression--------------
    def exitBoolExpression(self, ctx: KonturParser.BoolExpressionContext):
        if ctx.TRUE_VALUE():
            self.stack.append(True)
        elif ctx.FALSE_VALUE():
            self.stack.append(False)

        elif ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            value = self.memory.get(var_name)
            if not isinstance(value, bool):
                raise RuntimeError(f"Zmienna '{var_name}' nie jest typu bool")
            self.stack.append(value)
        elif ctx.operator:
            right = self.stack.pop()
            left = self.stack.pop()
            op = ctx.operator.text
            if op == '&&':
                self.stack.append(bool(left) and bool(right))
            elif op == '||':
                self.stack.append(bool(left) or bool(right))
            else:
                raise RuntimeError(f"Unknown logical operator: {op}")

        elif ctx.comparisonOperator():
            right = self.stack.pop()
            left = self.stack.pop()
            op = ctx.comparisonOperator().getText()
            if op == '==':
                self.stack.append(left == right)
            elif op == '!=':
                self.stack.append(left != right)
            elif op == '<':
                self.stack.append(left < right)
            elif op == '<=':
                self.stack.append(left <= right)
            elif op == '>':
                self.stack.append(left > right)
            elif op == '>=':
                self.stack.append(left >= right)
            else:
                raise RuntimeError(f"Unknown comparison operator: {op}")
        elif ctx.NOT():
            value = self.stack.pop()
            self.stack.append(not bool(value))
        elif ctx.LEFT_PAREN() and ctx.RIGHT_PAREN():
            value = self.stack.pop()
            self.stack.append(value)

    # -------------If Statement--------------
    def exitIfStatement(self, ctx: KonturParser.IfStatementContext):
        condition = self.stack.pop() if self.stack else False
        if condition:
            self.skip_blocks = [False] * len(ctx.block())
            self.skip_blocks[0] = False
        else:
            matched = False
            elifs = ctx.ELIF_INSTR()
            for i, _ in enumerate(elifs):
                cond = self.stack.pop() if self.stack else False
                if cond and not matched:
                    matched = True
                    self.skip_blocks = [True] * len(ctx.block())
                    self.skip_blocks[i + 1] = False
                    break
            if not matched and ctx.ELSE_INSTR():
                self.skip_blocks = [True] * len(ctx.block())
                self.skip_blocks[-1] = False
            elif not matched:
                self.skip_blocks = [True] * len(ctx.block())

    # -------------Matrix Expression--------------
    def exitMatrixExpression(self, ctx: KonturParser.MatrixExpressionContext):
        matrix = self.stack.pop()
        if ctx.INVERT_MATRIX():
            try:
                matrix = np.linalg.inv(matrix)
            except np.linalg.LinAlgError:
                raise RuntimeError("Macierz nieodwracalna")

        if ctx.TRANSPOSITION():
            matrix = matrix.T

        self.stack.append(matrix)


    def exitMatrixAtom(self, ctx: KonturParser.MatrixAtomContext):
        if ctx.IDENTIFIER():
            name = ctx.IDENTIFIER().getText()
            if name not in self.memory:
                raise RuntimeError(f"Zmienna '{name}' nie istnieje")
            self.stack.append(self.memory[name])
        elif ctx.matrixConstruction():
            pass


    def exitMatrixConstruction(self, ctx: KonturParser.MatrixConstructionContext):
        raw_rows = []

        for row_ctx in ctx.row():
            row = []
            for val_ctx in row_ctx.value():
                if val_ctx.NUMBER():
                    row.append(float(val_ctx.NUMBER().getText()))
                elif val_ctx.IDENTIFIER():
                    name = val_ctx.IDENTIFIER().getText()
                    if name not in self.memory:
                        raise Exception(f"Zmienna {name} nie istnieje")
                    row.append(self.memory[name])
                else:
                    raise NotImplementedError("Nieobsługiwane wartości w macierzy")
            raw_rows.append(row)

        max_len = max(len(row) for row in raw_rows)
        padded_rows = [row + [0] * (max_len - len(row)) for row in raw_rows]
        matrix = np.array(padded_rows, dtype=float)
        self.stack.append(matrix)

    #--------------Blocks---------------------
