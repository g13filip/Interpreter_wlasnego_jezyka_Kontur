grammar Kontur;

program: statement* EOF;

statement:
    block
  | assignment
  | expression
  | funcDecl
  | plotDecl
  | returnDecl
  | loopStatement
  | displayDecl
  | ifStatement;

block: LEFT_BRACE statement* RIGHT_BRACE;

assignment: typeName? IDENTIFIER ASSIGN expression SEMICOLON;

expression:   numExpression
            | matrixExpression
            | stringExpression
            | boolExpression
            | funcCall
            | indexedVar
            | IDENTIFIER
            | NUMBER
            | STRING
            | TRUE_VALUE
            | FALSE_VALUE;

indexedVar: IDENTIFIER LEFT_BRACKET indexList RIGHT_BRACKET;

indexList: expression (COMMA expression)*;

matrixExpression: (INVERT_MATRIX)? matrixAtom (TRANSPOSITION)?;
matrixAtom: IDENTIFIER | matrixConstruction;

matrixConstruction: LEFT_BRACKET row (SEMICOLON row)* RIGHT_BRACKET;
row: value (COMMA value)*;
value: NUMBER | IDENTIFIER | matrixExpression;

stringExpression: (STRING | IDENTIFIER) ( PLUS (STRING | IDENTIFIER))*;

funcCall: IDENTIFIER LEFT_PAREN IDENTIFIER (COMMA IDENTIFIER)* RIGHT_PAREN SEMICOLON;

boolExpression: numExpression comparisonOperator numExpression
               |    stringExpression operator=('=='| '!=') stringExpression
               |    matrixExpression operator=('==' | '!=') matrixExpression
               |    boolExpression operator=('&&' | '||')  boolExpression
               |    TRUE_VALUE
               |    FALSE_VALUE;

comparisonOperator:   EQUAL
                    | NOT_EQUAL
                    | LESS_THAN
                    | GREATER_THAN
                    | LESS_EQUAL
                    | GREATER_EQUAL
                    ;


funcDecl: typeName FUNC_INSTR IDENTIFIER LEFT_PAREN parameters RIGHT_PAREN statement;

parameters: typeName IDENTIFIER (COMMA typeName IDENTIFIER)*;

returnDecl: RETURN_INSTR (expression)? SEMICOLON;

numExpression: numExpression (PLUS|MINUS) term | term;

term: term (MULTIPLY|DIVIDE|MODULO) factor
    | factor;

factor: NUMBER
      | IDENTIFIER
      | funcCall
      | indexedVar
      | LEFT_PAREN numExpression RIGHT_PAREN;

typeName: TYPE_STRING | TYPE_INT | TYPE_FLOAT | TYPE_BOOL | TYPE_MATRIX;


ifStatement: IF_INSTR LEFT_PAREN boolExpression RIGHT_PAREN statement (ELSE_INSTR statement)?;

loopStatement: forLoop | whileLoop;

forLoop: FOR_INSTR LEFT_PAREN (IDENTIFIER | assignment)? SEMICOLON
                               boolExpression SEMICOLON
                               statement RIGHT_PAREN
                               statement;
whileLoop:
           WHILE_INSTR LEFT_PAREN boolExpression RIGHT_PAREN statement;

displayDecl: DISPLAY_INSTR LEFT_PAREN statement RIGHT_PAREN SEMICOLON;

plotDecl: PLOT_INSTR LEFT_PAREN IDENTIFIER RIGHT_PAREN SEMICOLON;

// ----------- Data Types ------------------
TYPE_STRING     : 'string';
TYPE_INT        : 'int';
TYPE_FLOAT      : 'float';
TYPE_BOOL       : 'bool';
TYPE_MATRIX     : 'matrix';
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


COMMENT  : '//' ~[\r\n]* -> skip;
WHITE_SPACE: [ \t\r\n]+ -> skip;
NUMBER: [0-9]+('.'[0-9]+)?;
STRING
    : '"' (ESC | ~["\\\r\n])* '"'
    | '\'' (ESC | ~['\\\r\n])* '\'';
fragment ESC
    : '\\' ["\\/bfnrt];
IDENTIFIER      : [a-zA-Z_][a-zA-Z0-9_]*;
