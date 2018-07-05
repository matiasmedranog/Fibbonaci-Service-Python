from flask import Flask
import json
import mimerender
from Fibonacci import Fibonacci

mimerender = mimerender.FlaskMimeRender()

render_json = lambda **args: json.dumps(args)

app = Flask(__name__)

@app.route('/')
@app.route('/<number>')
@mimerender(
    default = 'json',
    json = render_json
)
def showMessage(number='10'):
    return {'n':Fibonacci(int(number)),'n-1':Fibonacci(int(number)-1)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001)
