# from flask import Flask, jsonify
# from flask_cors import CORS
# from openfx_api.openfx_api import OpenFxApi
# from api.web_options import get_options
# import http

# from scraping.reuters_com import reuters_com
# from scraping.investing_com import get_pair

# app = Flask(__name__)
# CORS(app)

# def get_response(data):
#     if data is None:
#         return jsonify(dict(message='error getting data')), http.HTTPStatus.NOT_FOUND
#     else:
#         return jsonify(data)


# @app.route("/api/test")
# def test():
#     return jsonify(dict(message='hello'))


# @app.route("/api/headlines")
# def headlines():
#     return get_response(reuters_com())


# @app.route("/api/account")
# def account():
#     return get_response(OpenFxApi().get_account_summary())


# @app.route("/api/options")
# def options():
#     return get_response(get_options())


# @app.route("/api/technicals/<pair>/<tf>")
# def technicals(pair, tf):
#     return get_response(get_pair(pair, tf))


# @app.route("/api/prices/<pair>/<granularity>/<count>")
# def prices(pair, granularity, count):
#     return get_response(OpenFxApi().web_api_candles(pair, granularity, count))


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, jsonify
from flask_cors import CORS
from openfx_api.openfx_api import OpenFxApi
from api.web_options import get_options
import http
import subprocess
import os
import sys
import subprocess  # Import subprocess to run external scripts
from scraping.reuters_com import reuters_com
from scraping.investing_com import get_pair

app = Flask(__name__)
CORS(app)

def get_response(data):
    if data is None:
        return jsonify(dict(message='error getting data')), http.HTTPStatus.NOT_FOUND
    else:
        return jsonify(data)


@app.route("/api/test")
def test():
    return jsonify(dict(message='hello'))


@app.route("/api/headlines")
def headlines():
    return get_response(reuters_com())


@app.route("/api/account")
def account():
    return get_response(OpenFxApi().get_account_summary())


@app.route("/api/options")
def options():
    return get_response(get_options())


@app.route("/api/technicals/<pair>/<tf>")
def technicals(pair, tf):
    return get_response(get_pair(pair, tf))


@app.route("/api/prices/<pair>/<granularity>/<count>")
def prices(pair, granularity, count):
    return get_response(OpenFxApi().web_api_candles(pair, granularity, count))


# New Endpoint to Run the Bot Script
@app.route("/api/run-bot", methods=["POST"])
def run_bot():
    try:
        # Construct the absolute path to the bot script
        script_path = os.path.abspath("run_bot.py")

        # Command to open a terminal and run the script
        if sys.platform.startswith('win'):
            # Windows command to open a terminal and execute the script
            subprocess.Popen(["start", "cmd", "/k", f"python {script_path}"], shell=True)
        elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
            # Linux or macOS command to open a terminal and execute the script
            subprocess.Popen(["gnome-terminal", "--", "python3", script_path])
        else:
            raise Exception("Unsupported operating system")

        return jsonify({"success": True, "message": "Bot execution started in a new terminal"}), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error running bot: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
