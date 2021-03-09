# open input
fin = open('./input.txt', 'r')

# read lines
lines = fin.read().splitlines()

# close input
fin.close()

# open output
fout = open('./output.txt', 'w')

# whether string is int
def is_int(string):
    try:
        int(string)
        return True
    except:
        return False

# process int
def prc_int(string):
    if string.startswith(var):
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
    # comment
    if command == '#':
        index += 1
    # print
    elif command == 'print':
        string = prc_str(' '.join(args))
        fout.write(string + '\n')
    # skip next line
    elif command == 'skip':
        index += 2
    # goto line
    elif command == 'goto':
        try:
            line = int(args[0])
            index = line - 2
        except:
            fout.write('! Invalid goto !')
    # for loop
    elif command == 'for':
        try:
            count = prc_int(args[0])
            for i in range(count):
                prc_com(args[1], args[2:])
        except:
            fout.write('! Invalid for loop !\n')
    # if statement
    elif command == 'if':
        try:
            a = prc_int(args[0])
            # operators
            if args[1] == '+':
                if a + prc_int(args[2]) == prc_int(args[3]):
                    process_command(args[4], args[5:])
            elif args[1] == '-':
                if a - prc_int(args[2]) == prc_int(args[3]):
                    process_command(args[4], args[5:])
            elif args[1] == '<':
                if a < prc_int(args[2]):
                    prc_com(args[3], args[4:])
            elif args[1] == '>':
                if a > prc_int(args[2]):
                    prc_com(args[3], args[4:])
            else:
                if a == prc_int(args[2]):
                    process_command(args[3], args[4:])
        except:
            fout.write('! Invalid if !\n')
    # variable
    elif command.startswith('var') and is_int(command[3:]):
        try:
            varidx = int(command[3:])
            # zero arg
            if len(args) < 1:
                varlist[varidx] = ''
            # one arg
            elif len(args) == 1:
                # int arg
                if is_int(args[0]):
                    varlist[varidx] = int(args[0])
                # var arg
                elif args[0].startswith('var'):
                    varlist[varidx] = prc_var(args[0])
                # str arg
                else:
                    varlist[varidx] = args[0]
            # add operator
            elif args[1] == '+':
                if len(args) > 2:
                    varlist[varidx] += prc_int(args[2])
                else:
                    varlist[varidx] += 1
            # sub operator
            elif args[1] == '-':
                if len(args) > 2:
                    varlist[varidx] -= prc_int(args[2])
                else:
                    varlist[varidx] -= 1
            # string var
            else:
                varlist[varidx] = ' '.join(args)
        except:
            fout.write('! Invalid var !\n')
    # variable list
    elif command == 'varlist':
        try:
            count = int(args[0])
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
while index < len(lines):
    words = lines[index].split()
    if len(words) < 1:
        index += 1
        continue
    command = words[0]
    prc_com(command, words[1:])
    index += 1

# close output
fout.close()
