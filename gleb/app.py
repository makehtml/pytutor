from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    user_name = 'Gleb'
    return render_template('index.j2', user_name=user_name)


@app.route('/test')
def test():
    user_name_test = 'Gleb_test'
    return render_template('test.j2', user_name=user_name_test)
