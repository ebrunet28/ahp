import requests

from api.nhl.constants import URL


class Accessor:
    @classmethod
    def get_awards(cls, id_: int = None):
        url = URL + "awards"
        if id_:
            url += "/{}".format(id_)
        response = cls._get(url=url)
        return response.json()

    @classmethod
    def get_conferences(cls, id_: int = None):
        url = URL + "conferences"
        if id_:
            url += "/{}".format(id_)
        response = cls._get(url=url)
        return response.json()

    @classmethod
    def get_divisions(cls, id_: int = None):
        url = URL + "divisions"
        if id_:
            url += "/{}".format(id_)
        response = cls._get(url=url)
        return response.json()

    @classmethod
    def get_draft(cls, year: int = None):
        url = URL + "draft"
        if year:
            url += "/{}".format(year)
        response = cls._get(url=url)
        return response.json()

    @classmethod
    def get_draft_prospects(cls, id_: int = None):
        url = URL + "draft/prospects"
        if id_:
            url += "/{}".format(id_)
        response = cls._get(url=url)
        return response.json()

    @classmethod
    def get_people(cls, id_: int):
        url = URL + "people/{}".format(id_)
        response = cls._get(url=url)
        return response.json()

    @classmethod
    def get_people_stats(cls, id_: int):
        url = URL + "people/{}/stats".format(id_)
        response = cls._get(url=url)
        return response.json()


    @classmethod
    def get_schedule(cls):
        url = URL + "schedule"
        response = cls._get(url=url)
        return response.json()

    @classmethod
    def get_standings(cls):
        url = URL + "standings"
        response = cls._get(url=url)
        return response.json()

    @classmethod
    def get_standings_types(cls):
        url = URL + "standingsTypes"
        response = cls._get(url=url)
        return response.json()

    @classmethod
    def get_stat_types(cls):
        url = URL + "statTypes"
        response = cls._get(url=url)
        return response.json()

    @classmethod
    def get_teams(cls, id_: int = None):
        url = URL + "teams"
        if id_:
            url += "/{}".format(id_)
        response = cls._get(url=url)
        return response.json()

    @classmethod
    def get_teams_roster(cls, id_: int):
        url = URL + "teams/{}/roster".format(id_)
        response = cls._get(url=url)
        return response.json()

    @classmethod
    def get_teams_stats(cls, id_: int):
        url = URL + "teams/{}/stats".format(id_)
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

    accessor.get_awards()
    accessor.get_awards(id_=1)

    accessor.get_conferences()
    accessor.get_conferences(id_=1)

    accessor.get_divisions()
    accessor.get_divisions(id_=1)

    accessor.get_draft()
    accessor.get_draft(year=2019)
    accessor.get_draft_prospects()
    accessor.get_draft_prospects(id_=53727)

    # TODO game

    accessor.get_people(id_=8477474)
    # accessor.get_people_stats(id_=8477474)  # TODO probably to combine with modifiers

    accessor.get_schedule()

    accessor.get_standings()
    accessor.get_standings_types()

    accessor.get_stat_types()

    accessor.get_teams()
    accessor.get_teams(id_=1)
    accessor.get_teams_roster(id_=1)
    accessor.get_teams_stats(id_=1)
