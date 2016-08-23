# mini-compiler
:umbrella:

File extension: `.patrik`

## Example usage:
__File: hello.patrik:__
```go
func main:
    print 1+2
```

```
python compiler.py hello.patrik
output: hello.asm

nasm -f macho hello.asm
output: hello.o

ld hello.o
output: 3
```

## Grammar:

|               |   |                                                              |
|---------------|---|--------------------------------------------------------------|
| _Goal_        | = | _MainMehtod_                                                 |
| _MainMethod_  | = | __func__ __main__ __:__ __INDENT__ (_Statement_)* __DEDENT__  |
| _Statement_   | = | __print__ _Expression_                                       |
| _Expression_  | = | _Integer_ __+__ _Integer_                                    |
|               |   | _Integer_                                                    |

## Example programs

### 1.
```go
func main:
    print 1
    print 1+2
```
__Tokens:__
```
[FUNC, MAIN, COLON, INDENT, PRINT, INT(1), PRINT, INT(1), PLUS, INT(2), DEDENT]
```

__Parse tree:__
```
Goal(
    MainMethod([
        PrintStatement(
            IntExpression(1)
        ),
        PrintStatement(
            AddExpression(1, 2)
        ),
    ])
)
```

__Assembly:__
```
```

__Output:__
```
1
3
```
### 2.
```go
func main:
    print 39
```
__Tokens:__ 
```
[FUNC, MAIN, COLON, INDENT, PRINT, INT(39), DEDENT]
```

__Parse tree:__
```
Goal(
    MainMethod([
        PrintStatement(
            IntExpression(39)
        ),
    ])
)
```

__Output:__
```
39
```

## Ideas
http://www.csc.kth.se/~phaller/compilers/labs/lab7.html
