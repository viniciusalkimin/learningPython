dataSet = []
num: int = 1
with open("C:/PythonWorkspace/learningPython/fileManipulation/src/resources/iris.data", "r") as file:
    lines = file.readlines()
    for line in lines:
        unitData = line.split(",")
        var = {num: [unitData[0], unitData[1], unitData[2], unitData[3], unitData[4]]}
        num +=1
        dataSet.append(var)

print(dataSet)