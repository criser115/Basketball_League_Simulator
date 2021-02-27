# Basketball league

class Team:

    num_of_teams = 0

    def __init__(self, name, mascot, wins, loses):
        self.name = name
        self.mascot = mascot
        self.wins = wins
        self.loses = loses

        Team.num_of_teams += 1

    def fullname(self):
        return '{} {}'.format(self.name, self.mascot)

    def record(self):
        return '{} - {}'.format(self.wins, self.loses)


class Season:

    num_of_seasons = 0

    def __init__(self, champions=None):

        if champions is None:
            self.champions = []
        else:
            self.champions = champions

    def add_champ(self, champ):
        self.champions.append(champ)


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

print(team_1.fullname(), team_1.record())
print("There are {} teams in this league.".format(Team.num_of_teams))





