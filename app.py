from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/my_plants', methods=['POST'])
def my_plants():
    json_file = request.get_json()
    sensor = json_file['sensor']
    print(sensor)

    return 'OK'


if __name__ == '__main__':
    app.run()
