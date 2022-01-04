#Integrate html with flask 
#http verb GET And POST

## jinja2 template 
'''
{%...%} for condition nd loop statemennts
{{   }} expresion to print output
{#.....#} this is for comments 
'''

from flask import Flask, redirect, url_for ,render_template,request
web=Flask(__name__)



@web.route('/')
def welcome():
    return render_template('index.html')

# @web.route('/passs/<int:score>')
# def passs(score):
#     res=""
#     if score>50:
#         res="PASS"
#     else:
#         res="FAIL"
#     return render_template('results.html',results=res)




##for testing jinja {{}} above condition is writen in results.html page 
# @web.route('/passs/<int:score>')
# def passs(score):
#     return render_template('results.html',results=score)





@web.route('/passs/<int:score>')
def passs(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    exp={'score':score,'res':res}
    return render_template('results.html',results=exp)



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

    

#Result checker html page 
@web.route('/submit',methods=['POST','GETS'])
def submit():
        total_score=0
        if request.method=='POST':
            science=float(request.form['science'])
            maths=float(request.form['maths'])
            c=float(request.form['c'])
            datascience=float(request.form['datascience'])
            total_score=(science+maths+c+datascience)/4
        res=""
        if total_score>=50:
            res="passs"
        else:
            res="failed"
        return redirect(url_for(res,score=total_score)) 



if __name__=="__main__":
    web.run(debug=True)

