import unittest
from unittest.mock import Mock

from test4 import Match, MatchErrors, Player, Soccer, Team


# class TestSoccerMock(unittest.TestCase):
#     def test_shoot_goal_player_increment_score(self):
#         mock_person = Mock()
#         mock_person.total_goals = 0

#         mock_first_team = Mock()
#         mock_first_team.players = [mock_person]
#         mock_first_team.goals = 0

#         mock_match = Match(mock_first_team, Mock())

#         mock_person.total_goals = 0
#         goals = mock_person.total_goals

#         Soccer.shoot_goal(mock_person, mock_match)
#         self.assertEqual(goals + 1, mock_person.total_goals)


class TestSoccer(unittest.TestCase):
    # def test_only_player_can_shoot_goal(self):
    #     person = "not person"
    #     first_team = Team()
    #     second_team = Team()
    #     match = Match(first_team, second_team)

    #     with self.assertRaises(MatchErrors.CANT_SHOOT_GOAL_NOT_PLAYER):
    #         Soccer.can_shoot_goal(person, match)

    def test_shoot_goal_player_increment_score(self):
        person = Player("Name")
        first_team = Team([person])
        second_team = Team()
        match = Match(first_team, second_team)

        goals = person.total_goals
        Soccer.shoot_goal(person, match)
        self.assertEqual(goals + 1, person.total_goals)

    def test_shoot_goal_first_team_increment_score(self):
        person = Player("Name")
        first_team = Team([person])
        second_team = Team()
        match = Match(first_team, second_team)

        goals = first_team.goals
        Soccer.shoot_goal(person, match)
        self.assertEqual(goals + 1, first_team.goals)

    def test_shoot_goal_second_team_increment_score(self):
        person = Player("Name")
        first_team = Team()
        second_team = Team([person])
        match = Match(first_team, second_team)

        goals = second_team.goals
        Soccer.shoot_goal(person, match)
        self.assertEqual(goals + 1, second_team.goals)

    def test_start_match_match_has_started(self):
        person = Player("Name")
        first_team = Team()
        second_team = Team()
        match = Match(first_team, second_team)

        Soccer.start_match(person, match)
        self.assertEqual(match.status, match.STARTED)

    def test_finish_match_match_has_finish(self):
        person = Player("Name")
        first_team = Team()
        second_team = Team()
        match = Match(first_team, second_team)

        Soccer.finish_match(person, match)
        self.assertEqual(match.status, match.FINISHED)

    def test_finish_match_distribution_winnings_draw(self):
        person = Player("Name")
        first_player = Player("Name")
        second_player = Player("Name")
        first_team = Team([first_player])
        second_team = Team([second_player])
        match = Match(first_team, second_team)

        first_team.goals = 0
        second_team.goals = 0
        player_reward = match.reward / 2
        referee_reward = int(match.reward / 2)

        Soccer.finish_match(person, match)
        self.assertEqual(first_player.cash, player_reward)
        self.assertEqual(second_player.cash, player_reward)
        self.assertEqual(person.cash, referee_reward)

    def test_finish_match_distribution_winnings_first_team_wins(self):
        person = Player("Name")
        first_team_player = Player("Name")
        second_team_player = Player("Name")
        first_team = Team([first_team_player])
        second_team = Team([second_team_player])
        match = Match(first_team, second_team)

        first_team.goals = 1
        second_team.goals = 0
        player_reward = match.reward
        referee_reward = int(match.reward / 2)

        Soccer.finish_match(person, match)
        self.assertEqual(first_team_player.cash, player_reward)
        self.assertEqual(second_team_player.cash, 0)
        self.assertEqual(person.cash, referee_reward)


if __name__ == "__main__":
    unittest.main()
