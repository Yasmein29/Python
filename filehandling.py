with open("file1.txt", "w") as file:
    file.write("Hi")

file.close()

with open("file2.txt", "r") as file:
    data = file.readlines()
    print(data)
    for Line in data:
        wurd = Line.split()
        print(wurd)

file.close()