from flask import Flask, render_template, request, redirect, session, flash, jsonify, redirect, url_for, send_file


app = Flask(__name__, template_folder='template', static_folder='static')


@app.route('/')
def index():
    return render_template('jam.html')

@app.route('/van')
def contact():
    return render_template('van.html')

@app.route('/kap')
def kap():
    return render_template('jam.html')
if __name__ == '__main__':
    app.run(debug = True)