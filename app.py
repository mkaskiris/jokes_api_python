from flask import Flask, jsonify, request
from flask_mail import Mail, Message
from flask_cors import CORS
from controllers import jokes
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'dustmastergeneral@gmail.com'
app.config['MAIL_PASSWORD'] = 'dustypete'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# app.config['MAIL_SERVER']='smtp.mailtrap.io'
# app.config['MAIL_PORT'] = 2525
# app.config['MAIL_USERNAME'] = '09c179eaa9d3ba'
# app.config['MAIL_PASSWORD'] = '831aa882d2acdc'
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

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

@app.route('/api/jokes/<int:id>', methods=['GET','POST'])
def joke_handler(id):
    fns = {
        'GET': jokes.show,
        'POST': jokes.create
    }
    resp, code = fns[request.method](request, id)
    # print(resp)
    # print(resp["joke"] + resp["punchline"])
    # msg = Message('ok', 
    #             sender='dustmastergeneral@gmail.com', 
    #             recipients = ['mkaskiris@hotmail.com'])
    # msg.body('Hello there')
    # #msg.body(resp["joke"] + resp["punchline"])
    # mail.send(msg)

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
