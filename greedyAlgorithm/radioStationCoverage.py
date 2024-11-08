stations = {}
stations["k1"] = set(["ID", "NV", "UT"])
stations["k2"] = set(["WA", "ID", "MT"])
stations["k3"] = set(["OR", "NV", "CA"])
stations["k4"] = set(["NV", "UT"])
stations["k5"] = set(["CA", "AZ"])

coveraged = set()
statesToCover = set(["MT", "WA", "OR", "ID", "NV", "UT", "CA", "AZ"])
finalStations = set()

def coverManyStateAsPossible(stations, statesToCover):
    finalStations = set()
    while statesToCover:
        bestStation = None
        statesCovered = set()
        for station, statesForStation in stations.items():
            coveraged = statesToCover & statesForStation
            if len(coveraged) > len(statesCovered) and station not in finalStations:
                bestStation = station
                statesCovered = coveraged
        if bestStation is not None:
            statesToCover -= statesCovered
            finalStations.add(bestStation)
            stations.pop(bestStation)
        else:
            return None
    return finalStations

print(coverManyStateAsPossible(stations, statesToCover))
