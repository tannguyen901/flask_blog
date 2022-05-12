from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)


posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
obj_list = []

for msg in posts:
    post_obj = Post(msg['id'],msg['body'],msg['title'],msg['subtitle'])
    obj_list.append(post_obj)


@app.route('/')
def home():
    return render_template("index.html", posts=obj_list)

@app.route('/post/<int:id>')
def blog(id):
    return_obj = None
    for obj in obj_list:
        if obj.id == id:
            return_obj = obj
    return render_template('post.html', post=return_obj )
    

if __name__ == "__main__":
    app.run(debug=True)