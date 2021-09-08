from flask import Flask, render_template, request
from program import Program

app = Flask(__name__)

# render index.html
@app.route('/')
def index():
    return render_template("index.html")

# upload team prefs
@app.route('/teamprefs', methods=['POST'])
def team_upload():
    if request.method == 'POST':
        file = request.files['file']
        # file.save(file.filename)
        print(file.read())

# upload student prefs
@app.route('/studentprefs', methods=['POST'])
def student_upload():
    if request.method == 'POST':
        file = request.files['file']
        # file.save(file.filename)
        print(file.read())

# run matching algo
# @app.route('/match')
# def match():


if __name__ == '__main__':
    app.run()