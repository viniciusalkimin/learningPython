with open("src/resources/newFile.txt", "r") as file:
    print(file)
    # content = file.read()
    # print(content)

    for line in file.readlines():
        print(line)

