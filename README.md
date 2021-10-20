# sqlBD_ABC_media
## This program is a Project for CS 482 at NMSU. 

### Part 1
Part 1 of the Project relies on creating an SQL database for a fictional company named ABC Media, and also populates it with sample data.
The SQL file crtdb.sql should be run first to create the database "abc_media_db". Then running the SQL file insdb.sql populates the tables
with sample data in order to test queries. Part1_Description.pdf contains the schema design and required constraints, so this document should be
checked for database requirements.

### Part 2
Part 2 of the Project relies on creating a Python program that connects to the SQL database created in Part 1.
The SQL file modify.sql shoud be run before running the Python program because it modifies the existing tables in such a way
that the new queries will produce the desired test results. The test.sql file contains test queries that were first tested
directly in SQL, then added to the Python program.

The project description Part2_Description.pdf, contains the 8 queries that need to be solved within the Python program.
The Python program (project2.py) should be run from the command line with the question number 1-8 and a parameter for specific questions.
The list below specifies which question numbers require a parameter in addition to the question number:
- python project2.py 1 <param_street_name>
- python project2.py 2 <param_scheduler_system>
- python project2.py 3
- python project2.py 4 <param_phone_no>
- python project2.py 5
- python project2.py 6 <param_model_no>
- python project2.py 7
- python project2.py 8
Note: The program hard codes the SQL database connection, as well as parametrizes specific SQL queries. In this manner, we can help protect
from SQL injection.
