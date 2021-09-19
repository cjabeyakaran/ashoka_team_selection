import pandas as pd
from classes.algo import Algo

class Program:
    def __init__(self):
        self.algo = Algo()

    def handle_students_file(self, file_path):
        # helper function to convert row into dancer object
        def create_dancer(row):
            prefs = []
            gender = row["Gender"] # mark dancer as Male vs Female

            cols = ["Preference 1:", "Preference 2:", "Preference 3:", "Preference 4:", "Preference 5:"]
            for col in cols:
                if pd.notnull(row[col]):
                    prefs.append(f"{row[col]} - {gender}s")

                    if row[col] == "Raas" and gender == "Female":
                        prefs.append(f"{row[col]} - Males")

            self.algo.add_dancer(row["Name:"].strip(), prefs)

            return row

        # import spreadsheet and create dancer object for each row
        df = pd.read_excel(file_path)
        df.apply(create_dancer, axis=1)

    def handle_teams_file(self, file_path):
        # helper function to convert row into team Females and team Males objects
        df = pd.read_excel(file_path, index_col="Team:")

        team_names = ["Raas", "Garba", "Chaahat", "Bhangra"]
        for name in team_names:
            girl_prefs = df.loc[name, "List girl dancers/singers in order of preference:"]
            max_girls = df.loc[name, "Ideally, how many girls are you looking to recruit this year?"]
            
            self.algo.add_team(f"{name} - Females", girl_prefs, max_girls)

            if name != "Garba":
                boy_prefs = df.loc[name, "List boy dancers/singers in order of preference:"]
                max_boys = df.loc[name, "Ideally, how many boys are you looking to recruit this year?"]
            
                self.algo.add_team(f"{name} - Males", boy_prefs, max_boys)


    def run_matching(self):
        return self.algo.run()

            


        
