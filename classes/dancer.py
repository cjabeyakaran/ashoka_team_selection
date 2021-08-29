class Dancer:
    def __init__(self, name, **kwargs):
        self.name = name
        self.prefs = kwargs.get('prefs', [])
        self.assigned = False

    def add_pref(self, team: str):
        self.prefs.append(team)

    def highest_pref(self):
        team = ""
        try:
            team = self.prefs.pop(0)
        except IndexError:
            team = "unassigned"

        return team

    def set_team(self, team: str):
        self.team = team