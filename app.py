from flask import Flask

app = Falsk(__name__)

@app.route('/')
def home():
    return 'Hello Flask!!'

@app.route('/about')
def about():
    return 'This is about page'

@app.route('/contact')
def contact():
    return 'This is contact page'

@app.route('/user/<username>')
def user(username):
    return f'Userid:{username}'

@app.route('/post/<int: postid>')
def postnumber(postid):
    return f'Postid : {postid}'

if __name__ == '__main__':
    app.run(debug = True)