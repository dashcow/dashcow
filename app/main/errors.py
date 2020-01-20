from flask import redirect

from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return redirect('/404'), 404