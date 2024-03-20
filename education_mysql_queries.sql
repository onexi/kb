-- --------------------------------------
--  SELECTION BASICS
-- --------------------------------------

SELECT  *
FROM Colleges
WHERE City='Cambridge';

--

SELECT Name AS University, 
	Students*1000 AS 'number of students'
FROM Colleges;

--

SELECT FirstName, 
	LastName,
	Birthdate,
	 TIMESTAMPDIFF(YEAR, Birthdate,now()) AS Age
FROM Students;

--

SELECT 
	Name, 
    Students * 1000 AS Population, 
    Students * 1000 * 1.2 AS ProjectedGrowth
FROM Colleges;    

-- --------------------------------------
--  WHERE CONDITIONS
-- --------------------------------------

SELECT * 
FROM Students
WHERE Region = 'TX';

--

SELECT * 
FROM Students
WHERE Region <> 'TX';

--

SELECT * 
FROM Students
WHERE BirthDate > '1990-01-01';

-- --------------------------------------
--  LOGICAL OPERATORS
-- --------------------------------------

SELECT * 
FROM Students
WHERE 
    BirthDate > '1990-01-01' AND Region = 'TX';

--

SELECT * 
FROM Students
WHERE 
   NOT (BirthDate > '1990-01-01');

--

SELECT *
FROM Students
WHERE 
    BirthDate > '1950-01-01'
    AND 
    Region = 'TX'
    AND
    City = 'Austin';

-- --------------------------------------
--  IN expr IN (value, …)
-- --------------------------------------

SELECT * 
FROM Students
WHERE Region IN ('AZ', 'TX', 'FL');

--

SELECT *
FROM Students
WHERE 
    City IN ('Austin', 'Miami', 'Chicago');

-- --------------------------------------
--  BETWEEN expr BETWEEN min AND max
-- --------------------------------------

SELECT *
FROM Students
WHERE StudentID
	BETWEEN 1 AND 5;

--

SELECT * 
FROM Students
WHERE BirthDate 
    BETWEEN '1990-01-01' AND '2000-01-01';

-- --------------------------------------
--  LIKE expr LIKE pattern
-- --------------------------------------

SELECT * 
FROM Students
WHERE FirstName LIKE  'A%';

--

SELECT * 
FROM Students
WHERE 
    Email LIKE '%gmail%'
    OR
    Phone LIKE '%541%';

-- --------------------------------------
--  REGEXP is a search pattern
-- --------------------------------------

-- A regular expression is a sequence of characters that defines a pattern to search through text    

SELECT * 
FROM Students
WHERE LastName REGEXP  'a|m|c';

-- Match last names that have an "a", or an "m", or a "c"

SELECT * 
FROM Students
WHERE LastName REGEXP  '^.{1,5}$'; 

-- Last names with 5 characters or less

SELECT * 
FROM Students
WHERE Phone REGEXP  '[(][0-9]{3}[)][[:space:]][0-9]{3}-[0-9]{4}';

-- Match phone numbers using a regular expression