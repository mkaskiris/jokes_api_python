from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import jokes
from werkzeug import exceptions
import smtplib

app = Flask(__name__)
CORS(app)


def email_setup(resp):

    gmail_user = 'kaskas1334@gmail.com'
    gmail_password = 'vgnnhnlrsqdlhqxl'
    recipient = 'mkaskiris@hotmail.com'
    email_text = resp['joke'] + '\t' + resp['punchline']

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user,
                        recipient,
                        email_text)
        server.close()
    except Exception as e:
        print(f'Something went wrong, {e}')


@app.route('/')
def home():
    return jsonify({'message': 'Hello from Team J.U.M.P!'}), 200


@app.route('/api/jokes', methods=['GET', 'POST'])
def jokes_handler():
    fns = {
        'GET': jokes.index,
        'POST': jokes.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code


@app.route('/api/jokes/<int:id>', methods=['GET', 'POST'])
def joke_handler(id):
    fns = {
        'GET': jokes.show,
        'POST': jokes.create
    }
    resp, code = fns[request.method](request, id)
    email_setup(resp)
    return jsonify(resp), code


@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404


@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400


@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500


if __name__ == "__main__":
    app.run(debug=True)
