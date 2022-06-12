from flask import Flask, render_template
from flask import request
from flask import Response

import random
import json

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9301)