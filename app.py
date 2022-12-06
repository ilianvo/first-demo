from flask import Flask, render_template
import random
app = Flask(__name__)
# list of cat images
images = [
  "https://www.pngkey.com/png/full/193-1934583_jenkins-x.png",
  "https://miro.medium.com/max/1400/1*QTmgOmxLr78Ty_evSD_Riw.gif",
]
@app.route('/')
def index():
  url = random.choice(images)
  return render_template('index.html', url=url)
if __name__ =='__main__':
    app.run(host="0.0.0.0")
