import mysql.connector # import connector

#make connection to db, change to your local info
pw="your specific password"
mydb = mysql.connector.connect(
	host ="localhost",
	user ="root",
	password =pw,
	database ="abc_media_db"
	)

mycursor = mydb.cursor();
mycursor.execute("SHOW tables;")
print (mycursor)

for x in mycursor:
	print(x)
