# mini-compiler
:umbrella:

## Grammar:

|               |   |                                                              |
|---------------|---|--------------------------------------------------------------|
| _Goal_        | = | _MainMehtod_                                                 |
| _MainMethod_  | = | __def__ __main__ __:__ __INDENT__ (_Statement_)* __DEDENT__  |
| _Statement_   | = | __print__ _Expression_                                       |
| _Expression_  | = | _Integer_ __+__ _Integer_                                    |
|               |   | _Integer_                                                    |
