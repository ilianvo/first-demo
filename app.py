from flask import Flask, render_template
import random
app = Flask(__name__)
# list of cat images
images = [
  "https://media1.giphy.com/media/xTiIzJSKB4l7xTouE8/giphy.gif?cid=790b7611cbf3bcb6c65ed24894cdafa210449ba4c47c09a6&rid=giphy.gif&ct=g",
]
@app.route('/')
def index():
  url = random.choice(images)
  return render_template('index.html', url=url)
if __name__ =='__main__':
    app.run(host="0.0.0.0")