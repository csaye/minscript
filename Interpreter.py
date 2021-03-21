# operators
import operator
ops2 = ['<', '>']
ops3 = ['+', '-', '*', '/', '^', '%', '//']
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '%': operator.mod,
    '//': operator.floordiv,
    '<': operator.lt,
    '>': operator.gt
}

# open input
fin = open('./input.mins', 'r')

# read lines
lines = fin.read().splitlines()

# close input
fin.close()

# open output
fout = open('./output.txt', 'w')

# splits a string with parentheses
def split(string):
    words = []
    word = ''
    open_par = 0
    i = 0
    # for each char in string
    for i in range(len(string)):
        ch = string[i]
        # if comment
        if ch == '#':
            # close word and return
            if len(word) > 0: words.append(word)
            return words
        # parse parentheses
        elif ch == '(':
            open_par += 1
        elif ch == ')':
            open_par -= 1
        # if space and no open parentheses
        if ch.isspace() and open_par <= 0:
            # close word and reset
            if len(word) > 0: words.append(word)
            word = ''
        else:
            word += ch
        # if end of string
        if i == len(string) - 1:
            # close word
            if len(word) > 0: words.append(word)
    return words

# whether string is int
def is_int(string):
    try:
        int(string)
        return True
    except:
        return False

# process int
def prc_int(string):
    # parentheses
    if string.startswith('('):
        # cut parentheses
        i = len(string) - 1
        string = string[1:i]
        words = split(string)
        # process vars and modifier
        v_a = prc_int(words[0])
        mod = words[1]
        v_b = prc_int(words[2])
        return ops[mod](v_a, v_b)
    # var
    elif string.startswith('var'):
        varidx = int(string[3:])
        return varlist[varidx]
    else:
        return int(string)

# process string
def prc_str(string):
    if string.startswith('var'):
        varidx = int(string[3:])
        return str(varlist[varidx])
    else:
        return string

# process var
def prc_var(string):
    varidx = int(string[3:])
    return varlist[varidx]

# process command
def prc_com(command, args):
    global index, varlist, lines
    # print
    if command == 'print':
        try:
            string = prc_str(' '.join(args))
            fout.write(string + '\n')
        except:
            fout.write('! Invalid print !')
    # print inline
    elif command == 'printin':
        try:
            string = prc_str(' '.join(args))
            fout.write(string)
        except:
            fout.write('! Invalid printin !')
    # skip next line
    elif command == 'skip':
        try:
            if len(args) > 0:
                count = prc_int(args[0])
                index += count
            else:
                index += 1
        except:
            fout.write('! Invalid skip !')
    # goto line
    elif command == 'goto':
        try:
            line = prc_int(args[0])
            index = line - 2
        except:
            fout.write('! Invalid goto !')
    # if statement
    elif command == 'if':
        try:
            # get value and modifier
            v_a = prc_int(args[0])
            mod = args[1]
            # 2 arg operation
            if mod in ops2:
                v_b = prc_int(args[2])
                if ops[mod](v_a, v_b):
                    prc_com(args[3], args[4:])
            # 3 arg operation
            elif mod in ops3:
                v_b = prc_int(args[2])
                v_c = prc_int(args[3])
                if ops[mod](v_a, v_b) == v_c:
                    prc_com(args[4], args[5:])
            # single arg comparison
            else:
                if v_a == prc_int(mod):
                    prc_com(args[2], args[3:])
        except:
            fout.write('! Invalid if !\n')
    # variable
    elif command.startswith('var') and is_int(command[3:]):
        try:
            varidx = int(command[3:])
            # zero arg
            if len(args) < 1:
                varlist[varidx] = ''
                return
            # get value and modifier
            v_a = varlist[varidx]
            mod = args[0]
            # if operator
            if mod in ops3:
                if len(args) < 2:
                    varlist[varidx] = ops[mod](v_a, 1)
                else:
                    v_b = prc_int(args[1])
                    varlist[varidx] = ops[mod](v_a, v_b)
            # int arg
            elif is_int(mod):
                varlist[varidx] = int(mod)
            # var arg
            elif mod.startswith('var'):
                varlist[varidx] = prc_var(mod)
            # str arg
            else:
                varlist[varidx] = ' '.join(args)
        except:
            fout.write('! Invalid var !\n')
    # variable list
    elif command == 'varlist':
        try:
            count = prc_int(args[0])
            while len(varlist) < count:
                varlist.append('')
        except:
            fout.write('! Invalid varlist !\n')
    # end program
    elif command == 'end':
        index = len(lines)
    # unrecognized command
    else:
        fout.write('! Command ' + command + ' not recognized !\n')

varlist = []
index = 0
# go through all lines
while index < len(lines):
    words = split(lines[index])
    # if no words in line, continue
    if len(words) == 0:
        index += 1
        continue
    command = words[0]
    prc_com(command, words[1:])
    index += 1

# close output
fout.close()
