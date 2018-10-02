import leagueoffreljord.riotConstants as Consts
import requests

class RiotAPI(object):

    def __init__(self, api_key, region=Consts.REGIONS['latin_america_south']):
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Consts.URL['base'].format(
                url=api_url
            ),
            params=args
            )
        return response.json()

    def get_summoner_by_name(self, name):
        api_url = Consts.URL['summoner_by_name'].format(
                summonerName=name
            )
        return self._request(api_url)

    def get_league_by_id(self, id):
        api_url = Consts.URL['league_by_id'].format(
                summonerId=id
        )
        return self._request(api_url)
