"""
Написать набор юнит тестов к данному классу
"""


class MatchErrors:
    class CantShootGoalNotPlayer(Exception):
        pass

    class CantShootGoalMatchNotStarted(Exception):
        pass

    class CantShootGoalNotInTeams(Exception):
        pass

    class CantStartNotReferee(Exception):
        pass

    class CantStartAlreadyStarted(Exception):
        pass

    class CantStartNotEvenTeams(Exception):
        pass

    class CantFinishNotReferee(Exception):
        pass

    CANT_SHOOT_GOAL_NOT_PLAYER = CantShootGoalNotPlayer
    CANT_SHOOT_GOAL_MATCH_NOT_STARTED = CantShootGoalMatchNotStarted
    CANT_SHOOT_GOAL_NOT_IN_TEAMS = CantShootGoalNotInTeams
    CANT_START_NOT_REFEREE = CantStartNotReferee
    CANT_START_ALREADY_STARTED = CantStartAlreadyStarted
    CANT_START_NOT_EVEN_TEAMS = CantStartNotEvenTeams
    CANT_FINISH_NOT_REFEREE = CantFinishNotReferee


class Player:
    def __init__(self, name: str, is_referee: bool = False) -> None:
        self.name = name
        self.is_referee = is_referee
        self.total_goals = 0
        self.cash = 0


class Team:
    def __init__(self, players: list[Player] = None) -> None:
        if players is None:
            players = []

        self.players = players
        self.goals = 0


class Match:
    BEFORE_START = 0
    STARTED = 1
    FINISHED = 2

    def __init__(self, first_team: Team, second_team: Team) -> None:
        self.first_team = first_team
        self.second_team = second_team
        self.status = self.BEFORE_START
        self.winner = None
        self.reward = 1_000_000


class Soccer:
    def can_shoot_goal(person, match):
        if not isinstance(person, Player):
            raise MatchErrors.CANT_SHOOT_GOAL_NOT_PLAYER
        if not match.status == match.STARTED:
            raise MatchErrors.CANT_SHOOT_GOAL_MATCH_NOT_STARTED
        if person not in match.first_team.players + match.second_team.players:
            raise MatchErrors.CANT_SHOOT_GOAL_NOT_IN_TEAMS

    def can_start_match(person, match):
        if not person.is_referee:
            raise MatchErrors.CANT_START_NOT_REFEREE
        if match.status != match.BEFORE_START:
            raise MatchErrors.CANT_START_ALREADY_STARTED
        if len(match.first_team.players) != len(match.second_team.players):
            raise MatchErrors.CANT_START_NOT_EVEN_TEAMS

    def can_finish_match(person, match):
        if match.status != match.STARTED:
            raise MatchErrors.CANT_FINISH_NOT_STARTED
        if not person.is_referee:
            raise MatchErrors.CANT_FINISH_NOT_REFEREE

    def shoot_goal(person, match):
        person.total_goals += 1
        if person in match.first_team.players:
            match.first_team.goals += 1
        else:
            match.second_team.goals += 1
        print("Goal was shoot by {}!".format(person.name))

    def start_match(person, match):
        match.status = match.STARTED
        # side effect, like sending emails, logging etc should live here
        print("{} started match!".format(person.name))

    def finish_match(person, match):
        """
        A bit more complicated function calculating rewards
        """
        match.status = match.FINISHED
        print("{} finished match!\n".format(person.name))
        first_score = match.first_team.goals
        second_score = match.second_team.goals
        if first_score == second_score:
            first_team_reward = match.reward / 2
            second_team_reward = match.reward / 2
        else:
            first_team_won = first_score > second_score
            first_team_reward = match.reward if first_team_won else 0
            second_team_reward = match.reward if not first_team_won else 0
            match.winner = match.first_team if first_team_won else match.second_team

        for player in match.first_team.players:
            player.cash += first_team_reward
            print(
                "{:24} - first team player  - earned {} cash!".format(
                    player.name, first_team_reward
                )
            )

        for player in match.second_team.players:
            player.cash += second_team_reward
            print(
                "{:24} - second team player - earned {} cash!".format(
                    player.name, second_team_reward
                )
            )

        referee_salary = int(0.5 * match.reward)
        person.cash += referee_salary
        print(
            "{:24} - referee            - earned {} cash as salary".format(
                person.name, referee_salary
            )
        )


# person = "not person"
# first_team = Team()
# second_team = Team()
# match = Match(first_team, second_team)

# Soccer.can_shoot_goal(person, match)
