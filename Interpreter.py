# open input
fin = open('./input.txt', 'r')

# read lines
lines = fin.read().splitlines()

# close input
fin.close()

# open output
fout = open('./output.txt', 'w')

commands = ['print']

# interpret lines
for line in lines:
    words = line.split()
    command = words[0]
    if command not in commands:
        fout.write('Command ' + command + ' not recognized')
    elif command == 'print':
        fout.write(' '.join(words[1:]))
    fout.write('\n')

# close output
fout.close()
