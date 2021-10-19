import mysql.connector # import connector
import argparse  # Import argument parsing

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
	# Creates a parsing object.
	parser = argparse.ArgumentParser()
	# Create the positional arguments.
	# The first command line argument is for the question number.
	parser.add_argument("question_no", help="Enter the question number.", type=int, choices=range(1,9))
	# The second command line argument is for questions 1, 2, 4, 6. Nargs is the number of arguments, and
	# '?' is one (optional) argument.
	parser.add_argument("parameter", help="For questions 1, 2, 4, and 6 enter the search parameter.", nargs='?')

	args = parser.parse_args()
	print(args.question_no)

	if args.parameter:
		print(args.parameter)
		param=(args.parameter)

	# Create a cursor object to manipulate database.
	mycursor = mydb.cursor();

	# This section will contain "Parametrized queries", where the queries
	# are saved as specific strings and the values are inserted at
	# execution time.

	# Question 1: Find the sites that are on a given street (i.e. the address contains
	# the street name, case insensitive). Show the detailed information of each site.
	#sql="select * from Site where address = '34882 Gleichner Circle';"
	if args.question_no==1:
		sql="select * from Site where address = %s;"
		answer=(param,)
		mycursor.execute(sql,answer)

	if args.question_no==2:
		sql="SELECT serialNo, Specializes.modelNo, name FROM DigitalDisplay NATURAL JOIN TechnicalSupport NATURAL JOIN Specializes WHERE schedulerSystem = %s;"
		answer=(param,)
		mycursor.execute(sql,answer)

	if args.question_no==5:
		sql="SELECT empId, name, SUM(hours) AS total FROM AdmWorkHours NATURAL JOIN Administrator GROUP BY empId , name ORDER BY SUM(hours) ASC;" 
		mycursor.execute(sql)
	
	#mycursor.execute(sql)
	#mycursor.execute(sql,answer)

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
