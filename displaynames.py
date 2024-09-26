infile = open('names.txt', 'r')
line = infile.readline()
number = 0

while line != "":
    print(line, end = "")
    number += 1
    line = infile.readline()

print("\nNumber of names: ", number)



infile.close()

"""def main():

   # Declare variables

   line = ''

   counter = 0

 

   # Open names.txt file for reading

   infile = open('names.txt', 'r')

 

   # Priming read

   line = infile.readline()

     

   # Read in until no more data

   while line != '':

       counter += 1

       line = infile.readline()

 

   # Close file

   infile.close()

 

   # Display the number of names in the file

   print (counter, 'names were read.')

 

# Call the main function.

main()"""