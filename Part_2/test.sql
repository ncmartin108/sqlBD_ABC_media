use abc_media_db;

select * from Site where address = '34882 Gleichner Circle';

SELECT 
    serialNo, Specializes.modelNo, name
FROM
    DigitalDisplay
        NATURAL JOIN
    TechnicalSupport
        NATURAL JOIN
    Specializes
WHERE
    schedulerSystem = 'smart';
    
select empId, name, sum(hours) as total
from AdmWorkHours natural join Administrator
group by empId, name
order by total asc;

# Question 3: List the distinct names of all salesmen and the number of salesmen with that name. The output should be in the 
# ascending order of the salesmen name. If multiple salesmen have the same name, show all the attribute values for those salesmen. 
# For instance, if the Salesman relation contains the following 4 records
# (1, ’Peter’, ’M’), (2, Mary, ’F’), (3, ’John’, ’M’), (4, Mary, ’F’).
# The output should be:
# Name 				cnt
# ------------------
# John 1
# Mary 2 (2,Mary,’F’),(4,Mary,’F’) 
# Peter 1
SELECT DISTINCT S.name, COUNT(S.name) AS cnt
FROM Salesman AS S
GROUP BY name
ORDER BY name ASC;
