# Dokumentacja języka programowania Kontur

---

## Dane studentów

- Mateusz Działowski - mdzialowski@student.agh.edu.pl
- Gabriel Filipowicz - g13filip@gmail.com
- Filip Duda - fduda@student.agh.edu.pl

---

## Założenia projektu

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

## Gramatyka

Gramatyka znajduje się [tutaj](Gramatyka/Kontur.g4).

## Przykładowy kod źródłowy w języku Kontur

Przykładowy kod źródłowy języka znajduję się [tutaj](Gramatyka/plik.txt);


## Narzędzia i biblioteki

| Narzędzie                | Zastosowanie                    |
|--------------------------|---------------------------------|
| `ANTLR 4`                | Generator parsera i leksera     |
| `Python 3.10+`           | Interpreter                     |
| `antlr4-python3-runtime` | Wykonanie parsera w Pythonie    |

---

## Tabela tokenów języka Kontur

### Typy danych i wartości logiczne

| Token         | Opis                     | Przykład |
|---------------|--------------------------|----------|
| `TYPE_INT`    | typ danych całkowitych   | `int`    |
| `TYPE_FLOAT`  | typ zmiennoprzecinkowy   | `float`  |
| `TYPE_STRING` | typ tekstowy             | `string` |
| `TYPE_BOOL`   | typ logiczny             | `bool`   |
| `TYPE_MATRIX` | typ macierzowy           | `matrix` |
| `TYPE_VOID`   | typ void                 | `void`   |
| `TRUE_VALUE`  | wartość logiczna `true`  | `true`   |
| `FALSE_VALUE` | wartość logiczna `false` | `false`  |

### Operatory matematyczne i logiczne

| Token            | Opis                            | Przykład |
|------------------|---------------------------------|----------|
| `ASSIGN`         | przypisanie                     | `=`      |
| `PLUS`           | dodawanie                       | `+`      |
| `MINUS`          | odejmowanie                     | `-`      |
| `MULTIPLY`       | mnożenie                        | `*`      |
| `DIVIDE`         | dzielenie                       | `/`      |
| `MODULO`         | reszta z dzielenia              | `%`      |
| `INCREMENT`      | inkrementacja                   | `++`     |
| `DECREMENT`      | dekrementacja                   | `--`     |
| `ADD_TO`         | szybkie dodawanie do zmiennej   | `+=`     |
| `SUBSTRACT_FROM` | szybkie odejmowanie od zmiennej | `-=`     |
| `DIVIDE_FROM`    | szybkie dzielenie zmiennej      | `/=`     |
| `TIMES`          | szybkie mnożenie zmiennej       | `*=`     |
| `TRANSPOSITION`  | transpozycja macierzy           | `'`      |
| `INVERT_MATRIX`  | odwrócenie macierzy             | `~`      |
| `EQUAL`          | porównanie: równość             | `==`     |
| `NOT_EQUAL`      | porównanie: nierówność          | `!=`     |
| `LESS_THAN`      | porównanie: mniejsze            | `<`      |
| `LESS_EQUAL`     | porównanie: mniejsze/równe      | `<=`     |
| `GREATER_THAN`   | porównanie: większe             | `>`      |
| `GREATER_EQUAL`  | porównanie: większe/równe       | `>=`     |
| `AND`            | operator logiczny "i"           | `&&`     |
| `OR`             | operator logiczny "lub"         | `\|\|`   |
| `NOT`            | operator logiczny "nie"         | `!`      |


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

### Funkcje wbudowane

| Token        | Opis        | Przykład |
|--------------|-------------|----------|
| `SIN_FUNC`   | sinus       | `sin()`  |
| `COS_FUNC`   | cosinus     | `cos()`  |
| `TAN_FUNC`   | tangens     | `tan()`  |
| `CTAN_FUNC`  | kotangens   | `ctan()` |
| `POWER_FUNC` | potęgowanie | `pow()`  |



### Inne tokeny

| Token        | Opis                                | Przykład           |
|--------------|-------------------------------------|--------------------|
| `IDENTIFIER` | nazwa zmiennej lub funkcji          | `x`, `suma`        |
| `COMMENT`    | komentarz                           | `// komentarz`     |
| `WHITE_SPACE`| biały znak                          | spacja, tab, enter |

---




