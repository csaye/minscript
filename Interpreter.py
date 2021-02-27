# open input
fin = open('./input.txt', 'r')

# read lines
lines = fin.read().splitlines()

# close input
fin.close()

# open output
fout = open('./output.txt', 'w')

index = 0
while index < len(lines):
    words = lines[index].split()
    command = words[0]
    # comment
    if command == '#':
        index += 1
        continue
    # print
    elif command == 'print':
        fout.write(' '.join(words[1:]))
    # skip next line
    elif command == 'skip':
        index += 2
        continue
    # unrecognized command
    else:
        fout.write('Command ' + command + ' not recognized')
    fout.write('\n')
    index += 1

# close output
fout.close()
