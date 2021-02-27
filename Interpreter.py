# open input
fin = open('./input.txt', 'r')

# read lines
lines = fin.read().splitlines()

# close input
fin.close()

# open output
fout = open('./output.txt', 'w')

# interpret lines
for line in lines:
    words = line.split()
    command = words[0]
    # comment
    if command == '#':
        continue
    # print
    elif command == 'print':
        fout.write(' '.join(words[1:]))
    # unrecognized command
    else:
        fout.write('Command ' + command + ' not recognized')
    fout.write('\n')

# close output
fout.close()
