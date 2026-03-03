file_read = open("abc.txt")
print("File is in read mode")
print(file_read.read())
file_read.close()

file_write = open("abc.txt", "w")
file_write.write("This is a new line")
file_write.write("\nThis is another line")
file_write.close()

file_append = open("abc.txt", "a")
file_append.write("\nThis line is added in append mode")
file_append.write("nThis line is also added in append mode")
file_append.close()