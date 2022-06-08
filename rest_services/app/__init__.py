from os import environ
from flask import Flask


from config import app_config
from .square_equation import square_equation as square_eq_blp
from .guess_color import guess_color as guess_clr_blp

app = Flask(__name__)
app.config.from_object(app_config)

app.register_blueprint(square_eq_blp, url_prefix='')
app.register_blueprint(guess_clr_blp, url_prefix='')