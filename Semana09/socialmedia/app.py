from flask import Flask, redirect, render_template, request, url_for
from models import *


app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET'] )

def index():
    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(name, post)
    
    return render_template('index.html', posts=get_posts())

@app.route('/delete/<int:id>')
def delete_by_id(id):
    delete_post_by_id(id)
    return render_template('index.html', posts=get_posts())

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    if request.method == 'POST':
        content = request.form['content']
        print(content)
        update_post(id, content)
        return redirect('/')
     
    else:
        post_edit = get_post_by_id(id)
        return render_template('update.html', post=post_edit)
    

if __name__ == '__main__':
    app.run(debug=True)