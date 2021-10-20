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
pw ="1moreyearofschool"
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
	# print(args.question_no)		# Uncomment to debug

	if args.parameter:
		# print(args.parameter)		# Uncomment to debug
		param=(args.parameter)

	# Create a cursor object to manipulate database.
	mycursor = mydb.cursor(buffered=True);

	# Creates a second cursor to manipulate Question #3.
	mycursor2 = mydb.cursor(buffered=True);

	# --------------------------------------------------------------------------------------------------------
	# This section will contain "Parametrized queries", where the queries
	# are saved as specific strings and the values are inserted at
	# execution time.
	# --------------------------------------------------------------------------------------------------------

	# Question 1: Find the sites that are on a given street (i.e. the address contains
	# the street name, case insensitive). Show the detailed information of each site.
	if args.question_no==1:
		sql="SELECT * FROM Site WHERE address = %s;"
		answer=(param,)
		mycursor.execute(sql,answer)
	

	# Question 2: Find the digital displays with a given scheduler system. Show their serial nos, 
	# model nos, and the names of technical supports who specialize their models. The scheduler system
	# should be a parameter input through the main program.
	if args.question_no==2:
		sql="SELECT serialNo, Specializes.modelNo, name FROM DigitalDisplay NATURAL JOIN TechnicalSupport NATURAL JOIN Specializes WHERE schedulerSystem = %s;"
		answer=(param,)
		mycursor.execute(sql,answer)


	# Question 3: List the distinct names of all salesmen and the number of salesmen with that name. The output 
	# should be in the ascending order of the salesmen name. If multiple salesmen have the same name, 
	# show all the attribute values for those salesmen.
	if args.question_no==3:
		# First sql query.
		sql = "SELECT DISTINCT S.name, COUNT(S.name) AS cnt FROM Salesman AS S GROUP BY S.name ORDER BY S.name ASC;"
		
		# Separate the first set of results row by row.
		mycursor.execute(sql)
		row = mycursor.fetchone()

		while row is not None:
			if (row[1] == 1):
				print(row)
				row = mycursor.fetchone()
			else:
				name_param = str(row[0])
				# Create a second SQL query to get names.
				query = "SELECT Sa.* FROM Salesman AS Sa WHERE Sa.name = "
				sql2 = query + "'" + name_param + "';"
				mycursor2.execute(sql2)
				second_results = mycursor2.fetchall()
				
				for x in second_results:
					print (row, ", ", x, ", ", end = "")
				
				print (" ")
				row = mycursor.fetchone()

	
	# Question 4: Find the clients with a given phone no. The phone no should be a parameter input 
	# through the main program.
	if args.question_no==4:
		answer=(param,)
		sql="SELECT * from Client where phone = '%s;';"
		mycursor.execute(sql, answer)


	# Question 5: Find the total working hours of each administrator. Display the administrators’ 
	# employee ids, names, and total working hours in ascending order of the total working hours. 
	if args.question_no==5:
		sql="SELECT empId, name, SUM(hours) AS total FROM AdmWorkHours NATURAL JOIN Administrator GROUP BY empId , name ORDER BY SUM(hours) ASC;" 
		mycursor.execute(sql)
	

	# Question 6: Find the technical supports that specialize a specified model. Display the names 
	# of those technical supports. The specified model no should be a parameter input through 
	# the main program.
	if args.question_no==6:
		answer=(param,)
		sql="SELECT tech.name FROM TechnicalSupport as tech, Specializes as spec WHERE spec.modelNo = '%s' AND tech.empID = spec.empID;" 
		mycursor.execute(sql, answer)


	# Question 7: Order the salesmen with descending order of their average commission rates. 
	# Display each salesman’s name and the average commission rate.
	if args.question_no == 7:
		sql = "SELECT S.name, AVG(P.comissionRate) AS Avg_CommissionRate FROM Salesman AS S NATURAL JOIN Purchases AS P GROUP BY P.empId ORDER BY AVG(P.comissionRate) DESC;"
		mycursor.execute(sql)


	# Question 8: Calculate the number of administrators, salesmen, and technical supports. 
	# Display the results in the following format.
	#		Role				cnt
	#		------------------
	#		Administrator		10
	#		Salesmen			40
	#		Technicians			20
	if args.question_no==8:
		sql="SELECT 'Administrator' AS Role, COUNT(DISTINCT Adm.empId) AS cnt FROM Administrator AS Adm UNION SELECT 'Salesmen' AS Role, COUNT(DISTINCT S.empId) FROM Salesman AS S UNION SELECT 'Technicians' AS Role, COUNT(DISTINCT T.empId) FROM TechnicalSupport AS T;" 
		mycursor.execute(sql)

	# --------------------------------------------------------------------------------------------------------
	# End of "Parametrized queries".
	# --------------------------------------------------------------------------------------------------------


	# Cursor object has a fetchall() method to fetch all the records present 
	# in the results table.
	myresults=mycursor.fetchall()

	for x in myresults:
		print (x)
	
	# At the end, we need to make sure to close the cursor and the database connection.
	if(mydb.is_connected()):
		mydb.close()
		mycursor.close()
		mycursor2.close()
		print("MySQL database connection is closed.")
	
if __name__=="__main__":
	main()
