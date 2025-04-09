grammar Kontur;

program: statement* EOF;

statement:
    LEFT_BRACE statement* RIGHT_BRACE
  | assignment
  | expression
  | funcDecl
  | plotDecl
  | returnDecl
  | loopStatement
  | displayDecl
  | ifStatement;

assignment: typeName IDENTIFIER ASSIGN expression SEMICOLON;

expression: numExpression | matrixExpression | stringExpression | boolExpression | funcExpression;

matrixExpression: (INVERT_MATRIX)? matrixAtom (TRANSPOSITION)?;
matrixAtom: IDENTIFIER | matrixConstruction;

matrixConstruction: LEFT_BRACKET row (SEMICOLON row)* RIGHT_BRACKET;
row: value (COMMA value)*;
value: NUMBER | IDENTIFIER | matrixExpression;

stringExpression: (STRING | IDENTIFIER) ( PLUS (STRING | IDENTIFIER))*;

funcExpression: IDENTIFIER LEFT_PAREN (IDENTIFIER)? ((COMMA IDENTIFIER)*)? RIGHT_PAREN SEMICOLON;

boolExpression: numExpression operator=('==' | '!=' | '<' | '>' | '<=' | '>=') numExpression
               |    stringExpression operator=('=='| '!=') stringExpression
               |    boolExpression operator=('&&' | '||')  boolExpression
               |    TRUE_VALUE
               |    FALSE_VALUE;


funcDecl: typeName FUNC_INSTR IDENTIFIER LEFT_PAREN parameters? RIGHT_PAREN statement;

parameters: typeName IDENTIFIER (COMMA typeName IDENTIFIER)*;

returnDecl: RETURN_INSTR (IDENTIFIER | expression) SEMICOLON;

numExpression: numExpression ('+'|'-') term | term;

term: term ('*'|'/') factor
    | factor;

factor: NUMBER
      | IDENTIFIER
      | '(' numExpression ')';
typeName: TYPE_STRING | TYPE_INT | TYPE_FLOAT | TYPE_BOOL | TYPE_MATRIX;

NUMBER: [0-9]+('.'[0-9]+)?;
STRING
    : '"' (ESC | ~["\\\r\n])* '"'
    | '\'' (ESC | ~['\\\r\n])* '\'';
fragment ESC
    : '\\' ["\\/bfnrt];


ifStatement: IF_INSTR LEFT_PAREN boolExpression RIGHT_PAREN statement;

loopStatement: forLoop | whileLoop;

forLoop: FOR_INSTR LEFT_PAREN (IDENTIFIER | assignment)? SEMICOLON
                               boolExpression SEMICOLON
                               statement RIGHT_PAREN
                               statement;
whileLoop:
           WHILE_INSTR LEFT_PAREN boolExpression RIGHT_PAREN statement;

displayDecl: DISPLAY_INSTR LEFT_PAREN STATEMENT RIGHT_PAREN SEMICOLON;

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
TRANSPOSITION   : '‘';
INVERT_MATRIX   : '!';
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

// -------------- Special Characters -------------
LEFT_PAREN      : '(';
RIGHT_PAREN     : ')';
LEFT_BRACKET    : '[';
RIGHT_BRACKET   : ']';
LEFT_BRACE      : '{';
RIGHT_BRACE     : '}';
SEMICOLON       : ';';
COMMA           : ',';
IDENTIFIER      : [a-zA-Z_][a-zA-Z0-9_]*;

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
