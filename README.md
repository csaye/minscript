# MinScript
A minimalist programming language written in Python.

## Commands

- \#
  - comment, skipped by interpreter
  - `# this is a comment`
- print
  - outputs rest of line
  - `print hello world` -> `hello world`
- printin
  - outputs rest of line with no newline
- skip
  - skips next line
  - `skip`
  - `print hello`
  - `print world` -> `world`
- goto
  - goes to given line
  - `print 1` -> `1`
  - `goto 5`
  - `print 3`
  - `print 4`
  - `print 5` -> `5`
- varlist
  - defines length of variable list
  - `varlist 3`
- var[index]
  - enables variable assignment
  - `varlist 1`
  - `var0 hello world`
  - `print var0` -> `hello world`
- if
  - executes given command if true
  - `varlist 1`
  - `var0 0`
  - `if var0 0 print hello` -> `hello`
  - `if var0 1 print world`
- end
  - ends program
  - `varlist 1`
  - `var0 0`
  - `if var0 10 end`
  - `var0 +`
  - `goto 3`

## Operators

- 2 operands
  - < (less than)
    - `if 1 < 2 print hello` -> `hello`
  - \> (greater than)
    - `if 2 > 1 print hello` -> `hello`

- 3 operands
  - \+ (addition)
    - `if 2 + 2 4 print hello` -> `hello`
  - \- (subtraction)
    - `if 5 - 2 3 print hello` -> `hello`
  - \* (multiplication)
    - `if 2 * 3 6 print hello` -> `hello`
  - / (true division)
    - `if 5 / 2 2.5 print hello` -> `hello`
  - ^ (power)
    - `if 2 ^ 3 8 print hello` -> `hello`
  - % (modulus)
    - `if 5 % 2 1 print hello` -> `hello`
  - // (floor division)
    - `if 5 // 2 2 print hello` -> `hello`

## Examples

```
# prints "hello world"
print hello world
```

```
# repeats until var0 is 10
varlist 1
var0 0
if var0 10 end
print var0
var0 +
goto 4
```

```
# prints decimal representation of var0
varlist 3
var0 1001101
var1 0
var2 1
if var0 0 goto 11
var1 + ((var0 % 10) * var2)
var2 * 2
var0 // 10
goto 6
print var1
```

```
# prints Fibonacci numbers up to 100
varlist 3
var0 0
var1 1
var2 0
if var2 > 100 end
var2 0
var2 + var0
var2 + var1
var0 var1
var1 var2
print var2
goto 6
```

```
# prints FizzBuzz up to 100
varlist 1
var0 1
if var0 > 100 end
if var0 % 3 0 goto 9
if var0 % 5 0 goto 13
print var0
goto 14
printin Fizz
if var0 % 5 0 goto 13
print
goto 14
print Buzz
var0 +
goto 4
```

More examples in [examples folder](examples).
