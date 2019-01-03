from random import *

def makeGroups():
    with open("players.txt", "r") as file:
        file = file.read()
        players = file.split("\n")

    nbPlayers = len(players)
    print(nbPlayers, "players")
    nbGroups = int(input("Number of groups: "))
    playersGroup = nbPlayers/nbGroups

    random = list(players)
    groups = []

    mod = nbPlayers % nbGroups
    for i in range(mod):
        groups.append(sample(random, int(playersGroup + 1)))
        for j in range(int(playersGroup + 1)):
            random.remove(groups[i][j])
    for i in range(mod, nbGroups):
        groups.append(sample(random, int(playersGroup)))
        for j in range(int(playersGroup)):
            random.remove(groups[i][j])
            
    return groups