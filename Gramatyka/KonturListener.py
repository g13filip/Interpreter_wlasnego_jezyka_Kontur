# Generated from Kontur.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .KonturParser import KonturParser
else:
    from KonturParser import KonturParser

# This class defines a complete listener for a parse tree produced by KonturParser.
class KonturListener(ParseTreeListener):

    # Enter a parse tree produced by KonturParser#program.
    def enterProgram(self, ctx:KonturParser.ProgramContext):
        pass

    # Exit a parse tree produced by KonturParser#program.
    def exitProgram(self, ctx:KonturParser.ProgramContext):
        pass


    # Enter a parse tree produced by KonturParser#statement.
    def enterStatement(self, ctx:KonturParser.StatementContext):
        pass

    # Exit a parse tree produced by KonturParser#statement.
    def exitStatement(self, ctx:KonturParser.StatementContext):
        pass


    # Enter a parse tree produced by KonturParser#loopStatements.
    def enterLoopStatements(self, ctx:KonturParser.LoopStatementsContext):
        pass

    # Exit a parse tree produced by KonturParser#loopStatements.
    def exitLoopStatements(self, ctx:KonturParser.LoopStatementsContext):
        pass


    # Enter a parse tree produced by KonturParser#breakStatement.
    def enterBreakStatement(self, ctx:KonturParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by KonturParser#breakStatement.
    def exitBreakStatement(self, ctx:KonturParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by KonturParser#continueStatement.
    def enterContinueStatement(self, ctx:KonturParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by KonturParser#continueStatement.
    def exitContinueStatement(self, ctx:KonturParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by KonturParser#block.
    def enterBlock(self, ctx:KonturParser.BlockContext):
        pass

    # Exit a parse tree produced by KonturParser#block.
    def exitBlock(self, ctx:KonturParser.BlockContext):
        pass


    # Enter a parse tree produced by KonturParser#assignment.
    def enterAssignment(self, ctx:KonturParser.AssignmentContext):
        pass

    # Exit a parse tree produced by KonturParser#assignment.
    def exitAssignment(self, ctx:KonturParser.AssignmentContext):
        pass


    # Enter a parse tree produced by KonturParser#expression.
    def enterExpression(self, ctx:KonturParser.ExpressionContext):
        pass

    # Exit a parse tree produced by KonturParser#expression.
    def exitExpression(self, ctx:KonturParser.ExpressionContext):
        pass


    # Enter a parse tree produced by KonturParser#indexedVar.
    def enterIndexedVar(self, ctx:KonturParser.IndexedVarContext):
        pass

    # Exit a parse tree produced by KonturParser#indexedVar.
    def exitIndexedVar(self, ctx:KonturParser.IndexedVarContext):
        pass


    # Enter a parse tree produced by KonturParser#indexedAssignment.
    def enterIndexedAssignment(self, ctx:KonturParser.IndexedAssignmentContext):
        pass

    # Exit a parse tree produced by KonturParser#indexedAssignment.
    def exitIndexedAssignment(self, ctx:KonturParser.IndexedAssignmentContext):
        pass


    # Enter a parse tree produced by KonturParser#indexList.
    def enterIndexList(self, ctx:KonturParser.IndexListContext):
        pass

    # Exit a parse tree produced by KonturParser#indexList.
    def exitIndexList(self, ctx:KonturParser.IndexListContext):
        pass


    # Enter a parse tree produced by KonturParser#matrixExpression.
    def enterMatrixExpression(self, ctx:KonturParser.MatrixExpressionContext):
        pass

    # Exit a parse tree produced by KonturParser#matrixExpression.
    def exitMatrixExpression(self, ctx:KonturParser.MatrixExpressionContext):
        pass


    # Enter a parse tree produced by KonturParser#matrixAtom.
    def enterMatrixAtom(self, ctx:KonturParser.MatrixAtomContext):
        pass

    # Exit a parse tree produced by KonturParser#matrixAtom.
    def exitMatrixAtom(self, ctx:KonturParser.MatrixAtomContext):
        pass


    # Enter a parse tree produced by KonturParser#matrixConstruction.
    def enterMatrixConstruction(self, ctx:KonturParser.MatrixConstructionContext):
        pass

    # Exit a parse tree produced by KonturParser#matrixConstruction.
    def exitMatrixConstruction(self, ctx:KonturParser.MatrixConstructionContext):
        pass


    # Enter a parse tree produced by KonturParser#row.
    def enterRow(self, ctx:KonturParser.RowContext):
        pass

    # Exit a parse tree produced by KonturParser#row.
    def exitRow(self, ctx:KonturParser.RowContext):
        pass


    # Enter a parse tree produced by KonturParser#value.
    def enterValue(self, ctx:KonturParser.ValueContext):
        pass

    # Exit a parse tree produced by KonturParser#value.
    def exitValue(self, ctx:KonturParser.ValueContext):
        pass


    # Enter a parse tree produced by KonturParser#stringExpression.
    def enterStringExpression(self, ctx:KonturParser.StringExpressionContext):
        pass

    # Exit a parse tree produced by KonturParser#stringExpression.
    def exitStringExpression(self, ctx:KonturParser.StringExpressionContext):
        pass


    # Enter a parse tree produced by KonturParser#funcCall.
    def enterFuncCall(self, ctx:KonturParser.FuncCallContext):
        pass

    # Exit a parse tree produced by KonturParser#funcCall.
    def exitFuncCall(self, ctx:KonturParser.FuncCallContext):
        pass


    # Enter a parse tree produced by KonturParser#builtInFunctions.
    def enterBuiltInFunctions(self, ctx:KonturParser.BuiltInFunctionsContext):
        pass

    # Exit a parse tree produced by KonturParser#builtInFunctions.
    def exitBuiltInFunctions(self, ctx:KonturParser.BuiltInFunctionsContext):
        pass


    # Enter a parse tree produced by KonturParser#boolExpression.
    def enterBoolExpression(self, ctx:KonturParser.BoolExpressionContext):
        pass

    # Exit a parse tree produced by KonturParser#boolExpression.
    def exitBoolExpression(self, ctx:KonturParser.BoolExpressionContext):
        pass


    # Enter a parse tree produced by KonturParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:KonturParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by KonturParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:KonturParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by KonturParser#funcDecl.
    def enterFuncDecl(self, ctx:KonturParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by KonturParser#funcDecl.
    def exitFuncDecl(self, ctx:KonturParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by KonturParser#returnType.
    def enterReturnType(self, ctx:KonturParser.ReturnTypeContext):
        pass

    # Exit a parse tree produced by KonturParser#returnType.
    def exitReturnType(self, ctx:KonturParser.ReturnTypeContext):
        pass


    # Enter a parse tree produced by KonturParser#parameters.
    def enterParameters(self, ctx:KonturParser.ParametersContext):
        pass

    # Exit a parse tree produced by KonturParser#parameters.
    def exitParameters(self, ctx:KonturParser.ParametersContext):
        pass


    # Enter a parse tree produced by KonturParser#parameter.
    def enterParameter(self, ctx:KonturParser.ParameterContext):
        pass

    # Exit a parse tree produced by KonturParser#parameter.
    def exitParameter(self, ctx:KonturParser.ParameterContext):
        pass


    # Enter a parse tree produced by KonturParser#returnDecl.
    def enterReturnDecl(self, ctx:KonturParser.ReturnDeclContext):
        pass

    # Exit a parse tree produced by KonturParser#returnDecl.
    def exitReturnDecl(self, ctx:KonturParser.ReturnDeclContext):
        pass


    # Enter a parse tree produced by KonturParser#numExpression.
    def enterNumExpression(self, ctx:KonturParser.NumExpressionContext):
        pass

    # Exit a parse tree produced by KonturParser#numExpression.
    def exitNumExpression(self, ctx:KonturParser.NumExpressionContext):
        pass


    # Enter a parse tree produced by KonturParser#term.
    def enterTerm(self, ctx:KonturParser.TermContext):
        pass

    # Exit a parse tree produced by KonturParser#term.
    def exitTerm(self, ctx:KonturParser.TermContext):
        pass


    # Enter a parse tree produced by KonturParser#factor.
    def enterFactor(self, ctx:KonturParser.FactorContext):
        pass

    # Exit a parse tree produced by KonturParser#factor.
    def exitFactor(self, ctx:KonturParser.FactorContext):
        pass


    # Enter a parse tree produced by KonturParser#typeName.
    def enterTypeName(self, ctx:KonturParser.TypeNameContext):
        pass

    # Exit a parse tree produced by KonturParser#typeName.
    def exitTypeName(self, ctx:KonturParser.TypeNameContext):
        pass


    # Enter a parse tree produced by KonturParser#operation.
    def enterOperation(self, ctx:KonturParser.OperationContext):
        pass

    # Exit a parse tree produced by KonturParser#operation.
    def exitOperation(self, ctx:KonturParser.OperationContext):
        pass


    # Enter a parse tree produced by KonturParser#reassignment.
    def enterReassignment(self, ctx:KonturParser.ReassignmentContext):
        pass

    # Exit a parse tree produced by KonturParser#reassignment.
    def exitReassignment(self, ctx:KonturParser.ReassignmentContext):
        pass


    # Enter a parse tree produced by KonturParser#ifStatement.
    def enterIfStatement(self, ctx:KonturParser.IfStatementContext):
        pass

    # Exit a parse tree produced by KonturParser#ifStatement.
    def exitIfStatement(self, ctx:KonturParser.IfStatementContext):
        pass


    # Enter a parse tree produced by KonturParser#loopIfStatement.
    def enterLoopIfStatement(self, ctx:KonturParser.LoopIfStatementContext):
        pass

    # Exit a parse tree produced by KonturParser#loopIfStatement.
    def exitLoopIfStatement(self, ctx:KonturParser.LoopIfStatementContext):
        pass


    # Enter a parse tree produced by KonturParser#loopStatement.
    def enterLoopStatement(self, ctx:KonturParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by KonturParser#loopStatement.
    def exitLoopStatement(self, ctx:KonturParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by KonturParser#forLoop.
    def enterForLoop(self, ctx:KonturParser.ForLoopContext):
        pass

    # Exit a parse tree produced by KonturParser#forLoop.
    def exitForLoop(self, ctx:KonturParser.ForLoopContext):
        pass


    # Enter a parse tree produced by KonturParser#whileLoop.
    def enterWhileLoop(self, ctx:KonturParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by KonturParser#whileLoop.
    def exitWhileLoop(self, ctx:KonturParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by KonturParser#displayDecl.
    def enterDisplayDecl(self, ctx:KonturParser.DisplayDeclContext):
        pass

    # Exit a parse tree produced by KonturParser#displayDecl.
    def exitDisplayDecl(self, ctx:KonturParser.DisplayDeclContext):
        pass


    # Enter a parse tree produced by KonturParser#plotDecl.
    def enterPlotDecl(self, ctx:KonturParser.PlotDeclContext):
        pass

    # Exit a parse tree produced by KonturParser#plotDecl.
    def exitPlotDecl(self, ctx:KonturParser.PlotDeclContext):
        pass



del KonturParser