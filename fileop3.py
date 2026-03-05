file1 = open("file1.txt", 'r')
file2 = open("file2.txt", 'w')
for Line in file1.readlines():
    if not (Line.startswith("im")):
        print(Line)
        file2.write(Line)
file1.close()
file2.close()