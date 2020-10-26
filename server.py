from flask import Flask, render_template, request, url_for
from Img2txt.Img2txt import letter2code

app = Flask(__name__)


@app.route('/')
def main(num=None):
    return "https://real-cold-river.tistory.com/"


@app.route('/cv_project1')
def cv_project1(num=None):
    return render_template('Img2txt.html', num=num)


@app.route('/cv_project1_result', methods=['POST', 'GET'])
def cv_project1_alg(num=None):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        char_input = request.args.get('char_input')
        char_input = "Test" if char_input == '' else char_input
        temp = request.args.get('num')
        try:
            temp = int(temp)
        except ValueError:
            temp = 15
        c0, c1 = request.args.get('c0'), request.args.get('c1')
        c0 = '6' if c0 == '' else c0
        c1 = '9' if c1 == '' else c1
        char_result = letter2code(char_input, temp, c0, c1)
        return render_template('Img2txt.html', num=temp, char_result=char_result.split("\n"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
