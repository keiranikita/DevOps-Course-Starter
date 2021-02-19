from flask import Flask, render_template, request, redirect

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item, save_item, get_item

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    todo_items=get_items()
    return render_template('index.html', todo_items=todo_items)

@app.route('/', methods=['POST'])
def add_todoitem():
    title=request.form.get("additem")
    add_item(title)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)