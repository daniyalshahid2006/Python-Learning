with open("practice.txt","w") as file:
    file.write("python\n")
    file.write("python is cool\n")
    file.write("I love python")
with open("practice.txt","r") as file:
    print(file.read())
    file.seek(0)
    line = (file.readlines())
    print(line[1])
    file.seek(0)
    file.readline()
    print(file.readline())
line = []
with open("practice.txt","r") as file:
    line = file.read()
    print(line)
