new_file = open("file3.txt", 'x')
new_file.close()

import os
print("Checking file is exist or not")
if os.path.exists("file3.txt"):
    print("File exist")
else:
    print("File not exist")