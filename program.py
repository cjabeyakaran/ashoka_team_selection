import pandas as pd
from classes.algo import Algo

# check later for column names, especially gender

class Program:
    def __init__(self):
        self.algo = Algo()

    def handle_students_file(self, file_path):
        # helper function to convert row into dancer object
        def create_dancer(row):
            prefs = []
            gender = row["Gender"] # mark dancer as boy vs girl

            cols = ["Preference 1:", "Preference 2:", "Preference 3:", "Preference 4:", "Preference 5:"]
            for col in cols:
                if pd.notnull(row[col]):
                    prefs.append(f"{row[col]} - {gender}s")

                    if row[col] == "Raas" and gender == "Girls":
                        prefs.append(f"{row[col]} - Boys")

            self.algo.add_dancer(row["Name:"], prefs)

            return row

        # import spreadsheet and create dancer object for each row
        df = pd.read_excel(file_path)
        df.apply(create_dancer, axis=1)
