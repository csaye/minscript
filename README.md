# min-script
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
- for
  - repeats given command
  - `for 3 print hi` -> `hi` `hi` `hi`
- varlist
  - defines length of variable list
  - `varlist 3`
- var
  - enables variable assignment
  - `varlist 1`
  - `var0 hello world`
  - `print var0` -> `hello world`
- if
  - executes given command if true
  - `varlist 1`
  - `var0 a`
  - `if var0 b print hello`
  - `if var0 a print world` -> `world`
- end
  - ends program
  - `varlist 1`
  - `var0 0`
  - `if var0 10 end`
  - `var0 +`
  - `goto 3`

## Examples

Hello World (prints "hello world"):
```
print hello world
```

Primes (prints all prime numbers up to 100):
```
varlist 2
var0 2
var1 2
if var1 var0 goto 8
if var0 % var1 0 goto 9
var1 +
goto 4
print var0
var0 +
if var0 > 100 end
goto 3

```

Fibonacci (prints all Fibonacci numbers up to 100):
```
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
goto 5
```

FizzBuzz (prints FizzBuzz up to 100):
```
varlist 1
var0 1
if var0 > 100 end
if var0 % 3 0 goto 8
if var0 % 5 0 goto 12
print var0
goto 13
printin Fizz
if var0 % 5 0 goto 12
print
goto 13
print Buzz
var0 +
goto 3
```
