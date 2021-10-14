import mysql.connector # import connector

#make connection to db, change to your local info
pw="1moreyearofschool"
mydb = mysql.connector.connect(
	host ="localhost",
	user ="root",
	password =pw,
	database ="abc_media_db"
	)

def main():
	#args = sys.argv[1:]
	#args list 
	mycursor = mydb.cursor();

	sql="select * from Site where address = '34882 Gleichner Circle';"
	#sql1="select * from Site where address = %s;"
	#addr=('34882 Gleichner Circle')
	#addr=input("Enter address to search for in sites: ")
	
	mycursor.execute(sql)
	#mycursor.execute(sql1,addr)

	myresults=mycursor.fetchall()

	for x in myresults:
		print (x)

	if(mydb.is_connected()):
		mydb.close()
		mycursor.close()
		print("mysql connection is closed.")
	
if __name__=="__main__":
	main()
