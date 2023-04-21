# open file located in same folder
file = open('test.txt')
# read the file and print it
# print(file.read())

# read specific characters or bytes
# print(file.read(3))

# read lines
# print(file.readline())
# print(file.readline())

# print each line in file

# line = file.readline()
# while line !="":
#     print(line)
#     line = file.readline()

# lines = file.readlines()
# for lines in file.readlines():
#     print(lines)


# file.close()

# opens files in read mode
with open('test.txt', 'r') as reader:
    #read the content of the file and store them as list
    content = reader.readlines()
    #opens file in write mode
    with open('test.txt', 'w') as writer:
        #reversed the list
        for lines in reversed(content):
            # write into file again
            writer.write(lines)
