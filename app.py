from flask import Flask, render_template, request
from program import Program
from werkzeug.utils import secure_filename
import os

curr = os.getcwd()
UPLOAD_FOLDER = os.path.join(curr, "uploads")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

program = Program()

# render index.html
@app.route('/')
def index():
    return render_template('index.html')

# run matching algo
@app.route('/match', methods = ['POST'])
def match():
    # return program.run_matching()
    team_f = request.files['team-file']
    team_filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(team_f.filename))
    team_f.save(team_filepath)
    program.handle_teams_file(team_filepath)

    dancer_f = request.files['dancer-file']
    dancer_filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(dancer_f.filename))
    dancer_f.save(dancer_filepath)
    program.handle_students_file(dancer_filepath)

    return render_template('rosters.html', rosters=program.run_matching())

if __name__ == '__main__':
    app.run()