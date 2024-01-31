# #!C:/Users/shriv/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.10
# print("Content-Type:text/html")
# print()
# import cgi

# print("<h1>welcome to hostel engine</h1>")
# print("hr/")
# print("<h1>using input tag</h1>")
# print("<body bgcolor='red'>")

# form=cgi.FieldStorage()


# first=form.getvalue("first")
# last=form.getvalue("last")
# email=form.getvalue("email")
# phone=form.getvalue("phone")
# address1=form.getvalue("address1")
# address2=form.getvalue("address2")
# city=form.getvalue("city")
# country=form.getvalue("country")
# req=form.getvalue("req")



import mysql.connector as my
con=my.connect(host = "localhost",user = "root",passwd = "",database = "hostel_data")
cur=con.cursor()
# cur.execute("create table register(id,name varchar(200))")
# city=input("ENTER CITY : ")
# date=int(input("ENTER DATE(0000-00-00)=(00000000) : "))
# seater=int(input("SEATER : "))

sql="insert into register(first,last,email,phone,address1,address2,city,country,req)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(first,last,email,phone,address1,address2,city,country,req)
cur.execute(sql,val)
con.commit()
# print(con)

# print("<h3>record inserted succesfull</h3>")
