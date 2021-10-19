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
order by total asc