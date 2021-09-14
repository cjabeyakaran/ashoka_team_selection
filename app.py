from flask import Flask, render_template, request
from program import Program
from werkzeug.utils import redirect, secure_filename

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
        filename = secure_filename(f.filename)
        f.save(filename)
        program.handle_teams_file(filename)
        return redirect(request.referrer)
        

# upload student prefs
@app.route('/studentprefs', methods=['POST'])
def student_upload():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(filename)
        program.handle_students_file(filename)
        return redirect(request.referrer)

# run matching algo
@app.route('/match')
def match():
    return program.run_matching()

if __name__ == '__main__':
    app.run()