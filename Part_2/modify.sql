#*******************************************************************************
#
#	Project: Part 2
#	Team: Matt Horrocks, Nasley Chumacero-Martin, Kashka Calvin
#	CS482 Database Management Systems I
#
#	Description: These SQL statements modify the existing information for
#				database abc_media_db, which was created and populated with
#				sample entries in Project Part 1.
#
#*******************************************************************************
#use abc_media_db; # which database to use

# Change the existing information in the Salesman table.
UPDATE Salesman
SET name = 'Jesus'
WHERE name = 'Jesus Rodriguez';

UPDATE Salesman
SET name = 'Rachel'
WHERE name = 'Rachel Morris';

UPDATE Salesman
SET name = 'Stephen'
WHERE name = 'Stephen Cole';

UPDATE Salesman
SET name = 'Michael'
WHERE name = 'Michael Dyman';

UPDATE Salesman
SET name = 'Chris'
WHERE name = 'Chris Valencia';

# Add new values to Salesman table to test.
INSERT INTO Salesman
VALUES (457, 'Stephen', 'M');

INSERT INTO Salesman
VALUES (653, 'Mary', 'F');

INSERT INTO Salesman
VALUES (79, 'Mary', 'F');

INSERT INTO Salesman
VALUES (186, 'Taylor', 'F');

INSERT INTO Salesman
VALUES (22, 'Michael', 'M');

INSERT INTO Salesman
VALUES (553, 'Michael', 'M');

INSERT INTO Salesman
VALUES (771, 'Michael', 'M');

INSERT INTO Salesman
VALUES (300, 'Taylor', 'M');