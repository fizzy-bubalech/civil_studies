import json


with open("parties.txt", "r") as fp:
    parties = json.load(fp)

for i in range(len(parties)):
    parties[i] = "".join([ord(c) for c in parties[i]] )

print(parties)