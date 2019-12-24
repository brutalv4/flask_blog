from flask import (
    Flask,
    render_template as render
)
from flask_dotenv import DotEnv

from forms import (
    RegistrationForm,
    LoginForm
)

app = Flask(__name__)
env = DotEnv(app)

posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post2',
        'content': 'Second post content',
        'date_posted': 'April 22, 2018'
    },

]


@app.route('/')
@app.route('/home')
def home():
    return render('home.html', posts=posts)


@app.route('/about')
def about():
    return render('about.html', title='About')


@app.route('/register')
def register():
    return render('register.html', title='Register', form=RegistrationForm())


@app.route('/login')
def login():
    return render('login.html', title='Login', form=LoginForm())


if __name__ == '__main__':
    app.run()
