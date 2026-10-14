from MostUsedUtils import Most_Active_Pokemon, Most_Targeted_Pokemon, Most_Used_Move

with open("Pokemon.csv", "r") as f:

    BigList = []
    counter = 0
    for line in f:
        if counter == 0:
            counter += 1
            continue
        SmallList = line.strip().split(",")
        BigList.append(SmallList)

    print(Most_Active_Pokemon(BigList))
    print(Most_Targeted_Pokemon(BigList))
    print(Most_Used_Move(BigList))