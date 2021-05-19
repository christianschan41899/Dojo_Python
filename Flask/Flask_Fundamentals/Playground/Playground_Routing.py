from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def playground():
    return render_template('Playground.html')

@app.route('/play/<int:boxes>')
def playground2(boxes):
    return render_template('Playground_x_times.html', times = boxes)

@app.route('/play/<int:boxes>/<colour>')
def playground3(boxes, colour):
    return render_template('Playground_x_times_color.html', times = boxes, color = colour)
if __name__=="__main__":   
    app.run(debug=True) 