# Flowgen

## Project Description

FlowGen is an open-source tool will convert programs written in a custom-made language into flowcharts. The language is easy to write and specialised for flowcharts providing a simple intuitive way to design common flowchart requirements such as processes, decisions, I/O and loops more quickly.

Flowcharts can be very useful when visualising systems especially to those who don’t have technical knowledge as they abstract complex programs into simple diagrams that can be read like an instruction manual. In contrast a Computer Scientist may understand how to code but may not be gifted in making easy to understand flowcharts. 

This project aims to fix this problem and prove faster, more consistent and less error-prone diagrams. By utilising the consistency of a programming language, the user can focus on designing the logic of the program rather than the design aspect and the flowchart will be able to update in real time to give the user instant feedback on what they are creating.

## Syntax

### Overview
This programming language uses a structured, block-based syntax designed to make programs easy to read, write and understand. The language supports fundamental programming features, including **statements, functions, conditional logic, loops, input/output operations and selectable options**. It also supports **nested control-flow statements**, allowing more complex program structures to be created.

### Program Structure
Every program must start with a title. After this, it can contain processes, functions and control-flow statements.

### Statements and Processes

A statement is a name made up of letters, numbers and underscores. It must start with a letter or underscore.

A process is a statement followed by a semicolon (`;`).

### Functions
Functions group code together under a name. Each function contains a block of code inside curly braces (`{ }`).

### Conditional Statements
Conditional statements allow different blocks of code to run depending on a condition:
- **If:** Runs a block if its condition is met.
- **Elif:** Checks another condition if the previous one was not met.
- **Else:** Runs if none of the conditions were met.

These statements can be nested inside each other.

### Loops
The language supports two types of loops:
- **While:** Repeats a block while a condition is met.
- **For:** Uses three statements to control how a block repeats.

Both use curly braces (`{ }`) to contain their code.

### Options
Options allow users to define many paths for the flowchart to go down, each with its own block of code and path name. This is useful for things like menus.

### Input and Output
The `IO` keyword represents input and output operations within a program.

### Blocks and Nesting
Blocks group code together using curly braces (`{ }`). They can contain processes and other control-flow statements, allowing more complex structures to be built.

### Lexical Rules
Identifiers can contain:
- Uppercase letters (`A–Z`).
- Lowercase letters (`a–z`).
- Underscores (`_`).
- Numbers (`0–9`), as long as they are not the first character.
  
### Language Extended Backus–Naur form (EBNF)

```
Program = Title, {Process | Function | ControlFlowStatement};
Title = “title”, “=”, Process;
Process = Statement, “;”;
ControlFlowStatement = If | While | Loop | Options | IO;
Function = “function”, “:”, Statement, Block;
If = “if”, “(“, Statement,”)”, Block, {Elif}, Else;
Elif = “elif”, “(“, Statement,”)”, Block;
Else = “else”, Block;
While = “while”, “(“, Statement,”)”, Block;
Loop = “for”, “(“, Statement, “;”, Statement, “;”, Statement, “)”, Block;
Options = “options”, “{”, Option, {Option}, “}”;
Option = Statement, Block;
Block = “{”, {Process | ControlFlowStatement}, “}”;
IO = “IO”, “=”, Process;
Statement = ValidCharacter, {ValidCharacter | Digit};
ValidCharacter = UpperLetter | LowerLetter | “_”;
UpperLetter = "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" |"T" | "U" | "V" | "W" | "X" | "Y" | "Z”;
LowerLetter = "a" | "b" | "c" | "d" | "e" | "f" | "g"| "h" | "i" | "j" | "k" | "l" | "m" | "n"| "o" | "p" | "q" | "r" | "s" | "t" | "u"          | "v" | "w" | "x" | "y" | "z" ;
Digit = “0” | ”1” | ”2” | ”3” | ”4” | ”5” | ”6” | ”7” | ”8” | ”9”;
``` 
