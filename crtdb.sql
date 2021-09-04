#*******************************************************************************#
#	                                                                           	#
#	Project: Part 1																#
#	Team: Mari Langford-Pavao, Nasley Chumacero-Martin, Matt Horrocks			#
#	CS482 Database Management Systems I											#
#	                                                                            #
#	Description:	This file creates an SQL database with the required tables,	#
#					foreign keys, and value constraints. The schema for this	#
#					database is in the Project Part 1 documents for a 			#
#					fictional company named ABC Media.							#
#																				#
#*******************************************************************************#

# Step One: The schema has to be defined so that tables can be inserted.
CREATE SCHEMA abc_media_db;

# Step Two: Create the database tables with the specific rows as described in
#           the project documentation.

# Table 1: Create a table with two rows for Video. Neither row can be empty.
#          Video (videoCode: integer, videoLength: integer)
CREATE TABLE  Video(
  videoCode INT(10),
)

# Table 2: Create a table with 6 rows for Model. None of the rows should be
#         allowed to be empty.
# Model (modelNo: char(10), width: numeric (6,2), height: numeric (6,2),
# weight: numeric (6,2), depth: numeric (6,2), screenSize: numeric (6,2))

# Step Three: TBD
