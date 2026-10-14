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

# The purpose of this function is titular
def Most_Targeted_Pokemon(data: list[list[str]]) -> str:
    target = 1
    return Most_Used_By(target, data)

# The purpose of this function is titular
def Most_Used_Move(data: list[list[str]]) -> str:
    target = 2
    return Most_Used_By(target, data)