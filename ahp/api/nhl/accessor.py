import requests
from urllib.parse import urljoin

from ahp.api.nhl.constants import URL


class Accessor:
    def __init__(self):
        self._url = URL

    def get_awards(self, id_: int = None):
        url = urljoin(base=self._url, url="awards")
        if id_:
            url += "/{}".format(id_)
        response = self._get(url=url)
        return response.json()

    def get_conferences(self, id_: int = None):
        url = urljoin(base=self._url, url="conferences")
        if id_:
            url += "/{}".format(id_)
        response = self._get(url=url)
        return response.json()

    def get_divisions(self, id_: int = None):
        url = urljoin(base=self._url, url="divisions")
        if id_:
            url += "/{}".format(id_)
        response = self._get(url=url)
        return response.json()

    def get_draft(self, year: int = None):
        url = urljoin(base=self._url, url="draft")
        if year:
            url += "/{}".format(year)
        response = self._get(url=url)
        return response.json()

    def get_draft_prospects(self, id_: int = None):
        url = urljoin(base=self._url, url="draft/prospects")
        if id_:
            url += "/{}".format(id_)
        response = self._get(url=url)
        return response.json()

    def get_people(self, id_: int):
        url = urljoin(base=self._url, url="people/{}".format(id_))
        response = self._get(url=url)
        return response.json()

    def get_people_stats(self, id_: int):
        url = urljoin(base=self._url, url="people/{}/stats".format(id_))
        response = self._get(url=url)
        return response.json()

    def get_schedule(self):
        url = urljoin(base=self._url, url="schedule")
        response = self._get(url=url)
        return response.json()

    def get_standings(self):
        url = urljoin(base=self._url, url="standings")
        response = self._get(url=url)
        return response.json()

    def get_standings_types(self):
        url = urljoin(base=self._url, url="standingsTypes")
        response = self._get(url=url)
        return response.json()

    def get_stat_types(self):
        url = urljoin(base=self._url, url="statTypes")
        response = self._get(url=url)
        return response.json()

    def get_teams(self, id_: int = None):
        url = urljoin(base=self._url, url="teams")
        if id_:
            url += "/{}".format(id_)
        response = self._get(url=url)
        return response.json()

    def get_teams_roster(self, id_: int):
        url = urljoin(base=self._url, url="teams/{}/roster".format(id_))
        response = self._get(url=url)
        return response.json()

    def get_teams_stats(self, id_: int):
        url = urljoin(base=self._url, url="teams/{}/stats".format(id_))
        response = self._get(url=url)
        return response.json()

    @staticmethod
    def _get(url: str):
        response = requests.get(url)
        assert response
        return response
