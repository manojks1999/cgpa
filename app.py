from flask import Flask,request, url_for, redirect, render_template
import math
import requests
import pyrebase

app=Flask(__name__)


###################################################################
# NEWS API EXTRACTION
###############################################################
main_url="http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=4ba3a1be51cf433f98c1eaafea95ed83"
open_bbc_page=requests.get(main_url).json()
article=open_bbc_page["articles"]
title=[]
authers=[]
description=[]
url=[]
img_url=[]

for i in article:
  (title.append(i["title"]))
  (authers.append(i["author"]))
  (description.append(i["description"]))
  (url.append(i["url"]))
  (img_url.append(i["urlToImage"]))

len1=len(authers)  

"""for i in range(len(authers)):
  print(i," author : ",authers[i])
  print(i," Title : ",title[i])
  print(i," Description : ",description[i])
  print(i," Url : ",url[i])
  print("\n\n\n")"""
###############################################################
############################################################
########################################################################################################
#########################################################################################################
#FIREBASE     FIREBASE      FIREBASE      FIREBASE      FIREBASE      FIREBASE
###########################################################################################################
##########################################################################################################
firebaseConfig = {
    "apiKey": "AIzaSyDigCy3ADXRfCIxy2d735c1JfQc6Q6sO_g",
    "authDomain": "sport-management-19a46.firebaseapp.com",
    "databaseURL": "https://sport-management-19a46.firebaseio.com",
    "projectId": "sport-management-19a46",
    "storageBucket": "sport-management-19a46.appspot.com",
    "messagingSenderId": "189512983929",
    "appId": "1:189512983929:web:1fe2cba9570b5bf1a0bba8"
  }
# Initialize Firebase
firebase=pyrebase.initialize_app(firebaseConfig);

db=firebase.database()

#db.child("admin").update({"username":"manojks"})
#db.child("admin").update({"password":"8277370800"})
#users=db.child("names").child("name").get()
#print(users.val())
#print(users.key())
#db.child("names").child("name").remove()



#db.child("admin").update({"username":"manojks"})
#db.child("admin").update({"password":"8277370800"})



username=db.child("admin").child("username").get()
password=db.child("admin").child("password").get()
username1=(username.val())
password1=(password.val())


username1=db.child("marks").get().val()
print(username1)

def upmarks(usn,sub1,sub2,sub3,sub4,sub5,sub6,total):
	db.child("marks").child(usn).push([{"sub1":sub1},{"sub2":sub2},{"sub3":sub3},{"sub4":sub4},{"sub5":sub5},{"sub6":sub6},{"lab1":lab1},{"lab2":lab2},{"total":total}])

"""usn="4AI17IS031"
print(type(usn))
total=100
print(type(total))
upmarks(usn,10,20,30,40,50,60,10,20,total)"""

"""v=db.child("marks").get()
v1=v.val()
for v0 in v1:
	print(v0)
	v2=db.child("marks").child(v0).get()
	v3=v2.val()
	for v5 in v3:
		print(v5)
		v4=db.child("marks").child(v0).child(v5).get()
		v6=v4.val()
		for v7 in v6:
			print(v7)"""


#db.child("feedback").push([{"name":name},{"feed":text}])
########################################################################################################
#########################################################################################################
#FIREBASE     FIREBASE      FIREBASE      FIREBASE      FIREBASE      FIREBASE
###########################################################################################################
##########################################################################################################


@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/ece.html')
def ece():
    return render_template('ece.html')

@app.route('/ce.html')
def ce():
    return render_template('ce.html')


@app.route('/eee.html')
def eee():
    return render_template('eee.html')


@app.route('/me.html')
def me():
    return render_template('me.html')


@app.route('/cse.html')
def cse():
    return render_template('cse.html')


@app.route('/index.html')
def index():
    return render_template('index.html') 

@app.route('/feedback.html')
def feedbackr():
    return render_template('feedback.html') 


@app.route('/thank.html')
def thank():
    return render_template('thank.html') 

@app.route('/login.html')
def logi():
    return render_template('login.html') 

@app.route('/tech_news.html')
def home():
  return render_template('tech_news.html',len1=len1,authers=authers,title=title,description=description,url=url,img_url=img_url)



@app.route('/login',methods=['GET','POST'])
def login():
	if request.method=='POST':
		usr=str(request.form['user'])
		pass1=str(request.form['pass'])
	if usr==username1 and pass1==password1:
		val="Go to Firebase Console not yet developed code"
	else:
		val="Invalid Credential!"
	return render_template('login.html',val=val)


@app.route('/feedback',methods=['GET','POST'])
def feed():
	if request.method=='POST':
		name=str(request.form['name'])
		text=str(request.form['feed'])
		if name is not "":
			db.child("feedback").child(name).push({"feed":text})#FIREBASE WORKING
	return render_template('thank.html')
######################
#####################




#########################
#######################
@app.route('/res',methods=['POST','GET'])
def res():
	if request.method=='POST':
		branch=request.form['branch']
		print(branch)
		try:
			usn=str(request.form['usn'])
			sub1=int(request.form['Sub1'])
			sub2=int(request.form['Sub2'])
			sub3=int(request.form['Sub3'])
			sub4=int(request.form['Sub4'])
			sub5=int(request.form['Sub5'])
			sub6=int(request.form['Sub6'])
			lab1=int(request.form['lab1'])
			lab2=int(request.form['lab2'])
			print(sub1)
			print(sub2)
			print(sub3)
			print(sub4)
			print(sub5)
			print(sub6)
			print(lab1)
			print(lab2)
			print(usn)
		except Exception as e:
			if(branch=='ise'):
				return render_template('index.html',pred='Please input correct values!')
			if(branch=='cse'):
				return render_template('cse.html',pred='Please input correct values!')
			if(branch=='eee'):
				return render_template('eee.html',pred='Please input correct values!')
			if(branch=='ece'):
				return render_template('ece.html',pred='Please input correct values!')
			if(branch=='me'):
				return render_template('me.html',pred='Please input correct values!')
			if(branch=='ce'):
				return render_template('ce.html',pred='Please input correct values!')
		
		sub1=int((sub1/10))
		sub2=int((sub2/10))
		sub3=int((sub3/10))
		sub4=int((sub4/10))
		sub5=int((sub5/10))
		sub6=int((sub6/10))
		lab1=int((lab1/10))
		lab2=int((lab2/10))
		marks1=[]
		marks=[sub1,sub2,sub3,sub4,sub5,sub6,lab1,lab2]
		for ele in marks:
			if ele>=10:
				ele=9
			marks1.append(ele+1)
		sub1,sub2,sub3,sub4,sub5,sub6,lab1,lab2=marks1
		print(sub1,sub2,sub3,sub4,sub5,sub6,lab1,lab2)




	

		if(branch=='ise'):
			try:
				result=((sub1*4)+(sub2*4)+(sub3*4)+(sub4*4)+(sub5*3)+(sub6*3)+(lab1*2)+(lab2*2))/260
				print(result*10)
				result=round(result*10,2)
				print(result)
				if usn!="":
					upmarks(usn,sub1,sub2,sub3,sub4,sub5,sub6,lab1,lab2,result)
			except Exception as e:
				return render_template('index.html',pred='Please input correct value')
			print(result)
			return render_template('index.html',pred='Your result is {}'.format(str(result)))
		


		if(branch=='ece'):
			try:
				result=((sub1*4)+(sub2*4)+(sub3*4)+(sub4*4)+(sub5*3)+(sub6*3)+(lab1*2)+(lab2*2))/260
				print(result*10)
				result=round(result*10,2)
				print(result)
				if usn!="":
					upmarks(usn,sub1,sub2,sub3,sub4,sub5,sub6,result)
			except Exception as e:
				return render_template('ece.html',pred='Please input correct value')
			print(result)
			return render_template('ece.html',pred='Your result is {}'.format(str(result)))
		


		if(branch=='cse'):
			try:
				result=((sub1*4)+(sub2*4)+(sub3*4)+(sub4*4)+(sub5*3)+(sub6*3)+(lab1*2)+(lab2*2))/260
				print(result*10)
				result=round(result*10,2)
				if usn!="":
					upmarks(usn,sub1,sub2,sub3,sub4,sub5,sub6,result)
			except Exception as e:
				return render_template('cse.html',pred='Please input correct value')
			print(result)
			return render_template('cse.html',pred='Your result is {}'.format(str(result)))
		


		if(branch=='me'):
			try:
				result=((sub1*4)+(sub2*4)+(sub3*4)+(sub4*4)+(sub5*3)+(sub6*3)+(lab1*2)+(lab2*2))/260
				print(result*10)
				result=round(result*10,2)
				if usn!="":
					upmarks(usn,sub1,sub2,sub3,sub4,sub5,sub6,result)
			except Exception as e:
				return render_template('me.html',pred='Please input correct value')
			print(result)
			return render_template('me.html',pred='Your result is {}'.format(str(result)))
		


		if(branch=='ce'):
			try:
				result=((sub1*4)+(sub2*4)+(sub3*4)+(sub4*4)+(sub5*3)+(sub6*3)+(lab1*2)+(lab2*2))/260
				print(result*10)
				result=round(result*10,2)
				print(result)
				if usn!="":
					upmarks(usn,sub1,sub2,sub3,sub4,sub5,sub6,result)
			except Exception as e:
				return render_template('ce.html',pred='Please input correct value')
			print(result)
			return render_template('ce.html',pred='Your result is {}'.format(str(result)))
		


		if(branch=='eee'):
			try:
				result=((sub1*4)+(sub2*4)+(sub3*4)+(sub4*4)+(sub5*3)+(sub6*3)+(lab1*2)+(lab2*2))/260
				print(result*10)
				result=round(result*10,2)
				if usn!="":
					upmarks(usn,sub1,sub2,sub3,sub4,sub5,sub6,result)
			except Exception as e:
				return render_template('eee.html',pred='Please input correct value')
			print(result)
			return render_template('eee.html',pred='Your result is {}'.format(str(result)))




if __name__=='__main__':
	app.run(debug=True)