# from flask import Flask

# app = Flask(__name__)
# @app.route('/verification/<string:num>')
# def verification(num):
#     return "the verification num is" +(num)




# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask
app = Flask(__name__)
@app.route('/results/<int:marks>')
def results(marks):
    return ("yor marks is" +str(marks))

if __name__ == '__main__':
    app.run(debug=True)
