option = input("Choosen the option\n" +
                  "<I> - Insert User:\n"+
                  "<Q> - Quit: ").upper()
users = {}
while option != "Q":
    username = input("What is the username: ")
    name = input("What is the name: ")
    age = input("Whats is the age: ")
    users[username] = [name, age]

    option = input("Choose the option\n" +
                   "<I> - Insert User: \n" +
                   "<Q> - Quit: ").upper()

with open("src/resources/users.csv", "w") as file:
    file.write("username" + ";" + "name" + ";" + "age\n")
    for key, value in users.items():
        file.write(key + ";" + value[0] + ";" + value[1] + "\n")
