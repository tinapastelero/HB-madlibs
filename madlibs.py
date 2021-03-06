from random import choice, sample

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")
    nice_things = sample(AWESOMENESS, 3)
    # compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           nice_things=nice_things)

@app.route('/game')
def show_madlib_form():

    response = request.args.get("play")
    if response == 'no':
        return render_template('goodbye.html')
    else:
        return render_template('game.html')

@app.route('/madlib', methods=['POST'])
def show_madlib():
    person = request.form.get('person')
    color = request.form.get('color')
    noun = request.form.get('noun')
    adjective_list = request.form.getlist('adjective')
    verb = request.form.get('verb')
    number = request.form.get('number')


    return render_template('madlib.html',
                            person=person,
                            noun=noun,
                            color=color,
                            adjective_list=adjective_list,
                            verb=verb,
                            number=number)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
