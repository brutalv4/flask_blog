from flask import (
    Flask,
    render_template as render,
    flash,
    redirect,
    url_for)
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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been successfully logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful! Please check username and password', 'danger')

    return render('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run()
