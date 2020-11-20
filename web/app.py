import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def mainmenu():

    return """
    <html>
    <body>
    <center><h1>Hello World! from AWS CodeDeploy.</h1><br/>
    <h2>My Name is Satoshi</h2>
    <iframe width="1280" height="720" src="https://www.youtube.com/embed/GVrRXhS0mLs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </body>
    </html>"""

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=80)
