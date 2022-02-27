from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object("sinntelligence.config.ProductionConfig")
Bootstrap(app)

from sinntelligence import auth
from sinntelligence import routes
