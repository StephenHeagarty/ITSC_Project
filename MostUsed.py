with open("Pokemon.csv", "r") as f:

    BigList = []
    counter = 0
    for line in f:
        if counter == 0:
            counter += 1
            continue
        SmallList = line.strip().split(",")
        BigList.append(SmallList)

    # The purpose of this function is to determine which pokemon spends the most time on the field
    def Most_Used_Pokemon(data: list[list[str]]) -> str:
        Dracula = 0
        Goat = ""
        LotsOfCounters = {}
        for (Pokemon1, Pokemon2, Move, Rating1, Rating2, ID) in data:
            LotsOfCounters[Pokemon1] = LotsOfCounters.get(Pokemon1, 0) + 1
            LotsOfCounters[Pokemon2] = LotsOfCounters.get(Pokemon2, 0) + 1
        for pokemon, count in LotsOfCounters.items():
            if count > Dracula:
                Dracula = count
                Goat = pokemon
        return Goat

    print(Most_Used_Pokemon(BigList))

