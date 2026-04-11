with open("students.txt", "a") as file:
    file.write("Ayra Haiman, Silat\n")

with open("students.txt", "r") as file:
    print(file.read())