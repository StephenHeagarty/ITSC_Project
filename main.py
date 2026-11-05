from MostUsedUtils import Most_Active_Pokemon, Most_Targeted_Pokemon, Most_Used_Move
from ParseCSV import makeCSV, prepare_data, checkCSV
from TargetedData import make_dict, get_movesets, find_moveset, find_mostused_move

#Check for CSV
if not checkCSV():
    # Create the CSV from list of JSONs
    makeCSV(prepare_data())

with open("Pokemon.csv", "r") as f:

    BigList = []
    counter = 0
    for line in f:
        if counter == 0:
            counter += 1
            continue
        SmallList = line.strip().split(",")
        BigList.append(SmallList)

    movesets = get_movesets(BigList)

    # Find the target statistics
    print(Most_Active_Pokemon(BigList))
    print(Most_Targeted_Pokemon(BigList))
    print(Most_Used_Move(BigList))

    # Find a pokemon's moveset
    print(find_moveset("Weavile", movesets))

    # Sort a pokemon's moveset
    print(find_mostused_move("Volbeat", movesets))

    # Find the most active pokemon quickly
    print(sorted(make_dict(BigList), key = lambda v: v['used_move'], reverse = True))

    # Find the least active pokemon quickly
    print(sorted(make_dict(BigList), key=lambda v: v['used_move'], reverse=False))