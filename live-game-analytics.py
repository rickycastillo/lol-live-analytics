import requests

def requestSummonerData(region, summonerName, APIKey): 
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v1.4/summoner/by-name/" + summonerName + "?api_key=" + APIKey
    print "Getting Summoner Data..."
    response = requests.get(URL)
    return response.json()

def requestRankedData(region, ID, APIKey):
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v2.5/league/by-summoner/" + ID + "/entry?api_key=" + APIKey
    print "Getting Ranked Data..."
    response = requests.get(URL)
    return response.json()
    
def requestCurrentGame(region, ID, APIKey):
    URL = "https://" + region + ".api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/" + region + "1/" + ID + "?api_key=" + APIKey
    print "Getting Current Game Data..."
    response = requests.get(URL)
    return response.json()

def main():
    print "\nLive Game Analytics - Testing Environment\n\n"

    result = 50

    region = (str)(raw_input('Type in the region: '))
    region = region.lower()
    summonerName = (str)(raw_input('Type your Summoner Name here and DO NOT INCLUDE ANY SPACES: '))
    summonerName = summonerName.lower()
    APIKey = "RGAPI-330b0647-a6ac-468a-8a4b-7cf296abb08e"
    
    summonerData  = requestSummonerData(region, summonerName, APIKey)
    ID = summonerData[summonerName]['id']
    ID = str(ID)
    
    rankedData = requestRankedData(region, ID, APIKey)
    print rankedData[ID][0]['tier']
    print rankedData[ID][0]['entries'][0]['division']
    print rankedData[ID][0]['entries'][0]['leaguePoints']

    currentGame = requestCurrentGame(region, ID, APIKey)

    print currentGame

#This starts my program!
if __name__ == "__main__":
    main()

