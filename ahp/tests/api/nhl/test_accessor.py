import unittest
from unittest.mock import Mock, patch

from ahp.api.nhl.accessor import Accessor

# TODO find a way to share patch between methods (maybe through setUp)


class TestAccessor(unittest.TestCase):
    def setUp(self) -> None:
        self._accessor = Accessor()

        # TODO save json files from real api and link here, adapt for optional parameters
        self._awards = [{"awards": 1}]
        self._conferences = [{"conferences": 1}]
        self._divisions = [{"divisions": 1}]
        self._draft = [{"draft": 1}]
        self._draft_prospects = [{"draft_prospects": 1}]
        self._people = [{"people": 1}]
        self._people_stats = [{"people_stats": 1}]
        self._schedule = [{"schedule": 1}]
        self._standings = [{"standings": 1}]
        self._standings_types = [{"standings_types": 1}]
        self._stat_types = [{"stat_types": 1}]
        self._teams = [{"teams": 1}]
        self._teams_roster = [{"teams_roster": 1}]
        self._teams_stats = [{"teams_stats": 1}]

    @patch("requests.get")
    def test_get_awards(self, mock):

        mock.return_value.json.return_value = self._awards

        response = self._accessor.get_awards()

        self.assertListEqual(response, self._awards)

        response = self._accessor.get_awards(id_=1)

        self.assertListEqual(response, self._awards)

    @patch("requests.get")
    def test_get_conferences(self, mock):

        mock.return_value.json.return_value = self._conferences

        response = self._accessor.get_conferences()

        self.assertListEqual(response, self._conferences)

        response = self._accessor.get_conferences(id_=1)

        self.assertListEqual(response, self._conferences)

    @patch("requests.get")
    def test_get_divisions(self, mock):
        mock.return_value.json.return_value = self._divisions

        response = self._accessor.get_divisions()

        self.assertListEqual(response, self._divisions)

        response = self._accessor.get_divisions(id_=1)

        self.assertListEqual(response, self._divisions)

    @patch("requests.get")
    def test_get_draft(self, mock):
        mock.return_value.json.return_value = self._draft

        response = self._accessor.get_draft()

        self.assertListEqual(response, self._draft)

        response = self._accessor.get_draft(year=1899)

        self.assertListEqual(response, self._draft)

    @patch("requests.get")
    def test_get_draft_prospects(self, mock):
        mock.return_value.json.return_value = self._draft_prospects

        response = self._accessor.get_draft_prospects()

        self.assertListEqual(response, self._draft_prospects)

        response = self._accessor.get_draft_prospects(id_=1)

        self.assertListEqual(response, self._draft_prospects)

    @patch("requests.get")
    def test_get_people(self, mock):
        mock.return_value.json.return_value = self._people

        response = self._accessor.get_people(id_=1)

        self.assertListEqual(response, self._people)

    @patch("requests.get")
    def test_get_people_stats(self, mock):
        mock.return_value.json.return_value = self._people_stats

        response = self._accessor.get_people_stats(id_=1)

        self.assertListEqual(response, self._people_stats)

    @patch("requests.get")
    def test_get_schedule(self, mock):
        mock.return_value.json.return_value = self._schedule

        response = self._accessor.get_schedule()

        self.assertListEqual(response, self._schedule)

    @patch("requests.get")
    def test_get_standings(self, mock):
        mock.return_value.json.return_value = self._standings

        response = self._accessor.get_standings()

        self.assertListEqual(response, self._standings)

    @patch("requests.get")
    def test_get_standings_types(self, mock):
        mock.return_value.json.return_value = self._standings_types

        response = self._accessor.get_standings_types()

        self.assertListEqual(response, self._standings_types)

    @patch("requests.get")
    def test_get_stat_types(self, mock):
        mock.return_value.json.return_value = self._stat_types

        response = self._accessor.get_stat_types()

        self.assertListEqual(response, self._stat_types)

    @patch("requests.get")
    def test_get_teams(self, mock):
        mock.return_value.json.return_value = self._teams

        response = self._accessor.get_teams()

        self.assertListEqual(response, self._teams)

        response = self._accessor.get_teams(id_=1)

        self.assertListEqual(response, self._teams)

    @patch("requests.get")
    def test_get_teams_roster(self, mock):
        mock.return_value.json.return_value = self._teams_roster

        response = self._accessor.get_teams_roster(id_=1)

        self.assertListEqual(response, self._teams_roster)

    @patch("requests.get")
    def test_get_teams_stats(self, mock):
        mock.return_value.json.return_value = self._teams_stats

        response = self._accessor.get_teams_stats(id_=1)

        self.assertListEqual(response, self._teams_stats)
