nameList = []
name = "none"
count = 10

print("Please enter ten names.")

while count:
    name = input("#" + str(count) + ": " )
    nameList.append(name)
    count -= 1

print(nameList)
