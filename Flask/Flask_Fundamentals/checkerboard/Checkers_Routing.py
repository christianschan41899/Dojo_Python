from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def default(x = 8, y = 8):
    height = 45*y
    width = 45*x
    times = int(x/2)
    return render_template('checkered_display.html', by_y = y, by_x = x, width = width, height = height, times = times)

@app.route('/<int:x>')
def one_param(x, y = 8):
    return default(x, y)

@app.route('/<int:x>/<int:y>')
def two_param(x, y):
    return default(x, y)

if __name__=="__main__":   
    app.run(debug=True) 