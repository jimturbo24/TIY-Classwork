# prisoners = { <ID>: {name: <name>, cell: <cell>, ...}}

prisoners = {}
prisonerID = "default"

while prisonerID:
    prisonerID = input("Enter prisoner ID: ")
    if prisonerID == "":
        continue

    name = input("Enter prisoner name: ")
    cell = input("Enter prisoner cell: ")

    prisoners[prisonerID] = {"name": name, "cell": cell}

    print(prisoners)
