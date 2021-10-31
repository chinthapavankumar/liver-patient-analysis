from flask import Flask,request,render_template,redirect,url_for
app = Flask(__name__) 

from joblib import load
model=load('navieliver.save')

@app.route('/')
def home():
	return render_template('index.html')
@app.route('/liverdis',methods=['post'])
def liver():
	xt=[[float(x) for x in request.form.values()]]
	print(xt)
	predic=model.predict(xt)
	print(predic)
	if(predic[0]):
		return render_template('liverdisease.html')
	else:
		return render_template('nonliverdisease.html')
	

	

	

if __name__ == '__main__': 
	app.run(debug=True) 
	
