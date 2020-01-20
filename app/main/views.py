from flask import send_from_directory
from . import main


@main.route('/', defaults={'path': ''})
@main.route('/<path:path>')
def catch_all(path):
    if path and '/' not in path:
        return send_from_directory(main.static_folder, path)
    return main.send_static_file('index.html')
