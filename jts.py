import os
import sys

from flask import Blueprint, Flask, redirect, render_template


DIR = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()


bp = Blueprint(
    __name__,
    __name__,
    template_folder=DIR
)


@bp.route('/')
def init():
    return redirect('/index.html')


@bp.route('/<path:filename>')
def show(filename):
    return render_template(filename)


def run():
    app = Flask(__name__)
    app._static_folder = os.path.abspath('static/')

    app.config.update(
        TEMPLATES_AUTO_RELOAD=True
    )

    app.register_blueprint(bp)

    app.run(debug=True)
