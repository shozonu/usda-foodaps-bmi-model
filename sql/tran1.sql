-- Filter out rows with these columns
-- that contain error flags.
SELECT * FROM t1
WHERE bmi > 0
AND bmi != 'V'
AND bmicat != 'V'
AND bmicat != 'E'
AND healthstatus != 'D'
AND healthstatus != 'R'
AND ndinnersout != 'D'
AND ndinnersout != 'R';