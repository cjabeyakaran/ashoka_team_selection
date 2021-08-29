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
        team = Team(name, prefs=prefs, max_dancers=max)
        self.teams[name] = team
        self.rosters[name] = [] # name of dancers

    def try_assign(self, dancer: Dancer):
        while (not dancer.assigned):
            choice = dancer.highest_pref()

            if choice == "unassigned":
                self.rosters[choice].append(dancer.name)
                dancer.assigned = True
                print(dancer.name + " out of teams. Unassigned :(")
                break

            preffed_team = self.teams[choice]
             
            if dancer.name in preffed_team.prefs:
                dancer_rank = preffed_team.prefs.index(dancer.name)
            else: 
                print(dancer.name + " not ranked by team " + preffed_team.name)
                continue

            if len(preffed_team.roster) < preffed_team.max_dancers:
                preffed_team.roster.append([dancer_rank, dancer.name])
                preffed_team.roster.sort(key=lambda dancer: dancer[0])
                dancer.assigned = True
                print(dancer.name + " added to team " + preffed_team.name)
            else:
                if dancer_rank < preffed_team.roster[-1][0]:
                    bumped = preffed_team.roster.pop()[1]
                    preffed_team.roster.append([dancer_rank, dancer.name])
                    preffed_team.roster.sort(key=lambda dancer: dancer[0])
                    dancer.assigned = True

                    bumped_dancer = self.dancers[bumped]
                    bumped_dancer.assigned = False
                    print(dancer.name + " bumped " + bumped_dancer.name + " from " + preffed_team.name)
                    self.try_assign(bumped_dancer)
            

    def run(self):
        for dancer in self.dancers.values():
            self.try_assign(dancer)