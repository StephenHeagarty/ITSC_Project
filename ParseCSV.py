# Source - https://stackoverflow.com/a/3207973
# Posted by pycruft, modified by community. See post 'Timeline' for change history
# Retrieved 2026-10-13, License - CC BY-SA 4.0


from os import walk
import pandas as pd
import json

files = []
rows = []

for (dirpath, dirnames, filenames) in walk("AllTheFiles"):
    files.extend(filenames)
    break

counter = 0
for battle in files:
    # Open the file in read mode ('r')
    counter += 1
    print(counter)
    with open("AllTheFiles/" + battle, 'r') as file:
        # Load the JSON content into a Python variable
        data = json.load(file)
        PNames = {}
        ID = data["battle_id"]
        teams = data["team_revelation"]["teams"]
        turns = data["turns"]
        players = data["players"]
        rating_p1 = players["p1"]["ladder_rating_pre"]
        rating_p2 = players["p2"]["ladder_rating_pre"]
        for pokemon in teams["p1"]:
            PNames[pokemon["pokemon_uid"]] = pokemon["species"]
        for pokemon in teams["p2"]:
            PNames[pokemon["pokemon_uid"]] = pokemon["species"]
        for turn in turns:
            for event in turn["events"]:
                if event["type"] != "move":
                    continue
                if event["target_uid"] is None:
                    continue
                if event["pokemon_uid"] is None:
                    continue
                row = [PNames[event["pokemon_uid"]], PNames[event["target_uid"]], event["move_id"]]
                if event["player"] == "p1":
                    row.append(rating_p1)
                    row.append(rating_p2)
                else:
                    row.append(rating_p2)
                    row.append(rating_p1)
                row.append(ID)
                rows.append(row)

df = pd.DataFrame(rows, columns=['Pokemon_1','Pokemon_2','Move_Used','Rating_1','Rating_2', 'ID'])
df.to_csv("Pokemon.csv", index=False)