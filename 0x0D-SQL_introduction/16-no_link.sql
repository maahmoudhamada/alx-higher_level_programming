-- Script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
DELETE FROM `second_table`
WHERE name = "GEORGE";

INSERT INTO `second_table` VALUES(3, "Aria", 18);
INSERT INTO `second_table` VALUES(4, "Aria", 12);

SELECT score, name FROM `second_table`
ORDER BY score DESC;
