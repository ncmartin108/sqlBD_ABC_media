import mysql.connector # import connector

#
#	Project: Part 2
#	Team: Kashka Calvin, Nasley Chumacero-Martin, Matt Horrocks
#	CS482: Database Management Systems I
#
#	Description: This program connects to an existing database
#	called "abc_media_db"
#


# Make connection to db, change to your local info
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
	# Create a cursor object to manipulate database.
	mycursor = mydb.cursor();

	# This section will contain "Parametrized queries", where the queries
	# are saved as specific strings and the values are inserted at
	# execution time.
	sql="select * from Site where address = '34882 Gleichner Circle';"
	#sql1="select * from Site where address = %s;"
	#addr=('34882 Gleichner Circle')
	#addr=input("Enter address to search for in sites: ")
	
	mycursor.execute(sql)
	#mycursor.execute(sql1,addr)

	# Cursor object has a fetchall() methohd to fetch all the records present 
	# in the results table.
	myresults=mycursor.fetchall()

	for x in myresults:
		print (x)
	
	# At the end, we need to make sure to close the cursor and the database connection.
	if(mydb.is_connected()):
		mydb.close()
		mycursor.close()
		print("MySQL database connection is closed.")
	
if __name__=="__main__":
	main()
