from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def si():

    result = None
    total = None
    p = None
    t = None
    r = None

    if request.method == 'POST':

        p = float(request.form['p'])
        t = float(request.form['t'])
        r = float(request.form['r'])

        result = (p * t * r) / 100
        total = p + result

    return render_template(
        'index.html',
        result=result,
        total=total,
        p=p,
        t=t,
        r=r
    )


@app.route('/greet/<uname>')
def greet(uname):
    return f"Good morning, {uname}!"


if __name__ == '__main__':
    app.run(debug=True, port=3500)