from flask import Flask, render_template
import random
app = Flask(__name__)
# list of cat images
images = [
  "https://www.jenkins.io/images/logos/jenkins-x/jenkins-x.png",
]
@app.route('/')
def index():
  url = random.choice(images)
  return render_template('index.html', url=url)
if __name__ =='__main__':
    app.run(host="0.0.0.0")
