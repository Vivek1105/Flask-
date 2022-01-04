# Building url dynamically
# variable rules and URL building



from flask import Flask, redirect, url_for 
web=Flask(__name__)



@web.route('/passs/<int:score>')
def passs(score):
    return "the person has passed with"+ str(score)



@web.route("/failed/<int:score>")
def failed(score):
    return "the person has failed with"+ str(score)


#Result checker 
@web.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='failed'
    else:
        result='passs'
    return redirect(url_for(result,score=marks))

if __name__=="__main__":
    web.run(debug=True)

