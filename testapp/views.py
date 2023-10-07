from flask import render_template,request  # 追加
from testapp import app


@app.route('/')
def index():
    return "Hello, World!"




