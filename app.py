from flask import Flask, render_template as render, url_for

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
