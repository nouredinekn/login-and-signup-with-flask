#-----------------------import-----------------------
from flask import *
import sqlite3 , requests
#-----------------------setUp-----------------------
app=Flask(__name__)
#-----------------------routes-----------------------

               #----------------------- LOGIN -----------------------
@app.route('/login',methods=['GET','POST'])
def Login():
    if request.method=='POST':
# ----------------------- SQL -----------------------
        sql=sqlite3.connect('users.db')
        cur=sql.cursor()
#----------------------- HTML FROM --------------  python  4 ever ---------
        email=request.form['email']
        password=request.form['pass']
        #print(email,password)
# ----------------------- QUERY -----------------------
        query=f"SELECT Email , Password  FROM UserData where Email='{str(email)}' and Password='{str(password)}'"
        cur.execute(query)
        rusalt=cur.fetchall()
        if len(rusalt)==0:
            return render_template ( 'Login.html',faild='email address or password is incorrect, please try again.')
        elif len(rusalt)!=0:
            cmd=f'''SELECT FullName from "UserData" WHERE Email="{str(email)}"'''
            cur.execute (cmd )
            FullName = str(cur.fetchall ()[0][0])
            return render_template('success.html',FullName=FullName)
    return render_template('Login.html')
            # -----------------------Sign Up-------------------------
@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        sql = sqlite3.connect ( 'users.db' )
        cur = sql.cursor ()
        email=request.form['email']
        password=request.form['pass']
        fullname=request.form['fullname']
        query = f"SELECT Email , Password  FROM UserData where Email='{str ( email )}'"
        cur.execute ( query )
        rusalt = cur.fetchall ()
        if len(rusalt)==0:
            insert=f'''INSERT INTO UserData VALUES("{fullname}","{email}","{password}")'''
            cur.execute( insert )
            sql.commit()
            message='''Thank You For Signing Up !'''
            return render_template ( 'SignUp.html' , message=message)

        if len ( rusalt ) != 0 :
            message = '''Email Already In Use ,Please Try Again.'''
            return render_template ( 'SignUp.html' , message=message )
    return render_template ( 'SignUp.html')

#----------------------- RUN APP -----------------------
if '__main__'==__name__:
    app.run()