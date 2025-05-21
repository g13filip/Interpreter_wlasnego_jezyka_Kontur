grammar Kontur;

program: statement* EOF;

statement:
    assignment SEMICOLON
  | reassignment SEMICOLON
  | funcDecl
  | plotDecl
  | returnDecl
  | loopStatement
  | displayDecl
  | ifStatement
  | operation SEMICOLON;

loopStatements:
    assignment SEMICOLON
  | reassignment SEMICOLON
  | operation SEMICOLON
  | funcDecl
  | plotDecl
  | returnDecl
  | loopStatement
  | displayDecl
  | loopIfStatement
  | BREAK_INSTR SEMICOLON
  | CONTINUE_INSTR SEMICOLON;

block: LEFT_BRACE statement* RIGHT_BRACE;

assignment: typeName? IDENTIFIER (ASSIGN expression)?;

expression:   numExpression
            | matrixExpression
            | stringExpression
            | NOT? boolExpression
            | funcCall
            | indexedVar
            | IDENTIFIER
            | NUMBER
            | STRING;

indexedVar: IDENTIFIER LEFT_BRACKET indexList RIGHT_BRACKET;

indexList: expression (COMMA expression)*;

matrixExpression: (INVERT_MATRIX)? matrixAtom (TRANSPOSITION)?;
matrixAtom: IDENTIFIER | matrixConstruction;

matrixConstruction: LEFT_BRACE row (SEMICOLON row)* RIGHT_BRACE;
row: value (COMMA value)*;
value: NUMBER | IDENTIFIER | matrixExpression;

stringExpression: (STRING | IDENTIFIER) ( PLUS (STRING | IDENTIFIER))*;

funcCall: builtInFunctions |
            IDENTIFIER LEFT_PAREN (IDENTIFIER| expression) (COMMA (IDENTIFIER | expression))* RIGHT_PAREN;

builtInFunctions:POWER_FUNC LEFT_PAREN numExpression COMMA numExpression RIGHT_PAREN
                |
             (SIN_FUNC | COS_FUNC | TAN_FUNC | CTAN_FUNC )
              LEFT_PAREN numExpression RIGHT_PAREN;

boolExpression:  numExpression comparisonOperator numExpression
               |    stringExpression operator=('=='| '!=') stringExpression
               |    matrixExpression operator=('==' | '!=') matrixExpression
               |    boolExpression operator=('&&' | '||')  boolExpression
               |    NOT? LEFT_PAREN  boolExpression RIGHT_PAREN
               |    TRUE_VALUE
               |    FALSE_VALUE
               |    NOT? IDENTIFIER;

comparisonOperator:   EQUAL
                    | NOT_EQUAL
                    | LESS_THAN
                    | GREATER_THAN
                    | LESS_EQUAL
                    | GREATER_EQUAL;

funcDecl: FUNC_INSTR (typeName | TYPE_VOID) IDENTIFIER LEFT_PAREN parameters? RIGHT_PAREN block;

parameters: typeName IDENTIFIER (COMMA typeName IDENTIFIER)*;

returnDecl: RETURN_INSTR (expression)? SEMICOLON;

numExpression: numExpression (PLUS|MINUS) term | term;

term: term (MULTIPLY|DIVIDE|MODULO) factor
    | factor;

factor: NUMBER
      | IDENTIFIER
      | operation
      | indexedVar
      | LEFT_PAREN numExpression RIGHT_PAREN;

typeName: TYPE_STRING | TYPE_INT | TYPE_FLOAT | TYPE_BOOL | TYPE_MATRIX;

operation : (IDENTIFIER (INCREMENT | DECREMENT)) | funcCall;

reassignment: IDENTIFIER ((ADD_TO STRING | ADD_TO numExpression)
                          | SUBTRACT_FROM numExpression
                          | DIVIDE_FROM numExpression
                          | TIMES numExpression);


ifStatement: IF_INSTR LEFT_PAREN boolExpression RIGHT_PAREN (statement | block)

             (ELIF_INSTR LEFT_PAREN boolExpression RIGHT_PAREN (statement | block))*

             (ELSE_INSTR (statement | block))?;

loopIfStatement: IF_INSTR LEFT_PAREN boolExpression RIGHT_PAREN (LEFT_BRACE loopStatements+ RIGHT_BRACE | statement)

             (ELIF_INSTR LEFT_PAREN boolExpression RIGHT_PAREN (LEFT_BRACE loopStatements+ RIGHT_BRACE | statement))*

             (ELSE_INSTR (LEFT_BRACE loopStatements+ RIGHT_BRACE | statement))?;

loopStatement: forLoop | whileLoop;

forLoop: FOR_INSTR LEFT_PAREN (IDENTIFIER| assignment)? SEMICOLON
                               boolExpression SEMICOLON
                               (assignment | reassignment | operation) RIGHT_PAREN
                               (LEFT_BRACE loopStatements+ RIGHT_BRACE| statement);
whileLoop:
           WHILE_INSTR LEFT_PAREN boolExpression RIGHT_PAREN
           (LEFT_BRACE loopStatements+ RIGHT_BRACE | statement);

displayDecl: DISPLAY_INSTR LEFT_PAREN expression RIGHT_PAREN SEMICOLON;

plotDecl: PLOT_INSTR LEFT_PAREN (IDENTIFIER | matrixExpression) COMMA IDENTIFIER RIGHT_PAREN SEMICOLON;

// ----------- Data Types ------------------
TYPE_STRING     : 'string';
TYPE_INT        : 'int';
TYPE_FLOAT      : 'float';
TYPE_BOOL       : 'bool';
TYPE_MATRIX     : 'matrix';
TYPE_VOID       : 'void';
TRUE_VALUE      : 'true';
FALSE_VALUE     : 'false';

// ---------- Operators --------------------
ASSIGN          : '=';
PLUS            : '+';
MINUS           : '-';
MULTIPLY        : '*';
DIVIDE          : '/';
MODULO          : '%';
TRANSPOSITION   : '\'';
INVERT_MATRIX   : '~';
INCREMENT       : '++';
DECREMENT       : '--';
ADD_TO          : '+=';
SUBTRACT_FROM   : '-=';
TIMES           : '*=';
DIVIDE_FROM     : '/=';

// ------------ Logic Operators ------------------
EQUAL           : '==';
NOT_EQUAL       : '!=';
LESS_THAN       : '<';
LESS_EQUAL      : '<=';
GREATER_THAN    : '>';
GREATER_EQUAL   : '>=';
OR              : '||';
AND             : '&&';
NOT             : '!';

// -------------- Special Characters -------------
LEFT_PAREN      : '(';
RIGHT_PAREN     : ')';
LEFT_BRACKET    : '[';
RIGHT_BRACKET   : ']';
LEFT_BRACE      : '{';
RIGHT_BRACE     : '}';
SEMICOLON       : ';';
COMMA           : ',';

// ------------- Language Keyword --------------
IF_INSTR        : 'if';
ELSE_INSTR      : 'else';
ELIF_INSTR      : 'elif';
FOR_INSTR       : 'for';
WHILE_INSTR     : 'while';
CONTINUE_INSTR  : 'continue';
BREAK_INSTR     : 'break';
FUNC_INSTR      : 'func';
DISPLAY_INSTR   : 'display';
INPUT_INSTR     : 'input';
RETURN_INSTR    : 'return';
PLOT_INSTR      : 'plot';

// -------------- Built-in functions ------------
POWER_FUNC      : 'pow';
SIN_FUNC        : 'sin';
COS_FUNC        : 'cos';
TAN_FUNC        : 'tan';
CTAN_FUNC       : 'ctan';

// -------------- Else -----------------

COMMENT  : '//' ~[\r\n]* -> skip;
WHITE_SPACE: [ \t\r\n]+ -> skip;
NUMBER: [0-9]+('.'[0-9]+)?;
STRING
    : '"' (ESC | ~["\\\r\n])* '"'
    | '\'' (ESC | ~['\\\r\n])* '\'';
fragment ESC
    : '\\' ["\\/bfnrt];
IDENTIFIER      : [a-zA-Z_][a-zA-Z0-9_]*;
