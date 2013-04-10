from flask import Flask
from flask import request
import os
from random import choice


app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
    r = twiml.Response()
    if request.form['Body'].upper() == "HELP":
        r.sms("Welcome to the Reasons That Nicole Loves You hotline.  Text Whyy?? " \
                "to get one random reason.")
    else:
        r.sms(choice(reasons))
    return str(r)


reasons = [
    'You challenge me to try new things! Like Python!',
    'You are fiiiiine']


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True

    app.run(host='0.0.0.0', port=port)
