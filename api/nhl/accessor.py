import requests


class Accessor:
    @classmethod
    def get_teams(cls, id_: int = None):
        url = "https://statsapi.web.nhl.com/api/v1/teams"
        if id_:
            url += "/{}".format(id_)
        response = cls._get(url=url)
        return response.json()

    @classmethod
    def get_roster(cls, id_: int):
        url = "https://statsapi.web.nhl.com/api/v1/teams/{}/roster".format(id_)
        response = cls._get(url=url)
        return response.json()

    @classmethod
    def get_conferences(cls, id_: int = None):
        url = "https://statsapi.web.nhl.com/api/v1/conferences"
        if id_:
            url += "/{}".format(id_)
        response = cls._get(url=url)
        return response.json()

    @classmethod
    def get_divisions(cls, id_: int = None):
        url = "https://statsapi.web.nhl.com/api/v1/divisions"
        if id_:
            url += "/{}".format(id_)
        response = cls._get(url=url)
        return response.json()

    @classmethod
    def get_people(cls, id_: int):
        url = "https://statsapi.web.nhl.com/api/v1/people/{}".format(id_)
        response = cls._get(url=url)
        return response.json()

    @classmethod
    def get_stats(cls, id_: int):
        url = "https://statsapi.web.nhl.com/api/v1/people/{}/stats".format(id_)
        response = cls._get(url=url)
        return response.json()

    @classmethod
    def get_standings(cls):
        url = "https://statsapi.web.nhl.com/api/v1/standings"
        response = cls._get(url=url)
        return response.json()

    @classmethod
    def get_standings_types(cls):
        url = "https://statsapi.web.nhl.com/api/v1/standingsTypes"
        response = cls._get(url=url)
        return response.json()

    @classmethod
    def get_stat_types(cls):
        url = "https://statsapi.web.nhl.com/api/v1/statTypes"
        response = cls._get(url=url)
        return response.json()

    @staticmethod
    def _get(url: str):
        response = requests.get(url)
        assert response
        return response

    @staticmethod
    def _get_status_code(response: requests.Response):
        return response.status_code

    @staticmethod
    def _get_content(response: requests.Response):
        return response.content

    @staticmethod
    def _get_text(response: requests.Response):
        return response.text


if __name__ == "__main__":

    accessor = Accessor()

    accessor.get_teams()
    accessor.get_teams(id_=1)

    accessor.get_roster(id_=1)

    accessor.get_divisions()
    accessor.get_divisions(id_=1)

    accessor.get_people(id_=8477474)
    # accessor.get_stats(id_=8477474)

    accessor.get_standings()
    accessor.get_standings_types()

    accessor.get_stat_types()
