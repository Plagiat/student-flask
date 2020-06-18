from flask import Flask
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    return "Привет"


def main():
    db_session.global_init("db/students_attendances.sqlite")
    app.run(port=5000)


if __name__ == '__main__':
    main()