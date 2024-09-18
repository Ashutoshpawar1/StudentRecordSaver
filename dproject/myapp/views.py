from django.http import HttpResponse      
from django.shortcuts import render
import MySQLdb

# Create your views here.

# def call(request):
#     return HttpResponse("{}mydjango".format(num))
# def renderhtml(req):
#     return render(req,'p1.html')
# def render_1(req):
#     return render(req,"p1.html",{'name':'universal','page':"this is written by using views"})
# def render_2(req):
#     name="life is v.beautiful"
#     return render(req,"p1.html",{'name':name})
# def render_3(req):
#     id=101
#     tittle="My own page"
#     message="They gives you more comfortable in this page "
#     return render(req,"p1.html",{'id':id,'tittle':tittle,'message':message})
# def render_4(req):
#     l1=[10,20,30,40]
#     l2=[105,344,555,666]
#     return render(req,"p1.html",{'list1':l1 ,'list2':l2})
# def render_5(req):
#     d1={'id':101,'name':'ashu','age':23}
#     return render(req,"p1.html",{'dict':d1})
def renderpage2(req):
    return render(req,"home.html")
def Savedata(req):
    name=req.GET['name']
    age=req.GET['age']
    mobile=req.GET['mobile']
    address=req.GET['address']
    conn=MySQLdb.connect('localhost','root','','python3')
    query="insert into student(s_name,s_age,s_mobile,s_address)value('{}',{},{},'{}')".format(name,age,mobile,address)
    cur=conn.cursor()   
    cur.execute(query)
    conn.commit()
    cur.close() 
    conn.close()
    return HttpResponse("<center style='color:red' 'background-color:yellow'>save your records.......👍👍👍👍👍👍👍</b></center>")
def Viewallrecord(req):
    conn=MySQLdb.connect('localhost','root','','python3')
    query="select*from student"
    cur=conn.cursor()
    cur.execute(query)
    data=cur.fetchall()
    return render(req,"Viewallrecord.html",{'data':data})
def searchdata(req):
    id=req.GET['id']
    conn=MySQLdb.connect('localhost','root','','python3')
    query="select*from student where s_id={}".format(id)
    cur=conn.cursor()
    cur.execute(query)
    data=cur.fetchone()
    return render(req,"edit.html",{'data':data})

def updatedata(req):
    id=req.GET['id']
    name=req.GET['name']
    age=req.GET['age']
    mobile=req.GET['mobile']
    address=req.GET['address']
    conn=MYSQL.connect('localhost','root','','python3')
    query="update student set s_name='{}',s_age={},s_mobile={},s_address='{}'".format(name,age,mobile,address)
    cur=conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/Viewallrecord')

def deletedata(req):
    id=req.GET['id']
    conn=MySQLdb.connect('localhost','root','','python3')
    query="delete from student where s_id={}".format(id)
    cur=conn.cursor()
    cur.execute(query)
    conn.commmit()
    return render(req,"Viewallrecord.html")