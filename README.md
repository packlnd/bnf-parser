# mini-compiler
:umbrella:

File extension: `.patrik`

## Example usage:
Use as an interpreter
`python file.patrik interpreter`

__To be implemented:__

Use LLVM backend
`python file.patrik llvm`

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
```python
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

__Output:__
```
1
3
```
### 2.
```python
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
