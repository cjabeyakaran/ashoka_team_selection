class Team:
    def __init__(self, name, **kwargs):
        self.name = name
        self.boys = kwargs.get('boys', [])
        self.girls = kwargs.get('girls', [])
        self.max_boys = kwargs.get('max_boys', 0)
        self.max_girls = kwargs.get('max_girls', 0)
        self.roster = []

    def add_boy(self, boy: str):
        self.boys.append(boy)

    def add_girl(self, girl: str):
        self.girls.append(girl)

    def set_max_boys(self, max_boys: int):
        self.max_boys = max_boys

    def set_max_girls(self, max_girls: int):
        self.max_girls = max_girls