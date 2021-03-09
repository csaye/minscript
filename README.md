# python-clone
A python clone written in python.

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
