class Team:
    def __init__(self, name, **kwargs):
        self.name = name
        self.prefs = kwargs.get('prefs', [])
        self.max_dancers = kwargs.get('max_dancers', 0)
        self.roster = [] # list of index and name from prefs list