from flask import Flask, render_template, request
from program import Program
from werkzeug.utils import secure_filename

app = Flask(__name__)

program = Program()

# render index.html
@app.route('/')
def index():
    return render_template('index.html')

# upload team prefs
@app.route('/teamprefs', methods=['POST'])
def team_upload():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename()
        f.save(filename)
        program.handle_teams_file(filename)
        return "True"
        

# upload student prefs
@app.route('/studentprefs', methods=['POST'])
def student_upload():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename()
        f.save(filename)
        program.handle_students_file(filename)
        return "True"

# run matching algo
# @app.route('/match')
# def match():


if __name__ == '__main__':
    app.run()