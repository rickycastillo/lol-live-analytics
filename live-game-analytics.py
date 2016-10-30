import requests

def requestSummonerData(region, summonerName, APIKey): 
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v1.4/summoner/by-name/" + summonerName + "?api_key=" + APIKey
    print "Getting Summoner ID..."
    response = requests.get(URL)
    return response.json()

def requestRankedData(region, sumID, APIKey):
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v2.5/league/by-summoner/" + sumID + "/entry?api_key=" + APIKey
    print "Getting Summoner Ranked Data..."
    response = requests.get(URL)
    return response.json()
    
def requestCurrentGameData(region, sumID, APIKey):
    URL = "https://" + region + ".api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/" + region + "1/" + sumID + "?api_key=" + APIKey
    print "Getting Current Game ID..."
    response = requests.get(URL)
    return response.json()

def requestGameData(region, matchID, APIKey):
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v2.2/match/" + matchID + "?api_key=" + APIKey
    print "Getting Game Data..."
    response = requests.get(URL)
    return response.json()

def main():
    print "\nLive Game Analytics - Testing Environment\n\n"

    # dynamyc variable changing through the algorithm
    result = 50

    # ask for server name and summoner name in order to analyze a match
    region = (str)(raw_input('Region (NA, EUW, etc.): '))
    region = region.lower()
    summonerName = (str)(raw_input('Summoner Name: '))
    summonerName = summonerName.lower()
    APIKey = "RGAPI-330b0647-a6ac-468a-8a4b-7cf296abb08e"

    # get summonerData to extract the summonerID
    summonerData  = requestSummonerData(region, summonerName, APIKey)
    sumID = summonerData[summonerName]['id']
    sumID = str(sumID)

    # print summoner information
    rankedData = requestRankedData(region, sumID, APIKey)
    print "\nSUMMONER DATA\n-------------"
    print "Tier: " + rankedData[sumID][0]['tier']
    print "Division: " + rankedData[sumID][0]['entries'][0]['division']
    print "Points: " + (str)(rankedData[sumID][0]['entries'][0]['leaguePoints'])
    print "\n"

    # get currentGame to extract the matchID
    currentGame = requestCurrentGameData(region, sumID, APIKey)

    print currentGame

    # store the matchID
    matchID = (str)(currentGame['gameId'])
    
    print "Match ID: " + matchID

    gameData = requestGameData(region, matchID, APIKey)

    print gameData

#This starts my program!
if __name__ == "__main__":
    main()

