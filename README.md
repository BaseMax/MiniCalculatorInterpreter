# Mini Calculator Interpreter

Tiny calculator interpreter with supporting Mathematical functions using Python.

<img alt="Mini Calculator Interpreter python" src="https://raw.githubusercontent.com/BaseMax/MiniCalculatorInterpreter/master/demo.jpg" width="300">

## Features

- Variable
- Mathematical Constants
- Mathematical Functions

### Mathematical Constants

- pi
- e

### Mathematical Functions

- sin
- cos
- log
- log10
- log2
- exp
- sqrt
- acos
- atan
- radians
- sinh
- cosh
- tanh
- asin
- ceil
- fabs
- actorial
- loor
- copysign
- pow

### Download

```
git clone https://github.com/BaseMax/MiniCalculatorInterpreter
cd MiniCalculatorInterpreter
sudo pip3 install ply
python calculator.py
```

### Grammer

```
S -> statement

statement -> NAME EQUALS expression
statement -> expression,statement

expression -> expression PLUS expression
expression -> expression MINUS expression
expression -> expression DIVIDE expression
expression -> expression TIMES expression
expression -> MINUS expression
expression -> LPAREN expression RPAREN

expressions -> expressions COLON expression
expressions -> expression
expressions -> <empty>

expression -> NAME LPAREN expressions RPAREN
expression -> NUMBER_INT
expression -> NUMBER_DOUBLE
expression -> NAME
```

### Using

```
> 5+5
10
> 5*6
30
> pow(5,2)
25.0
> pi*2  
6.283185307179586
> e/2
1.3591409142295225
> log10(10)
1.0
> badFunction(10)
Undefined function 'badFunction'
None
> log2(10)
3.321928094887362
> log(10)
2.302585092994046
> test=5+6+sin(pi/2)
> test*test+5
149.0
> test=test*5
> test
60.0
```

----

# Max Base

My nickname is Max, Programming language developer, Full-stack programmer. I love computer scientists, researchers, and compilers. [Max Base]https://maxbase.org/))

## Asrez Team

A team includes some programmer, developer, designer, researchers) especially Max Base.

[Asrez Team]https://www.asrez.com/)

