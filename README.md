# Dokumentacja języka programowania Kontur

---

## Dane studentów

- Mateusz Działowski - mdzialowski@student.agh.edu.pl
- Gabriel Filipowicz - g13filip@gmail.com
- Filip Duda - fduda@student.agh.edu.pl

---

## Założenia programu

### Ogólne cele

Celem projektu jest stworzenie własnego języka programowania o składni inspirowanej MATLAB-em. Język umożliwia:
- operacje na zmiennych liczbowych, logicznych, tekstowych i macierzowych,
- pisanie własnych funkcji,
- wykonywanie obliczeń matematycznych i logicznych,
- tworzenie prostych wizualizacji.

### Rodzaj translatora

- **Rodzaj:** Interpreter

### Planowany wynik działania programu

Interpreter języka **Kontur**, który:
- analizuje kod źródłowy w języku Kontur,
- buduje drzewo składniowe (AST),
- interpretuje i wykonuje kod krok po kroku,
- wspiera funkcje, logikę, operacje na macierzach,
- wyświetla wyniki i wykresy.

### Język implementacji

- **Python 3.10+**

### Realizacja skanera/parsera

- **Narzędzie:** ANTLR 4
- **Gramatyka:** opisana w pliku `Kontur.g4`
- **Metoda:** Visitor Pattern (analiza AST)

---

## Tabela tokenów języka Kontur

### Typy danych i wartości logiczne

| Token         | Opis                          | Przykład     |
|---------------|-------------------------------|--------------|
| `TYPE_INT`     | typ danych całkowitych        | `int`        |
| `TYPE_FLOAT`   | typ zmiennoprzecinkowy        | `float`      |
| `TYPE_STRING`  | typ tekstowy                  | `string`     |
| `TYPE_BOOL`    | typ logiczny                  | `bool`       |
| `TYPE_MATRIX`  | typ macierzowy                | `matrix`     |
| `TRUE_VALUE`   | wartość logiczna `true`       | `true`       |
| `FALSE_VALUE`  | wartość logiczna `false`      | `false`      |

### Operatory matematyczne i logiczne

| Token           | Opis                            | Przykład |
|----------------|----------------------------------|----------|
| `ASSIGN`        | przypisanie                     | `=`      |
| `PLUS`          | dodawanie                       | `+`      |
| `MINUS`         | odejmowanie                     | `-`      |
| `MULTIPLY`      | mnożenie                        | `*`      |
| `DIVIDE`        | dzielenie                       | `/`      |
| `MODULO`        | reszta z dzielenia              | `%`      |
| `INCREMENT`     | inkrementacja                   | `++`     |
| `DECREMENT`     | dekrementacja                   | `--`     |
| `TRANSPOSITION` | transpozycja macierzy           | `'`      |
| `INVERT_MATRIX` | odwrócenie macierzy             | `~`      |
| `EQUAL`         | porównanie: równość             | `==`     |
| `NOT_EQUAL`     | porównanie: nierówność          | `!=`     |
| `LESS_THAN`     | porównanie: mniejsze            | `<`      |
| `LESS_EQUAL`    | porównanie: mniejsze/równe      | `<=`     |
| `GREATER_THAN`  | porównanie: większe             | `>`      |
| `GREATER_EQUAL` | porównanie: większe/równe       | `>=`     |
| `AND`           | operator logiczny "i"           | `&&`     |
| `OR`            | operator logiczny "lub"         | `\|\|`     |
| `NOT`           | operator logiczny "nie"         | `!`      |


### Znaki specjalne i separatory

| Token           | Opis                            | Przykład |
|----------------|----------------------------------|----------|
| `LEFT_PAREN`    | nawias otwierający              | `(`      |
| `RIGHT_PAREN`   | nawias zamykający               | `)`      |
| `LEFT_BRACKET`  | nawias kwadratowy otwierający   | `[`      |
| `RIGHT_BRACKET` | nawias kwadratowy zamykający    | `]`      |
| `LEFT_BRACE`    | nawias klamrowy otwierający     | `{`      |
| `RIGHT_BRACE`   | nawias klamrowy zamykający      | `}`      |
| `SEMICOLON`     | średnik                         | `;`      |
| `COMMA`         | przecinek                       | `,`      |


### Słowa kluczowe

| Token             | Opis                         | Przykład    |
|------------------|------------------------------|-------------|
| `IF_INSTR`        | instrukcja warunkowa if      | `if`        |
| `ELSE_INSTR`      | instrukcja else              | `else`      |
| `ELIF_INSTR`      | instrukcja elif              | `elif`      |
| `FOR_INSTR`       | pętla for                    | `for`       |
| `WHILE_INSTR`     | pętla while                  | `while`     |
| `CONTINUE_INSTR`  | kontynuacja pętli            | `continue`  |
| `BREAK_INSTR`     | przerwanie pętli             | `break`     |
| `FUNC_INSTR`      | deklaracja funkcji           | `func`      |
| `RETURN_INSTR`    | instrukcja zwracania wartości| `return`    |
| `DISPLAY_INSTR`   | funkcja wypisująca dane      | `display`   |
| `PLOT_INSTR`      | funkcja rysująca wykres      | `plot`      |


### Inne tokeny

| Token        | Opis                                | Przykład           |
|--------------|-------------------------------------|--------------------|
| `IDENTIFIER` | nazwa zmiennej lub funkcji          | `x`, `suma`        |
| `COMMENT`    | komentarz                           | `// komentarz`     |
| `WHITE_SPACE`| biały znak                          | spacja, tab, enter |

---

## Gramatyka
```antlr
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
```


---

## Narzędzia i biblioteki

| Narzędzie                | Zastosowanie                    |
|--------------------------|---------------------------------|
| `ANTLR 4`                | Generator parsera i leksera     |
| `Python 3.10+`           | Interpreter                     |
| `antlr4-python3-runtime` | Wykonanie parsera w Pythonie    |

## Przykładowy kod źródłowy w języku Kontur

```kontur
// Deklaracje zmiennych różnych typów
int a = 5;
float pi = 3.14159;
string imie = "Kasia";
bool flaga = true;
matrix M = [1, 2; 3, 4];
matrix N = [4, 3; 2, 1];

// Operacje na macierzach
matrix suma = M + N;
matrix roznica = M - N;
matrix iloczyn = M * N;
matrix transpozycja = M';
matrix odwrotna = ~M;

// Indeksowanie macierzy
float element = M(1, 0);  // 2. wiersz, 1. kolumna

// Operacje arytmetyczne i logiczne
int wynik = a + 2 * 3;
bool warunek = (wynik > 10) && !flaga;

// Operacje na stringach i funkcje trygonometryczne
string powitanie = "Witaj, " + imie + "!";
float sinus = sin(pi / 2);
float cosinus = cos(0);

// Wyświetlanie wartości i wykresy
display(powitanie);
display("sin(pi/2) = " + sinus);
display("cos(0) = " + cosinus);
plot(M);

// Pętla for
for (int i = 0; i < 3; i = i + 1) {
    display("Licznik: " + i);
}

// Pętla while
while (a > 0) {
    display("a = " + a);
    a = a - 1;
}

// Warunek if / elif / else
if (wynik > 20) {
    display("Wynik większy niż 20");
} elif (wynik == 20) {
    display("Wynik równy 20");
} else {
    display("Wynik mniejszy niż 20");
}

// Funkcja użytkownika
func int dodaj(int x, int y) {
    return x + y;
}

int sumaWart = dodaj(10, 5);
display("Suma: " + sumaWart);

// Funkcja przyjmująca macierz
func wyswietlMacierz(matrix X) {
    display("Otrzymana macierz:");
    plot(X);
}

wyswietlMacierz(N);
