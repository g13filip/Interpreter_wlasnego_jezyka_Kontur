# Generated from Kontur.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,51,307,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,5,0,60,8,0,10,0,12,0,63,9,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,76,8,1,1,2,1,2,5,2,80,8,2,10,
        2,12,2,83,9,2,1,2,1,2,1,3,3,3,88,8,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,106,8,4,1,5,1,5,1,5,1,5,
        1,5,1,6,1,6,1,6,5,6,116,8,6,10,6,12,6,119,9,6,1,7,3,7,122,8,7,1,
        7,1,7,3,7,126,8,7,1,8,1,8,3,8,130,8,8,1,9,1,9,1,9,1,9,5,9,136,8,
        9,10,9,12,9,139,9,9,1,9,1,9,1,10,1,10,1,10,5,10,146,8,10,10,10,12,
        10,149,9,10,1,11,1,11,1,11,3,11,154,8,11,1,12,1,12,1,12,5,12,159,
        8,12,10,12,12,12,162,9,12,1,13,1,13,1,13,1,13,1,13,5,13,169,8,13,
        10,13,12,13,172,9,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,192,8,14,1,14,
        1,14,1,14,5,14,197,8,14,10,14,12,14,200,9,14,1,15,1,15,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,5,17,
        218,8,17,10,17,12,17,221,9,17,1,18,1,18,3,18,225,8,18,1,18,1,18,
        1,19,1,19,1,19,1,19,1,19,1,19,5,19,235,8,19,10,19,12,19,238,9,19,
        1,20,1,20,1,20,1,20,1,20,1,20,5,20,246,8,20,10,20,12,20,249,9,20,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,259,8,21,1,22,1,22,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,270,8,23,1,24,1,24,3,24,
        274,8,24,1,25,1,25,1,25,1,25,3,25,280,8,25,1,25,1,25,1,25,1,25,1,
        25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,
        27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,0,3,28,38,40,29,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,0,7,1,0,50,51,1,0,18,19,1,0,24,25,1,0,18,23,1,0,9,10,
        1,0,11,13,1,0,1,5,325,0,61,1,0,0,0,2,75,1,0,0,0,4,77,1,0,0,0,6,87,
        1,0,0,0,8,105,1,0,0,0,10,107,1,0,0,0,12,112,1,0,0,0,14,121,1,0,0,
        0,16,129,1,0,0,0,18,131,1,0,0,0,20,142,1,0,0,0,22,153,1,0,0,0,24,
        155,1,0,0,0,26,163,1,0,0,0,28,191,1,0,0,0,30,201,1,0,0,0,32,203,
        1,0,0,0,34,211,1,0,0,0,36,222,1,0,0,0,38,228,1,0,0,0,40,239,1,0,
        0,0,42,258,1,0,0,0,44,260,1,0,0,0,46,262,1,0,0,0,48,273,1,0,0,0,
        50,275,1,0,0,0,52,288,1,0,0,0,54,294,1,0,0,0,56,300,1,0,0,0,58,60,
        3,2,1,0,59,58,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,
        62,64,1,0,0,0,63,61,1,0,0,0,64,65,5,0,0,1,65,1,1,0,0,0,66,76,3,4,
        2,0,67,76,3,6,3,0,68,76,3,8,4,0,69,76,3,32,16,0,70,76,3,56,28,0,
        71,76,3,36,18,0,72,76,3,48,24,0,73,76,3,54,27,0,74,76,3,46,23,0,
        75,66,1,0,0,0,75,67,1,0,0,0,75,68,1,0,0,0,75,69,1,0,0,0,75,70,1,
        0,0,0,75,71,1,0,0,0,75,72,1,0,0,0,75,73,1,0,0,0,75,74,1,0,0,0,76,
        3,1,0,0,0,77,81,5,31,0,0,78,80,3,2,1,0,79,78,1,0,0,0,80,83,1,0,0,
        0,81,79,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,
        5,32,0,0,85,5,1,0,0,0,86,88,3,44,22,0,87,86,1,0,0,0,87,88,1,0,0,
        0,88,89,1,0,0,0,89,90,5,51,0,0,90,91,5,8,0,0,91,92,3,8,4,0,92,93,
        5,33,0,0,93,7,1,0,0,0,94,106,3,38,19,0,95,106,3,14,7,0,96,106,3,
        24,12,0,97,106,3,28,14,0,98,106,3,26,13,0,99,106,3,10,5,0,100,106,
        5,51,0,0,101,106,5,49,0,0,102,106,5,50,0,0,103,106,5,6,0,0,104,106,
        5,7,0,0,105,94,1,0,0,0,105,95,1,0,0,0,105,96,1,0,0,0,105,97,1,0,
        0,0,105,98,1,0,0,0,105,99,1,0,0,0,105,100,1,0,0,0,105,101,1,0,0,
        0,105,102,1,0,0,0,105,103,1,0,0,0,105,104,1,0,0,0,106,9,1,0,0,0,
        107,108,5,51,0,0,108,109,5,29,0,0,109,110,3,12,6,0,110,111,5,30,
        0,0,111,11,1,0,0,0,112,117,3,8,4,0,113,114,5,34,0,0,114,116,3,8,
        4,0,115,113,1,0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,
        0,0,118,13,1,0,0,0,119,117,1,0,0,0,120,122,5,15,0,0,121,120,1,0,
        0,0,121,122,1,0,0,0,122,123,1,0,0,0,123,125,3,16,8,0,124,126,5,14,
        0,0,125,124,1,0,0,0,125,126,1,0,0,0,126,15,1,0,0,0,127,130,5,51,
        0,0,128,130,3,18,9,0,129,127,1,0,0,0,129,128,1,0,0,0,130,17,1,0,
        0,0,131,132,5,29,0,0,132,137,3,20,10,0,133,134,5,33,0,0,134,136,
        3,20,10,0,135,133,1,0,0,0,136,139,1,0,0,0,137,135,1,0,0,0,137,138,
        1,0,0,0,138,140,1,0,0,0,139,137,1,0,0,0,140,141,5,30,0,0,141,19,
        1,0,0,0,142,147,3,22,11,0,143,144,5,34,0,0,144,146,3,22,11,0,145,
        143,1,0,0,0,146,149,1,0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,
        21,1,0,0,0,149,147,1,0,0,0,150,154,5,49,0,0,151,154,5,51,0,0,152,
        154,3,14,7,0,153,150,1,0,0,0,153,151,1,0,0,0,153,152,1,0,0,0,154,
        23,1,0,0,0,155,160,7,0,0,0,156,157,5,9,0,0,157,159,7,0,0,0,158,156,
        1,0,0,0,159,162,1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,25,1,
        0,0,0,162,160,1,0,0,0,163,164,5,51,0,0,164,165,5,27,0,0,165,170,
        5,51,0,0,166,167,5,34,0,0,167,169,5,51,0,0,168,166,1,0,0,0,169,172,
        1,0,0,0,170,168,1,0,0,0,170,171,1,0,0,0,171,173,1,0,0,0,172,170,
        1,0,0,0,173,174,5,28,0,0,174,175,5,33,0,0,175,27,1,0,0,0,176,177,
        6,14,-1,0,177,178,3,38,19,0,178,179,3,30,15,0,179,180,3,38,19,0,
        180,192,1,0,0,0,181,182,3,24,12,0,182,183,7,1,0,0,183,184,3,24,12,
        0,184,192,1,0,0,0,185,186,3,14,7,0,186,187,7,1,0,0,187,188,3,14,
        7,0,188,192,1,0,0,0,189,192,5,6,0,0,190,192,5,7,0,0,191,176,1,0,
        0,0,191,181,1,0,0,0,191,185,1,0,0,0,191,189,1,0,0,0,191,190,1,0,
        0,0,192,198,1,0,0,0,193,194,10,3,0,0,194,195,7,2,0,0,195,197,3,28,
        14,4,196,193,1,0,0,0,197,200,1,0,0,0,198,196,1,0,0,0,198,199,1,0,
        0,0,199,29,1,0,0,0,200,198,1,0,0,0,201,202,7,3,0,0,202,31,1,0,0,
        0,203,204,3,44,22,0,204,205,5,42,0,0,205,206,5,51,0,0,206,207,5,
        27,0,0,207,208,3,34,17,0,208,209,5,28,0,0,209,210,3,2,1,0,210,33,
        1,0,0,0,211,212,3,44,22,0,212,219,5,51,0,0,213,214,5,34,0,0,214,
        215,3,44,22,0,215,216,5,51,0,0,216,218,1,0,0,0,217,213,1,0,0,0,218,
        221,1,0,0,0,219,217,1,0,0,0,219,220,1,0,0,0,220,35,1,0,0,0,221,219,
        1,0,0,0,222,224,5,45,0,0,223,225,3,8,4,0,224,223,1,0,0,0,224,225,
        1,0,0,0,225,226,1,0,0,0,226,227,5,33,0,0,227,37,1,0,0,0,228,229,
        6,19,-1,0,229,230,3,40,20,0,230,236,1,0,0,0,231,232,10,2,0,0,232,
        233,7,4,0,0,233,235,3,40,20,0,234,231,1,0,0,0,235,238,1,0,0,0,236,
        234,1,0,0,0,236,237,1,0,0,0,237,39,1,0,0,0,238,236,1,0,0,0,239,240,
        6,20,-1,0,240,241,3,42,21,0,241,247,1,0,0,0,242,243,10,2,0,0,243,
        244,7,5,0,0,244,246,3,42,21,0,245,242,1,0,0,0,246,249,1,0,0,0,247,
        245,1,0,0,0,247,248,1,0,0,0,248,41,1,0,0,0,249,247,1,0,0,0,250,259,
        5,49,0,0,251,259,5,51,0,0,252,259,3,26,13,0,253,259,3,10,5,0,254,
        255,5,27,0,0,255,256,3,38,19,0,256,257,5,28,0,0,257,259,1,0,0,0,
        258,250,1,0,0,0,258,251,1,0,0,0,258,252,1,0,0,0,258,253,1,0,0,0,
        258,254,1,0,0,0,259,43,1,0,0,0,260,261,7,6,0,0,261,45,1,0,0,0,262,
        263,5,35,0,0,263,264,5,27,0,0,264,265,3,28,14,0,265,266,5,28,0,0,
        266,269,3,2,1,0,267,268,5,36,0,0,268,270,3,2,1,0,269,267,1,0,0,0,
        269,270,1,0,0,0,270,47,1,0,0,0,271,274,3,50,25,0,272,274,3,52,26,
        0,273,271,1,0,0,0,273,272,1,0,0,0,274,49,1,0,0,0,275,276,5,38,0,
        0,276,279,5,27,0,0,277,280,5,51,0,0,278,280,3,6,3,0,279,277,1,0,
        0,0,279,278,1,0,0,0,279,280,1,0,0,0,280,281,1,0,0,0,281,282,5,33,
        0,0,282,283,3,28,14,0,283,284,5,33,0,0,284,285,3,2,1,0,285,286,5,
        28,0,0,286,287,3,2,1,0,287,51,1,0,0,0,288,289,5,39,0,0,289,290,5,
        27,0,0,290,291,3,28,14,0,291,292,5,28,0,0,292,293,3,2,1,0,293,53,
        1,0,0,0,294,295,5,43,0,0,295,296,5,27,0,0,296,297,3,2,1,0,297,298,
        5,28,0,0,298,299,5,33,0,0,299,55,1,0,0,0,300,301,5,46,0,0,301,302,
        5,27,0,0,302,303,5,51,0,0,303,304,5,28,0,0,304,305,5,33,0,0,305,
        57,1,0,0,0,24,61,75,81,87,105,117,121,125,129,137,147,153,160,170,
        191,198,219,224,236,247,258,269,273,279
    ]

class KonturParser ( Parser ):

    grammarFileName = "Kontur.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'string'", "'int'", "'float'", "'bool'", 
                     "'matrix'", "'true'", "'false'", "'='", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'''", "'~'", "'++'", "'--'", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'||'", 
                     "'&&'", "'!'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "';'", "','", "'if'", "'else'", "'elif'", "'for'", 
                     "'while'", "'continue'", "'break'", "'func'", "'display'", 
                     "'input'", "'return'", "'plot'" ]

    symbolicNames = [ "<INVALID>", "TYPE_STRING", "TYPE_INT", "TYPE_FLOAT", 
                      "TYPE_BOOL", "TYPE_MATRIX", "TRUE_VALUE", "FALSE_VALUE", 
                      "ASSIGN", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MODULO", 
                      "TRANSPOSITION", "INVERT_MATRIX", "INCREMENT", "DECREMENT", 
                      "EQUAL", "NOT_EQUAL", "LESS_THAN", "LESS_EQUAL", "GREATER_THAN", 
                      "GREATER_EQUAL", "OR", "AND", "NOT", "LEFT_PAREN", 
                      "RIGHT_PAREN", "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", 
                      "RIGHT_BRACE", "SEMICOLON", "COMMA", "IF_INSTR", "ELSE_INSTR", 
                      "ELIF_INSTR", "FOR_INSTR", "WHILE_INSTR", "CONTINUE_INSTR", 
                      "BREAK_INSTR", "FUNC_INSTR", "DISPLAY_INSTR", "INPUT_INSTR", 
                      "RETURN_INSTR", "PLOT_INSTR", "COMMENT", "WHITE_SPACE", 
                      "NUMBER", "STRING", "IDENTIFIER" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_block = 2
    RULE_assignment = 3
    RULE_expression = 4
    RULE_indexedVar = 5
    RULE_indexList = 6
    RULE_matrixExpression = 7
    RULE_matrixAtom = 8
    RULE_matrixConstruction = 9
    RULE_row = 10
    RULE_value = 11
    RULE_stringExpression = 12
    RULE_funcCall = 13
    RULE_boolExpression = 14
    RULE_comparisonOperator = 15
    RULE_funcDecl = 16
    RULE_parameters = 17
    RULE_returnDecl = 18
    RULE_numExpression = 19
    RULE_term = 20
    RULE_factor = 21
    RULE_typeName = 22
    RULE_ifStatement = 23
    RULE_loopStatement = 24
    RULE_forLoop = 25
    RULE_whileLoop = 26
    RULE_displayDecl = 27
    RULE_plotDecl = 28

    ruleNames =  [ "program", "statement", "block", "assignment", "expression", 
                   "indexedVar", "indexList", "matrixExpression", "matrixAtom", 
                   "matrixConstruction", "row", "value", "stringExpression", 
                   "funcCall", "boolExpression", "comparisonOperator", "funcDecl", 
                   "parameters", "returnDecl", "numExpression", "term", 
                   "factor", "typeName", "ifStatement", "loopStatement", 
                   "forLoop", "whileLoop", "displayDecl", "plotDecl" ]

    EOF = Token.EOF
    TYPE_STRING=1
    TYPE_INT=2
    TYPE_FLOAT=3
    TYPE_BOOL=4
    TYPE_MATRIX=5
    TRUE_VALUE=6
    FALSE_VALUE=7
    ASSIGN=8
    PLUS=9
    MINUS=10
    MULTIPLY=11
    DIVIDE=12
    MODULO=13
    TRANSPOSITION=14
    INVERT_MATRIX=15
    INCREMENT=16
    DECREMENT=17
    EQUAL=18
    NOT_EQUAL=19
    LESS_THAN=20
    LESS_EQUAL=21
    GREATER_THAN=22
    GREATER_EQUAL=23
    OR=24
    AND=25
    NOT=26
    LEFT_PAREN=27
    RIGHT_PAREN=28
    LEFT_BRACKET=29
    RIGHT_BRACKET=30
    LEFT_BRACE=31
    RIGHT_BRACE=32
    SEMICOLON=33
    COMMA=34
    IF_INSTR=35
    ELSE_INSTR=36
    ELIF_INSTR=37
    FOR_INSTR=38
    WHILE_INSTR=39
    CONTINUE_INSTR=40
    BREAK_INSTR=41
    FUNC_INSTR=42
    DISPLAY_INSTR=43
    INPUT_INSTR=44
    RETURN_INSTR=45
    PLOT_INSTR=46
    COMMENT=47
    WHITE_SPACE=48
    NUMBER=49
    STRING=50
    IDENTIFIER=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(KonturParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KonturParser.StatementContext)
            else:
                return self.getTypedRuleContext(KonturParser.StatementContext,i)


        def getRuleIndex(self):
            return KonturParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = KonturParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4055860695302398) != 0):
                self.state = 58
                self.statement()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(KonturParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(KonturParser.BlockContext,0)


        def assignment(self):
            return self.getTypedRuleContext(KonturParser.AssignmentContext,0)


        def expression(self):
            return self.getTypedRuleContext(KonturParser.ExpressionContext,0)


        def funcDecl(self):
            return self.getTypedRuleContext(KonturParser.FuncDeclContext,0)


        def plotDecl(self):
            return self.getTypedRuleContext(KonturParser.PlotDeclContext,0)


        def returnDecl(self):
            return self.getTypedRuleContext(KonturParser.ReturnDeclContext,0)


        def loopStatement(self):
            return self.getTypedRuleContext(KonturParser.LoopStatementContext,0)


        def displayDecl(self):
            return self.getTypedRuleContext(KonturParser.DisplayDeclContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(KonturParser.IfStatementContext,0)


        def getRuleIndex(self):
            return KonturParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = KonturParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                self.funcDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 70
                self.plotDecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 71
                self.returnDecl()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 72
                self.loopStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 73
                self.displayDecl()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 74
                self.ifStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACE(self):
            return self.getToken(KonturParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(KonturParser.RIGHT_BRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KonturParser.StatementContext)
            else:
                return self.getTypedRuleContext(KonturParser.StatementContext,i)


        def getRuleIndex(self):
            return KonturParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = KonturParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(KonturParser.LEFT_BRACE)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4055860695302398) != 0):
                self.state = 78
                self.statement()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(KonturParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(KonturParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(KonturParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(KonturParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(KonturParser.SEMICOLON, 0)

        def typeName(self):
            return self.getTypedRuleContext(KonturParser.TypeNameContext,0)


        def getRuleIndex(self):
            return KonturParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = KonturParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 62) != 0):
                self.state = 86
                self.typeName()


            self.state = 89
            self.match(KonturParser.IDENTIFIER)
            self.state = 90
            self.match(KonturParser.ASSIGN)
            self.state = 91
            self.expression()
            self.state = 92
            self.match(KonturParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numExpression(self):
            return self.getTypedRuleContext(KonturParser.NumExpressionContext,0)


        def matrixExpression(self):
            return self.getTypedRuleContext(KonturParser.MatrixExpressionContext,0)


        def stringExpression(self):
            return self.getTypedRuleContext(KonturParser.StringExpressionContext,0)


        def boolExpression(self):
            return self.getTypedRuleContext(KonturParser.BoolExpressionContext,0)


        def funcCall(self):
            return self.getTypedRuleContext(KonturParser.FuncCallContext,0)


        def indexedVar(self):
            return self.getTypedRuleContext(KonturParser.IndexedVarContext,0)


        def IDENTIFIER(self):
            return self.getToken(KonturParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(KonturParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(KonturParser.STRING, 0)

        def TRUE_VALUE(self):
            return self.getToken(KonturParser.TRUE_VALUE, 0)

        def FALSE_VALUE(self):
            return self.getToken(KonturParser.FALSE_VALUE, 0)

        def getRuleIndex(self):
            return KonturParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = KonturParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression)
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.numExpression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.matrixExpression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                self.stringExpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 97
                self.boolExpression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 98
                self.funcCall()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 99
                self.indexedVar()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 100
                self.match(KonturParser.IDENTIFIER)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 101
                self.match(KonturParser.NUMBER)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 102
                self.match(KonturParser.STRING)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 103
                self.match(KonturParser.TRUE_VALUE)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 104
                self.match(KonturParser.FALSE_VALUE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexedVarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(KonturParser.IDENTIFIER, 0)

        def LEFT_BRACKET(self):
            return self.getToken(KonturParser.LEFT_BRACKET, 0)

        def indexList(self):
            return self.getTypedRuleContext(KonturParser.IndexListContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(KonturParser.RIGHT_BRACKET, 0)

        def getRuleIndex(self):
            return KonturParser.RULE_indexedVar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexedVar" ):
                listener.enterIndexedVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexedVar" ):
                listener.exitIndexedVar(self)




    def indexedVar(self):

        localctx = KonturParser.IndexedVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_indexedVar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(KonturParser.IDENTIFIER)
            self.state = 108
            self.match(KonturParser.LEFT_BRACKET)
            self.state = 109
            self.indexList()
            self.state = 110
            self.match(KonturParser.RIGHT_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KonturParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(KonturParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(KonturParser.COMMA)
            else:
                return self.getToken(KonturParser.COMMA, i)

        def getRuleIndex(self):
            return KonturParser.RULE_indexList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexList" ):
                listener.enterIndexList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexList" ):
                listener.exitIndexList(self)




    def indexList(self):

        localctx = KonturParser.IndexListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_indexList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.expression()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 113
                self.match(KonturParser.COMMA)
                self.state = 114
                self.expression()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def matrixAtom(self):
            return self.getTypedRuleContext(KonturParser.MatrixAtomContext,0)


        def INVERT_MATRIX(self):
            return self.getToken(KonturParser.INVERT_MATRIX, 0)

        def TRANSPOSITION(self):
            return self.getToken(KonturParser.TRANSPOSITION, 0)

        def getRuleIndex(self):
            return KonturParser.RULE_matrixExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixExpression" ):
                listener.enterMatrixExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixExpression" ):
                listener.exitMatrixExpression(self)




    def matrixExpression(self):

        localctx = KonturParser.MatrixExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_matrixExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 120
                self.match(KonturParser.INVERT_MATRIX)


            self.state = 123
            self.matrixAtom()
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 124
                self.match(KonturParser.TRANSPOSITION)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixAtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(KonturParser.IDENTIFIER, 0)

        def matrixConstruction(self):
            return self.getTypedRuleContext(KonturParser.MatrixConstructionContext,0)


        def getRuleIndex(self):
            return KonturParser.RULE_matrixAtom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixAtom" ):
                listener.enterMatrixAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixAtom" ):
                listener.exitMatrixAtom(self)




    def matrixAtom(self):

        localctx = KonturParser.MatrixAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_matrixAtom)
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.match(KonturParser.IDENTIFIER)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.matrixConstruction()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixConstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACKET(self):
            return self.getToken(KonturParser.LEFT_BRACKET, 0)

        def row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KonturParser.RowContext)
            else:
                return self.getTypedRuleContext(KonturParser.RowContext,i)


        def RIGHT_BRACKET(self):
            return self.getToken(KonturParser.RIGHT_BRACKET, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(KonturParser.SEMICOLON)
            else:
                return self.getToken(KonturParser.SEMICOLON, i)

        def getRuleIndex(self):
            return KonturParser.RULE_matrixConstruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixConstruction" ):
                listener.enterMatrixConstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixConstruction" ):
                listener.exitMatrixConstruction(self)




    def matrixConstruction(self):

        localctx = KonturParser.MatrixConstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_matrixConstruction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(KonturParser.LEFT_BRACKET)
            self.state = 132
            self.row()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 133
                self.match(KonturParser.SEMICOLON)
                self.state = 134
                self.row()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 140
            self.match(KonturParser.RIGHT_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KonturParser.ValueContext)
            else:
                return self.getTypedRuleContext(KonturParser.ValueContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(KonturParser.COMMA)
            else:
                return self.getToken(KonturParser.COMMA, i)

        def getRuleIndex(self):
            return KonturParser.RULE_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRow" ):
                listener.enterRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRow" ):
                listener.exitRow(self)




    def row(self):

        localctx = KonturParser.RowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_row)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.value()
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 143
                self.match(KonturParser.COMMA)
                self.state = 144
                self.value()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(KonturParser.NUMBER, 0)

        def IDENTIFIER(self):
            return self.getToken(KonturParser.IDENTIFIER, 0)

        def matrixExpression(self):
            return self.getTypedRuleContext(KonturParser.MatrixExpressionContext,0)


        def getRuleIndex(self):
            return KonturParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = KonturParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_value)
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.match(KonturParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.match(KonturParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 152
                self.matrixExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(KonturParser.STRING)
            else:
                return self.getToken(KonturParser.STRING, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(KonturParser.IDENTIFIER)
            else:
                return self.getToken(KonturParser.IDENTIFIER, i)

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(KonturParser.PLUS)
            else:
                return self.getToken(KonturParser.PLUS, i)

        def getRuleIndex(self):
            return KonturParser.RULE_stringExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpression" ):
                listener.enterStringExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpression" ):
                listener.exitStringExpression(self)




    def stringExpression(self):

        localctx = KonturParser.StringExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_stringExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            _la = self._input.LA(1)
            if not(_la==50 or _la==51):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 160
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 156
                    self.match(KonturParser.PLUS)
                    self.state = 157
                    _la = self._input.LA(1)
                    if not(_la==50 or _la==51):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 162
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(KonturParser.IDENTIFIER)
            else:
                return self.getToken(KonturParser.IDENTIFIER, i)

        def LEFT_PAREN(self):
            return self.getToken(KonturParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(KonturParser.RIGHT_PAREN, 0)

        def SEMICOLON(self):
            return self.getToken(KonturParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(KonturParser.COMMA)
            else:
                return self.getToken(KonturParser.COMMA, i)

        def getRuleIndex(self):
            return KonturParser.RULE_funcCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCall" ):
                listener.enterFuncCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCall" ):
                listener.exitFuncCall(self)




    def funcCall(self):

        localctx = KonturParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(KonturParser.IDENTIFIER)
            self.state = 164
            self.match(KonturParser.LEFT_PAREN)
            self.state = 165
            self.match(KonturParser.IDENTIFIER)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 166
                self.match(KonturParser.COMMA)
                self.state = 167
                self.match(KonturParser.IDENTIFIER)
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 173
            self.match(KonturParser.RIGHT_PAREN)
            self.state = 174
            self.match(KonturParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.operator = None # Token

        def numExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KonturParser.NumExpressionContext)
            else:
                return self.getTypedRuleContext(KonturParser.NumExpressionContext,i)


        def comparisonOperator(self):
            return self.getTypedRuleContext(KonturParser.ComparisonOperatorContext,0)


        def stringExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KonturParser.StringExpressionContext)
            else:
                return self.getTypedRuleContext(KonturParser.StringExpressionContext,i)


        def EQUAL(self):
            return self.getToken(KonturParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(KonturParser.NOT_EQUAL, 0)

        def matrixExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KonturParser.MatrixExpressionContext)
            else:
                return self.getTypedRuleContext(KonturParser.MatrixExpressionContext,i)


        def TRUE_VALUE(self):
            return self.getToken(KonturParser.TRUE_VALUE, 0)

        def FALSE_VALUE(self):
            return self.getToken(KonturParser.FALSE_VALUE, 0)

        def boolExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KonturParser.BoolExpressionContext)
            else:
                return self.getTypedRuleContext(KonturParser.BoolExpressionContext,i)


        def AND(self):
            return self.getToken(KonturParser.AND, 0)

        def OR(self):
            return self.getToken(KonturParser.OR, 0)

        def getRuleIndex(self):
            return KonturParser.RULE_boolExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolExpression" ):
                listener.enterBoolExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolExpression" ):
                listener.exitBoolExpression(self)



    def boolExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = KonturParser.BoolExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_boolExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 177
                self.numExpression(0)
                self.state = 178
                self.comparisonOperator()
                self.state = 179
                self.numExpression(0)
                pass

            elif la_ == 2:
                self.state = 181
                self.stringExpression()
                self.state = 182
                localctx.operator = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    localctx.operator = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 183
                self.stringExpression()
                pass

            elif la_ == 3:
                self.state = 185
                self.matrixExpression()
                self.state = 186
                localctx.operator = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    localctx.operator = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 187
                self.matrixExpression()
                pass

            elif la_ == 4:
                self.state = 189
                self.match(KonturParser.TRUE_VALUE)
                pass

            elif la_ == 5:
                self.state = 190
                self.match(KonturParser.FALSE_VALUE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 198
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = KonturParser.BoolExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_boolExpression)
                    self.state = 193
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 194
                    localctx.operator = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==24 or _la==25):
                        localctx.operator = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 195
                    self.boolExpression(4) 
                self.state = 200
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComparisonOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(KonturParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(KonturParser.NOT_EQUAL, 0)

        def LESS_THAN(self):
            return self.getToken(KonturParser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(KonturParser.GREATER_THAN, 0)

        def LESS_EQUAL(self):
            return self.getToken(KonturParser.LESS_EQUAL, 0)

        def GREATER_EQUAL(self):
            return self.getToken(KonturParser.GREATER_EQUAL, 0)

        def getRuleIndex(self):
            return KonturParser.RULE_comparisonOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOperator" ):
                listener.enterComparisonOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOperator" ):
                listener.exitComparisonOperator(self)




    def comparisonOperator(self):

        localctx = KonturParser.ComparisonOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_comparisonOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16515072) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeName(self):
            return self.getTypedRuleContext(KonturParser.TypeNameContext,0)


        def FUNC_INSTR(self):
            return self.getToken(KonturParser.FUNC_INSTR, 0)

        def IDENTIFIER(self):
            return self.getToken(KonturParser.IDENTIFIER, 0)

        def LEFT_PAREN(self):
            return self.getToken(KonturParser.LEFT_PAREN, 0)

        def parameters(self):
            return self.getTypedRuleContext(KonturParser.ParametersContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(KonturParser.RIGHT_PAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(KonturParser.StatementContext,0)


        def getRuleIndex(self):
            return KonturParser.RULE_funcDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDecl" ):
                listener.enterFuncDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDecl" ):
                listener.exitFuncDecl(self)




    def funcDecl(self):

        localctx = KonturParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_funcDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.typeName()
            self.state = 204
            self.match(KonturParser.FUNC_INSTR)
            self.state = 205
            self.match(KonturParser.IDENTIFIER)
            self.state = 206
            self.match(KonturParser.LEFT_PAREN)
            self.state = 207
            self.parameters()
            self.state = 208
            self.match(KonturParser.RIGHT_PAREN)
            self.state = 209
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KonturParser.TypeNameContext)
            else:
                return self.getTypedRuleContext(KonturParser.TypeNameContext,i)


        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(KonturParser.IDENTIFIER)
            else:
                return self.getToken(KonturParser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(KonturParser.COMMA)
            else:
                return self.getToken(KonturParser.COMMA, i)

        def getRuleIndex(self):
            return KonturParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = KonturParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.typeName()
            self.state = 212
            self.match(KonturParser.IDENTIFIER)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 213
                self.match(KonturParser.COMMA)
                self.state = 214
                self.typeName()
                self.state = 215
                self.match(KonturParser.IDENTIFIER)
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_INSTR(self):
            return self.getToken(KonturParser.RETURN_INSTR, 0)

        def SEMICOLON(self):
            return self.getToken(KonturParser.SEMICOLON, 0)

        def expression(self):
            return self.getTypedRuleContext(KonturParser.ExpressionContext,0)


        def getRuleIndex(self):
            return KonturParser.RULE_returnDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnDecl" ):
                listener.enterReturnDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnDecl" ):
                listener.exitReturnDecl(self)




    def returnDecl(self):

        localctx = KonturParser.ReturnDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_returnDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(KonturParser.RETURN_INSTR)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3940650345070784) != 0):
                self.state = 223
                self.expression()


            self.state = 226
            self.match(KonturParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(KonturParser.TermContext,0)


        def numExpression(self):
            return self.getTypedRuleContext(KonturParser.NumExpressionContext,0)


        def PLUS(self):
            return self.getToken(KonturParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(KonturParser.MINUS, 0)

        def getRuleIndex(self):
            return KonturParser.RULE_numExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumExpression" ):
                listener.enterNumExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumExpression" ):
                listener.exitNumExpression(self)



    def numExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = KonturParser.NumExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_numExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 236
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = KonturParser.NumExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_numExpression)
                    self.state = 231
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 232
                    _la = self._input.LA(1)
                    if not(_la==9 or _la==10):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 233
                    self.term(0) 
                self.state = 238
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(KonturParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(KonturParser.TermContext,0)


        def MULTIPLY(self):
            return self.getToken(KonturParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(KonturParser.DIVIDE, 0)

        def MODULO(self):
            return self.getToken(KonturParser.MODULO, 0)

        def getRuleIndex(self):
            return KonturParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = KonturParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_term, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 247
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = KonturParser.TermContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 242
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 243
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 244
                    self.factor() 
                self.state = 249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(KonturParser.NUMBER, 0)

        def IDENTIFIER(self):
            return self.getToken(KonturParser.IDENTIFIER, 0)

        def funcCall(self):
            return self.getTypedRuleContext(KonturParser.FuncCallContext,0)


        def indexedVar(self):
            return self.getTypedRuleContext(KonturParser.IndexedVarContext,0)


        def LEFT_PAREN(self):
            return self.getToken(KonturParser.LEFT_PAREN, 0)

        def numExpression(self):
            return self.getTypedRuleContext(KonturParser.NumExpressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(KonturParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return KonturParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = KonturParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_factor)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.match(KonturParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.match(KonturParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self.funcCall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 253
                self.indexedVar()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 254
                self.match(KonturParser.LEFT_PAREN)
                self.state = 255
                self.numExpression(0)
                self.state = 256
                self.match(KonturParser.RIGHT_PAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_STRING(self):
            return self.getToken(KonturParser.TYPE_STRING, 0)

        def TYPE_INT(self):
            return self.getToken(KonturParser.TYPE_INT, 0)

        def TYPE_FLOAT(self):
            return self.getToken(KonturParser.TYPE_FLOAT, 0)

        def TYPE_BOOL(self):
            return self.getToken(KonturParser.TYPE_BOOL, 0)

        def TYPE_MATRIX(self):
            return self.getToken(KonturParser.TYPE_MATRIX, 0)

        def getRuleIndex(self):
            return KonturParser.RULE_typeName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeName" ):
                listener.enterTypeName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeName" ):
                listener.exitTypeName(self)




    def typeName(self):

        localctx = KonturParser.TypeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_typeName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_INSTR(self):
            return self.getToken(KonturParser.IF_INSTR, 0)

        def LEFT_PAREN(self):
            return self.getToken(KonturParser.LEFT_PAREN, 0)

        def boolExpression(self):
            return self.getTypedRuleContext(KonturParser.BoolExpressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(KonturParser.RIGHT_PAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KonturParser.StatementContext)
            else:
                return self.getTypedRuleContext(KonturParser.StatementContext,i)


        def ELSE_INSTR(self):
            return self.getToken(KonturParser.ELSE_INSTR, 0)

        def getRuleIndex(self):
            return KonturParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = KonturParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(KonturParser.IF_INSTR)
            self.state = 263
            self.match(KonturParser.LEFT_PAREN)
            self.state = 264
            self.boolExpression(0)
            self.state = 265
            self.match(KonturParser.RIGHT_PAREN)
            self.state = 266
            self.statement()
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 267
                self.match(KonturParser.ELSE_INSTR)
                self.state = 268
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forLoop(self):
            return self.getTypedRuleContext(KonturParser.ForLoopContext,0)


        def whileLoop(self):
            return self.getTypedRuleContext(KonturParser.WhileLoopContext,0)


        def getRuleIndex(self):
            return KonturParser.RULE_loopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatement" ):
                listener.enterLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatement" ):
                listener.exitLoopStatement(self)




    def loopStatement(self):

        localctx = KonturParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_loopStatement)
        try:
            self.state = 273
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.forLoop()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.whileLoop()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR_INSTR(self):
            return self.getToken(KonturParser.FOR_INSTR, 0)

        def LEFT_PAREN(self):
            return self.getToken(KonturParser.LEFT_PAREN, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(KonturParser.SEMICOLON)
            else:
                return self.getToken(KonturParser.SEMICOLON, i)

        def boolExpression(self):
            return self.getTypedRuleContext(KonturParser.BoolExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KonturParser.StatementContext)
            else:
                return self.getTypedRuleContext(KonturParser.StatementContext,i)


        def RIGHT_PAREN(self):
            return self.getToken(KonturParser.RIGHT_PAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(KonturParser.IDENTIFIER, 0)

        def assignment(self):
            return self.getTypedRuleContext(KonturParser.AssignmentContext,0)


        def getRuleIndex(self):
            return KonturParser.RULE_forLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoop" ):
                listener.enterForLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoop" ):
                listener.exitForLoop(self)




    def forLoop(self):

        localctx = KonturParser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(KonturParser.FOR_INSTR)
            self.state = 276
            self.match(KonturParser.LEFT_PAREN)
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 277
                self.match(KonturParser.IDENTIFIER)

            elif la_ == 2:
                self.state = 278
                self.assignment()


            self.state = 281
            self.match(KonturParser.SEMICOLON)
            self.state = 282
            self.boolExpression(0)
            self.state = 283
            self.match(KonturParser.SEMICOLON)
            self.state = 284
            self.statement()
            self.state = 285
            self.match(KonturParser.RIGHT_PAREN)
            self.state = 286
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE_INSTR(self):
            return self.getToken(KonturParser.WHILE_INSTR, 0)

        def LEFT_PAREN(self):
            return self.getToken(KonturParser.LEFT_PAREN, 0)

        def boolExpression(self):
            return self.getTypedRuleContext(KonturParser.BoolExpressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(KonturParser.RIGHT_PAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(KonturParser.StatementContext,0)


        def getRuleIndex(self):
            return KonturParser.RULE_whileLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileLoop" ):
                listener.enterWhileLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileLoop" ):
                listener.exitWhileLoop(self)




    def whileLoop(self):

        localctx = KonturParser.WhileLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(KonturParser.WHILE_INSTR)
            self.state = 289
            self.match(KonturParser.LEFT_PAREN)
            self.state = 290
            self.boolExpression(0)
            self.state = 291
            self.match(KonturParser.RIGHT_PAREN)
            self.state = 292
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DisplayDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DISPLAY_INSTR(self):
            return self.getToken(KonturParser.DISPLAY_INSTR, 0)

        def LEFT_PAREN(self):
            return self.getToken(KonturParser.LEFT_PAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(KonturParser.StatementContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(KonturParser.RIGHT_PAREN, 0)

        def SEMICOLON(self):
            return self.getToken(KonturParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return KonturParser.RULE_displayDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisplayDecl" ):
                listener.enterDisplayDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisplayDecl" ):
                listener.exitDisplayDecl(self)




    def displayDecl(self):

        localctx = KonturParser.DisplayDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_displayDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(KonturParser.DISPLAY_INSTR)
            self.state = 295
            self.match(KonturParser.LEFT_PAREN)
            self.state = 296
            self.statement()
            self.state = 297
            self.match(KonturParser.RIGHT_PAREN)
            self.state = 298
            self.match(KonturParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlotDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLOT_INSTR(self):
            return self.getToken(KonturParser.PLOT_INSTR, 0)

        def LEFT_PAREN(self):
            return self.getToken(KonturParser.LEFT_PAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(KonturParser.IDENTIFIER, 0)

        def RIGHT_PAREN(self):
            return self.getToken(KonturParser.RIGHT_PAREN, 0)

        def SEMICOLON(self):
            return self.getToken(KonturParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return KonturParser.RULE_plotDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlotDecl" ):
                listener.enterPlotDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlotDecl" ):
                listener.exitPlotDecl(self)




    def plotDecl(self):

        localctx = KonturParser.PlotDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_plotDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(KonturParser.PLOT_INSTR)
            self.state = 301
            self.match(KonturParser.LEFT_PAREN)
            self.state = 302
            self.match(KonturParser.IDENTIFIER)
            self.state = 303
            self.match(KonturParser.RIGHT_PAREN)
            self.state = 304
            self.match(KonturParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.boolExpression_sempred
        self._predicates[19] = self.numExpression_sempred
        self._predicates[20] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def boolExpression_sempred(self, localctx:BoolExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

    def numExpression_sempred(self, localctx:NumExpressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




