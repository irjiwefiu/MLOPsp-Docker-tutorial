from flask import Flask, render_template , request

app=Flask(__name__)

@app.route("/")
def index():
    return '''
        <html>
        <body>
            <form action="/greet" method="POST">
                Enter Your Name : <input type="text" name="username">
                <input type="submit" value="submit">
            </form>
        </body>
        </html>
'''
@app.route("/greet",methods=["POST"])
def greet():
    username= request.form['username']
    return f"<h1>Hello {username}, Welcome to this app for docker demonstration</h1>"

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)

