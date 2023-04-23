from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def home(times = 3, color = 'yellow'):
    return render_template('home.html', times=times, color=color)

@app.route('/play/<int:times>')
def repeat(times, color= 'yellow'):
    return render_template('home.html', times=times, color=color)

@app.route('/play/<int:times>/<color>')
def color(times, color):
    return render_template('home.html', times=times, color=color)

if __name__ == '__main__':
    app.run(debug = True, port= 5001)


