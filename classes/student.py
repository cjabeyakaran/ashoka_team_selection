class Student:
    def __init__(self, name, **kwargs):
        self.name = name
        self.prefs = kwargs.get('prefs', [])
        self.team = ""

    def addPref(self, team: str):
        self.prefs.append(team)

    def highestPref(self):
        return self.prefs.pop(0)

    def setTeam(self, team: str):
        self.team = team