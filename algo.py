from classes.dancer import Dancer
from classes.team import Team

class Program:
    def __init__(self):
        self.dancers = {}
        self.teams = {}
        self.rosters = {"unassigned": []}

    def add_dancer(self, name: str, prefs: list):
        dancer = Dancer(name, prefs=prefs)
        self.dancers[name] = dancer
    
    def add_team(self, name: str, prefs: list, max: int):
        team = Team(name, prefs=prefs, max=max)
        self.teams[name] = team
        self.rosters[name] = [] # name of dancers

    def try_assign(self, dancer: Dancer):
        while (not dancer.assigned):
            choice = dancer.highest_pref()
            team_pref = self.teams[choice]

            if choice == "unassigned":
                self.rosters[choice].append(dancer.name)
                dancer.assigned = True
                break

            dancer_rank = team_pref.prefs.index(dancer.name)
            if len(team_pref.roster) < team_pref.max_dancers:
                team_pref.roster.append([dancer_rank, dancer.name])
                team_pref.roster.sort(key=lambda dancer: dancer[0])
            else:
                if dancer_rank < team_pref[-1][0]:
                    bumped = team_pref.pop()[1]
                    team_pref.append([dancer_rank, dancer.name])
                    
                    self.dancers[bumped].assigned = False
                    bumped_dancer = self.try_assign(self.dancers[bumped])
            

    def run(self):
        for name, dancer in self.dancers.items():
            self.try_assign(dancer)