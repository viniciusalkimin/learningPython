# file = open("src/resources/file.txt", "w")
#
# file.write("Hello World!")
#
# file.close()

with open("src/resources/newFile.txt", "a") as file:
    file.write("\nAppend of new line")