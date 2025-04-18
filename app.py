from flask import Flask, render_template, request, redirect, session, flash, jsonify, redirect, url_for, send_file
import mysql.connector
from mysql.connector import Error
from flask_bcrypt import Bcrypt
import sqlite3
import re
from flask_mail import Mail, Message
import random
from itsdangerous import URLSafeTimedSerializer
from datetime import datetime
import os
from flask_socketio import SocketIO, emit
from email.mime.text import MIMEText
import pandas as pd
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
load_dotenv()
import os
from werkzeug.utils import secure_filename
from datetime import datetime, timezone
import tempfile

# Setting up the API key and model

import google.generativeai as genai


app = Flask(__name__, template_folder='template', static_folder='static')
bcrypt = Bcrypt(app)

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