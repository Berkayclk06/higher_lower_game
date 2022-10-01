import random

from flask import Flask
app = Flask(__name__)

random_num = random.randint(0, 9)


def make_head(function):
    def wrapper():
        return f"<h1>{function()}</h1>"
    return wrapper


@app.route('/')
@make_head
def quest():
    return "Guess a number between 0 and 9" \
           "<br></br>" \
           "<img src='https://media.giphy.com/media/IsfrRWvbUdRny/giphy.gif' width=300>"


@app.route("/<int:number>")
def smaller(number):
    if number < random_num:
        return "<h1 style='color: Red'>Too low, try again</h1>" \
                "</br>" \
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif number > random_num:
        return "<h1 style='color: Blue'>Too hi, try again</h1>" \
               "</br>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h1 style='color: Pink'>You found it!</h1>" \
                "</br>" \
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
