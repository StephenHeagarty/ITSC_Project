with open("Pokemon.csv", "r") as f:

    BigList = []
    counter = 0
    for line in f:
        if counter == 0:
            counter += 1
            continue
        SmallList = line.strip().split(",")
        BigList.append(SmallList)

    # The purpose of this function is to refactor similar logic to save myself some time
    def Most_Used_By(target: int, data: list[list[str]]) -> str:
        Nosferatu = 0
        Splash = ""
        LotsOfCounters = {}
        for fabric in data:
            LotsOfCounters[fabric[target]] = LotsOfCounters.get(fabric[target], 0) + 1
        for item, count in LotsOfCounters.items():
            if count > Nosferatu:
                Nosferatu = count
                Splash = item
        return Splash

    # The purpose of this function is to determine which pokemon does the most clicking of moves
    def Most_Active_Pokemon(data: list[list[str]]) -> str:
        target = 0
        return Most_Used_By(target, data)

    print(Most_Active_Pokemon(BigList))

    # The purpose of this function is titular
    def Most_Targeted_Pokemon(data: list[list[str]]) -> str:
        target = 1
        return Most_Used_By(target, data)

    print(Most_Targeted_Pokemon(BigList))

    # The purpose of this function is titular
    def Most_Used_Move(data: list[list[str]]) -> str:
        target = 2
        return Most_Used_By(target, data)

    print(Most_Used_Move(BigList))