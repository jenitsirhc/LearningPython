#infile = open('input.txt', 'r')
#line = infile.readline()

#while line != "":
#    print(line, end ="")
#    line = infile.readline()

# ----------------------------------------------------------
#

#outfile = open('output.txt', 'a')   #a for append
#outfile.write('Welcome to HAU\n')
#outfile.close()
#infile = open('output.txt', 'r')

#for line in infile:
#    print(line, end='')
#infile.close()

# ----------------------------------------------------------
#

infile = open('numbersInput.txt', 'r')
outfile = open('numbersOutput.txt', 'w')

line = infile.readline()      # line = '32.0'
total = 0
ctr = 0
while line != '':
    value = float(line)       # value = 32.0, 54.0
    outfile.write('%15.2f\n' % value)
    total += value            # total = 32.0
    ctr += 1                  # ctr = 1
    line = infile.readline()  # line = '54.0'

outfile.write('%15s\n' % '-----------')
outfile.write('Total: %8.2f\n' % total)
avg = total / ctr
outfile.write('Average: %6.2f\n' % avg)

infile.close()
outfile.close()