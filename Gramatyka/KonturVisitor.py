# Generated from Kontur.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .KonturParser import KonturParser
else:
    from KonturParser import KonturParser

# This class defines a complete generic visitor for a parse tree produced by KonturParser.

class KonturVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by KonturParser#program.
    def visitProgram(self, ctx:KonturParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#statement.
    def visitStatement(self, ctx:KonturParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#loopStatements.
    def visitLoopStatements(self, ctx:KonturParser.LoopStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#block.
    def visitBlock(self, ctx:KonturParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#assignment.
    def visitAssignment(self, ctx:KonturParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#expression.
    def visitExpression(self, ctx:KonturParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#indexedVar.
    def visitIndexedVar(self, ctx:KonturParser.IndexedVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#indexList.
    def visitIndexList(self, ctx:KonturParser.IndexListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#matrixExpression.
    def visitMatrixExpression(self, ctx:KonturParser.MatrixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#matrixAtom.
    def visitMatrixAtom(self, ctx:KonturParser.MatrixAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#matrixConstruction.
    def visitMatrixConstruction(self, ctx:KonturParser.MatrixConstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#row.
    def visitRow(self, ctx:KonturParser.RowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#value.
    def visitValue(self, ctx:KonturParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#stringExpression.
    def visitStringExpression(self, ctx:KonturParser.StringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#funcCall.
    def visitFuncCall(self, ctx:KonturParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#builtInFunctions.
    def visitBuiltInFunctions(self, ctx:KonturParser.BuiltInFunctionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#boolExpression.
    def visitBoolExpression(self, ctx:KonturParser.BoolExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:KonturParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#funcDecl.
    def visitFuncDecl(self, ctx:KonturParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#parameters.
    def visitParameters(self, ctx:KonturParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#returnDecl.
    def visitReturnDecl(self, ctx:KonturParser.ReturnDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#numExpression.
    def visitNumExpression(self, ctx:KonturParser.NumExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#term.
    def visitTerm(self, ctx:KonturParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#factor.
    def visitFactor(self, ctx:KonturParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#typeName.
    def visitTypeName(self, ctx:KonturParser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#operation.
    def visitOperation(self, ctx:KonturParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#reassignment.
    def visitReassignment(self, ctx:KonturParser.ReassignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#ifStatement.
    def visitIfStatement(self, ctx:KonturParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#loopIfStatement.
    def visitLoopIfStatement(self, ctx:KonturParser.LoopIfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#loopStatement.
    def visitLoopStatement(self, ctx:KonturParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#forLoop.
    def visitForLoop(self, ctx:KonturParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#whileLoop.
    def visitWhileLoop(self, ctx:KonturParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#displayDecl.
    def visitDisplayDecl(self, ctx:KonturParser.DisplayDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KonturParser#plotDecl.
    def visitPlotDecl(self, ctx:KonturParser.PlotDeclContext):
        return self.visitChildren(ctx)



del KonturParser