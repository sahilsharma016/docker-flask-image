from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/second_page')
def second_page():
    return render_template('second_page.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)
