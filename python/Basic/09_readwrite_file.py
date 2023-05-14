
# r = read only
# a = append/add on the old file
# r+ =
# w = write overall
read_file = open("README.md", "r")

print(read_file.readable())

# read all
# print(read_file.read())
# read one line
# print(read_file.readline())
# read all together one line into a array
# print(read_file.readlines())
# print(read_file.readlines()[0])

for line in read_file.readlines():
    print(line)
read_file.close()

write_file = open("out.txt", "w")

write_file.write("First line")
write_file.write("\nSecond line")
write_file.write("\nThird line")

write_file.close()