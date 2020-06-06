from flask import Flask

app = Flask(__name__)

from flaskApp import endpoints
from flaskApp import admin