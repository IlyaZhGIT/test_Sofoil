import unittest
from unittest.mock import Mock
from test4 import Soccer, MatchErrors


class TestSoccer(unittest.TestCase):

    def setUp(self):
        self.soccer = Soccer()

    def test_can_shoot_goal_not_player(self):
        person = Mock()
        match = Mock()
        with self.assertRaises(MatchErrors.CANT_SHOOT_GOAL_NOT_PLAYER):
            self.soccer.can_shoot_goal(person, match)

    def test_can_shoot_goal_match_not_started(self):
        person = Mock()
        person.is_referee = True
        match = Mock()
        match.status = match.BEFORE_START
        with self.assertRaises(MatchErrors.CANT_SHOOT_GOAL_MATCH_NOT_STARTED):
            self.soccer.can_shoot_goal(person, match)

    def test_can_shoot_goal_not_in_teams(self):
        person = Mock()
        person.is_referee = True
        match = Mock()
        match.status = match.STARTED
        match.first_team.players = [Mock()]
        match.second_team.players = [Mock()]
        with self.assertRaises(MatchErrors.CANT_SHOOT_GOAL_NOT_IN_TEAMS):
            self.soccer.can_shoot_goal(person, match)

    def test_can_start_match_not_referee(self):
        person = Mock()
        person.is_referee = False
        match = Mock()
        with self.assertRaises(MatchErrors.CANT_START_NOT_REFEREE):
            self.soccer.can_start_match(person, match)

    def test_can_start_match_already_started(self):
        person = Mock()
        person.is_referee = True
        match = Mock()
        match.status = match.STARTED
        with self.assertRaises(MatchErrors.CANT_START_ALREADY_STARTED):
            self.soccer.can_start_match(person, match)

    def test_can_start_match_not_even_teams(self):
        person = Mock()
        person.is_referee = True
        match = Mock()
        match.status = match.BEFORE_START
        match.first_team.players = [Mock()]
        match.second_team.players = [Mock(), Mock()]
        with self.assertRaises(MatchErrors.CANT_START_NOT_EVEN_TEAMS):
            self.soccer.can_start_match(person, match)

    # Add more test cases for other methods as needed


if __name__ == "__main__":
    unittest.main()


class TestSoccerMethods(unittest.TestCase):

    def test_can_shoot_goal_player_not_in_teams(self):
        # Arrange
        person = Mock()
        match = Mock()

        # Act & Assert
        with self.assertRaises(MatchErrors.CANT_SHOOT_GOAL_NOT_IN_TEAMS):
            Soccer.can_shoot_goal(person, match)

    def test_can_shoot_goal_match_not_started(self):
        # Arrange
        person = Mock()
        match = Mock()
        match.status = match.NOT_STARTED

        # Act & Assert
        with self.assertRaises(MatchErrors.CANT_SHOOT_GOAL_MATCH_NOT_STARTED):
            Soccer.can_shoot_goal(person, match)

    def test_can_shoot_goal_not_player(self):
        # Arrange
        person = "Not a player"
        match = Mock()
        match.status = match.STARTED

        # Act & Assert
        with self.assertRaises(MatchErrors.CANT_SHOOT_GOAL_NOT_PLAYER):
            Soccer.can_shoot_goal(person, match)

    def test_can_shoot_goal_valid_scenario(self):
        # Arrange
        person = Mock()
        match = Mock()
        match.status = match.STARTED
        match.first_team.players.append(person)

        # Act & Assert
        try:
            Soccer.can_shoot_goal(person, match)
        except Exception as e:
            self.fail("Unexpected exception: " + str(e))
