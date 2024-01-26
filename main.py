##Integrate html  with falsk
##HTTP verb GET and post

##JINJA2 tempplate engine
'''
{%...%} for statements
{{ }} expressions to print output
{#...#} this is the output
'''
from flask import Flask,redirect,url_for,render_template,request
#WSGI application
app = Flask(__name__)
@app.route('/')
def Home():
    return render_template('index.html')
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
        
    exp={'score':score,'res':res}      
    return render_template('result.html',result=exp)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has pased and the marks is "+str(score)


@app.route('/results/<int:score>')
def results(score):
    result=""
    if score<35:
       result='fail'
    else:
        result='success'
    return redirect(url_for(result,score))  
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        AIML = float(request.form['AIML'])
        DATASCINECE = float(request.form['DATASCINECE'])
        CYBERSEQURITY = float(request.form['CYBERSEQURITY'])
        total_score=(AIML+DATASCINECE+CYBERSEQURITY)/3
    res=""
    return redirect(url_for('success',score=total_score)) 
      
        
if __name__=='__main__':
    app.run(debug=True)