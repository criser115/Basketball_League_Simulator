import random
import operator
import pandas as pd

# Basketball league


class Team:
    num_of_teams = 0

    def __init__(self, name, mascot, wins, loses):
        self.name = name
        self.mascot = mascot
        self.wins = wins
        self.loses = loses
        self.score = 0

        Team.num_of_teams += 1

    def fullname(self):
        return '{} {}'.format(self.name, self.mascot)

    def record(self):
        return '{} - {}'.format(self.wins, self.loses)

    def add_win(self):
        self.wins = self.wins + 1

    def add_lose(self):
        self.loses = self.loses + 1


class Season:
    num_of_seasons = 0

    def __init__(self, schedule):

        self.schedule = schedule

    def play_game(self):
        for game in self.schedule:
            for team in game:
                team[0].score = random.randint(75, 120)
                team[1].score = random.randint(75, 120)
                if team[0].score > team[1].score:
                    team[0].add_win()
                    team[1].add_lose()
                    print('{} beat {} {} to {}'.format(team[0].fullname(), team[1].fullname(), team[0].score,
                                                       team[1].score))
                else:
                    team[1].add_win()
                    team[0].add_lose()
                    print('{} beat {} {} to {}'.format(team[1].fullname(), team[0].fullname(), team[1].score,
                                                       team[0].score))

    def playoffs(self, teams):

        self.teams = teams
        self.playoff_teams = sorted(teams, key=operator.attrgetter("loses"))

        while len(self.playoff_teams) > 4:
            self.playoff_teams.pop()

        self.playoff_teams[0].score = random.randint(75, 120)
        self.playoff_teams[3].score = random.randint(75, 120)

        self.playoff_teams[1].score = random.randint(75, 120)
        self.playoff_teams[2].score = random.randint(75, 120)

        if self.playoff_teams[0].score > self.playoff_teams[3].score and self.playoff_teams[1].score > \
            self.playoff_teams[2].score:
            print(
                f"{self.playoff_teams[0].fullname()} beat {self.playoff_teams[3].fullname()} {self.playoff_teams[0].score} to {self.playoff_teams[3].score}")
            print()
            print(
                f"{self.playoff_teams[1].fullname()} beat {self.playoff_teams[2].fullname()} {self.playoff_teams[1].score} to {self.playoff_teams[2].score}")
            print()

            self.playoff_teams[0].score = random.randint(75, 120)
            self.playoff_teams[1].score = random.randint(75, 120)

            if self.playoff_teams[0].score > self.playoff_teams[1].score:
                print(
                    f"{self.playoff_teams[0].fullname()} beat {self.playoff_teams[1].fullname()} {self.playoff_teams[0].score} to {self.playoff_teams[1].score}")
                print()
                print(f"{self.playoff_teams[0].fullname()} ARE THE CHAMPIONS!!!")
            else:
                print(
                    f"{self.playoff_teams[1].fullname()} beat {self.playoff_teams[0].fullname()} {self.playoff_teams[1].score} to {self.playoff_teams[0].score}")
                print()
                print(f"{self.playoff_teams[1].fullname()} ARE THE CHAMPIONS!!!")

        elif self.playoff_teams[0].score > self.playoff_teams[3].score and self.playoff_teams[2].score > \
            self.playoff_teams[1].score:
            print(
                f"{self.playoff_teams[0].fullname()} beat {self.playoff_teams[3].fullname()} {self.playoff_teams[0].score} to {self.playoff_teams[3].score}")
            print()
            print(
                f"{self.playoff_teams[2].fullname()} beat {self.playoff_teams[1].fullname()} {self.playoff_teams[2].score} to {self.playoff_teams[1].score}")
            print()

            self.playoff_teams[0].score = random.randint(75, 120)
            self.playoff_teams[2].score = random.randint(75, 120)

            if self.playoff_teams[0].score > self.playoff_teams[2].score:
                print(
                    f"{self.playoff_teams[0].fullname()} beat {self.playoff_teams[2].fullname()} {self.playoff_teams[0].score} to {self.playoff_teams[2].score}")
                print()
                print(f"{self.playoff_teams[0].fullname()} ARE THE CHAMPIONS!!!")
            else:
                print(
                    f"{self.playoff_teams[2].fullname()} beat {self.playoff_teams[0].fullname()} {self.playoff_teams[2].score} to {self.playoff_teams[0].score}")
                print()
                print(f"{self.playoff_teams[2].fullname()} ARE THE CHAMPIONS!!!")

        elif self.playoff_teams[3].score > self.playoff_teams[0].score and self.playoff_teams[1].score > \
            self.playoff_teams[2].score:
            print(
                f"{self.playoff_teams[3].fullname()} beat {self.playoff_teams[0].fullname()} {self.playoff_teams[3].score} to {self.playoff_teams[0].score}")
            print()
            print(
                f"{self.playoff_teams[1].fullname()} beat {self.playoff_teams[2].fullname()} {self.playoff_teams[1].score} to {self.playoff_teams[2].score}")
            print()

            self.playoff_teams[3].score = random.randint(75, 120)
            self.playoff_teams[1].score = random.randint(75, 120)

            if self.playoff_teams[3].score > self.playoff_teams[1].score:
                print(
                    f"{self.playoff_teams[3].fullname()} beat {self.playoff_teams[1].fullname()} {self.playoff_teams[3].score} to {self.playoff_teams[1].score}")
                print()
                print(f"{self.playoff_teams[3].fullname()} ARE THE CHAMPIONS!!!")
            else:
                print(
                    f"{self.playoff_teams[1].fullname()} beat {self.playoff_teams[3].fullname()} {self.playoff_teams[1].score} to {self.playoff_teams[3].score}")
                print()
                print(f"{self.playoff_teams[1].fullname()} ARE THE CHAMPIONS!!!")

        else:
            print(
                f"{self.playoff_teams[3].fullname()} beat {self.playoff_teams[0].fullname()} {self.playoff_teams[3].score} to {self.playoff_teams[0].score}")
            print()
            print(
                f"{self.playoff_teams[2].fullname()} beat {self.playoff_teams[1].fullname()} {self.playoff_teams[2].score} to {self.playoff_teams[1].score}")
            print()

            self.playoff_teams[3].score = random.randint(75, 120)
            self.playoff_teams[2].score = random.randint(75, 120)

            if self.playoff_teams[3].score > self.playoff_teams[2].score:
                print(
                    f"{self.playoff_teams[3].fullname()} beat {self.playoff_teams[2].fullname()} {self.playoff_teams[3].score} to {self.playoff_teams[2].score}")
                print()
                print(f"{self.playoff_teams[3].fullname()} ARE THE CHAMPIONS!!!")
            else:
                print(
                    f"{self.playoff_teams[2].fullname()} beat {self.playoff_teams[3].fullname()} {self.playoff_teams[2].score} to {self.playoff_teams[3].score}")
                print()
                print(f"{self.playoff_teams[2].fullname()} ARE THE CHAMPIONS!!!")


class Schedule:

    def __init__(self):
        self.games = []
        # self.create_balanced_round_robin()

    def create_balanced_round_robin(self, players):
        """ Create a schedule for the players in the list and return it"""
        self.games = []
        if len(players) % 2 == 1: players = players + [None]
        # manipulate map (array of indexes for list) instead of list itself
        # this takes advantage of even/odd indexes to determine home vs. away
        n = len(players)
        map = list(range(n))
        mid = n // 2
        for i in range(n - 1):
            l1 = map[:mid]
            l2 = map[mid:]
            l2.reverse()
            round = []
            for j in range(mid):
                t1 = players[l1[j]]
                t2 = players[l2[j]]
                if j == 0 and i % 2 == 1:
                    # flip the first match only, every other round
                    # (this is because the first match always involves the last player in the list)
                    round.append((t2, t1))
                else:
                    round.append((t1, t2))
            self.games.append(round)
            # rotate list by n/2, leaving last element at the end
            map = map[mid:-1] + map[:mid] + map[-1:]
        return self.games

    def show_schedule(self):
        print("\n".join(['{} vs. {}'.format(m[0], m[1]) for round in self.games for m in round]))


team_1 = Team("Dulles", "Vikings", 0, 0)
team_2 = Team('Travis', 'Tigers', 0, 0)
team_3 = Team('Austin', 'Bulldogs', 0, 0)
team_4 = Team('Bush', 'Broncos', 0, 0)
team_5 = Team('Clements', 'Rangers', 0, 0)
team_6 = Team('Kempner', 'Cougars', 0, 0)
team_7 = Team('Willowridge', 'Eagles', 0, 0)
team_8 = Team('Hightower', 'Hurricanes', 0, 0)
team_9 = Team('Marshall', 'Buffs', 0, 0)
team_10 = Team('Elkins', 'Knights', 0, 0)


teams = [team_1, team_2, team_3, team_4, team_5, team_6, team_7, team_8, team_9, team_10]
schedule_1 = Schedule()
schedule_1.create_balanced_round_robin(teams)

new_season = Season(schedule_1.games)

new_season.play_game()
print()

standings_df = pd.DataFrame(
    [[team_1.fullname(), team_1.wins, team_1.loses],
     [team_2.fullname(), team_2.wins, team_2.loses],
     [team_3.fullname(), team_3.wins, team_3.loses],
     [team_4.fullname(), team_4.wins, team_4.loses],
     [team_5.fullname(), team_5.wins, team_5.loses],
     [team_6.fullname(), team_6.wins, team_6.loses],
     [team_7.fullname(), team_7.wins, team_7.loses],
     [team_8.fullname(), team_8.wins, team_8.loses],
     [team_9.fullname(), team_9.wins, team_9.loses],
     [team_10.fullname(), team_10.wins, team_10.loses]],
    columns=['Teams', 'Wins', 'Loses']
)

print(standings_df.sort_values('Wins', ascending=False, ignore_index=True))

print()

new_season.playoffs(teams)
