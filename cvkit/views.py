
from flask import Blueprint, render_template

from . import parser


blueprint = Blueprint(
    "cvbuilder",
    __name__,
    template_folder="templates",
)


@blueprint.get("/")
def index():
    cv = parser.load()

    return render_template(
        "index.html",
        cv=cv,
    )
    