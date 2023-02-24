from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/checkresult/<int:score>')
def checkresult(score):
    res = ""
    if score >=50:
        res = "PASS"
    else:
        res ="FAIL"
    return render_template('result.html',result=res)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_sc=float(request.form['datascience'])
        total_score = (science+maths+c+data_sc)
    return redirect(url_for('checkresult',score=total_score))

if __name__ == "__main__":
    app.run()

