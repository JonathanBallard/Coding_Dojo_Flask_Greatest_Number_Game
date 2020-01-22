from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
# our index route will handle rendering our form




@app.route('/')
def index():
    if 'randomNum' in session:
        pass
        # print('Number Is: ' + str(session['randomNum']))
    else:
        session['randomNum'] = random.randint(1,100)
        # print('Number Created: ' + str(session['randomNum']))
    
    if 'numTries' in session:
        pass
    else:
        session['numTries'] = 0

    if 'guess' in session:
        pass
        # print('Guess Found, and Is: ' + str(session['guess']))
    else:
        if request.form.get('guess'):
            session['guess'] = int(request.form['guessedNum'])
            # print('Guess Is: ' + str(session['guess']))
        else:
            session['guess'] = -1
            # print('Guess DEFAULT: ' + str(session['guess']))

    return render_template("index.html")


@app.route('/destroy_session')
def destroy():

    session.clear()
    return redirect("/")

@app.route('/guess', methods=['POST'])
def guess():

    if 'numTries' in session:
        session['numTries'] += 1
    else:
        session['numTries'] = 0
    session['guess'] = int(request.form['guessedNum'])
    session['randomNum'] = int(session['randomNum'])
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)