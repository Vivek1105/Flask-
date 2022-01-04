from flask import Flask
app=Flask(__name__)



@app.route("/passs/<int:score>")
def passs(score):
    return "the person has passed with"+ str(score)

@app.route("/failed/<int:score>")
def failed(score):
    return "the person has failed with"+ str(score)

if __name__=="__main__":
    app.run(debug=True)