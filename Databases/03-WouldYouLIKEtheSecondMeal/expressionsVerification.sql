/* You're a math teacher at an elementary school. Today you taught your class basic arithmetic operations ("+", "-", "*", "/") and now you need to give the students some homework. You have a lot of expressions in the format a <operation> b = c, where a, b, and c are some integers and operation is one of the operations given above.

Information about these expressions is stored in the table expressions, which has the structure:

id: the unique operation id;
a: an integer;
b: an integer;
operation: one of the operations given above ("+", "-", "*", or "/");
c: an integer.

The homework you're going to give is simple: For each expression, the student needs to determine whether it's correct or not, i.e. whether it's true that the expression to the left of the = sign equals c.

Since you have many students and checking all their answers manually is a lot of work, you want to streamline the process by automatically identifying all the expressions that are correct. Given the table expressions, build the resulting table as follows: The table should have the same columns as the initial table does, but it should only contain those rows that represent correct expressions. The rows should be ordered by id.

Example

For the following table expressions

+----+----+---+-----------+----+
| id | a  | b | operation | c  |
+----+----+---+-----------+----+
| 1  | 2  | 3 | +         | 5  |
+----+----+---+-----------+----+
| 2  | 2  | 3 | +         | 6  |
+----+----+---+-----------+----+
| 3  | 3  | 2 | /         | 1  |
+----+----+---+-----------+----+
| 4  | 4  | 7 | *         | 28 |
+----+----+---+-----------+----+
| 5  | 54 | 2 | -         | 27 |
+----+----+---+-----------+----+
| 6  | 3  | 0 | /         | 0  |
+----+----+---+-----------+----+

the output should be

+----+----+---+-----------+----+
| id | a  | b | operation | c  |
+----+----+---+-----------+----+
| 1  | 2  | 3 | +         | 5  |
+----+----+---+-----------+----+
| 4  | 4  | 7 | *         | 28 |
+----+----+---+-----------+----+

Explanation:

2 + 3 = 5 - correct;
2 + 3 = 6 - incorrect;
3 / 2 = 1 - incorrect;
4 * 7 = 28 - correct;
54 - 2 = 27 - incorrect;
3 / 0 = 0 - incorrect.

Solution:
*/

/*Please add ; after each select statement*/
CREATE PROCEDURE expressionsVerification()
BEGIN
    SELECT id, a, b, operation, c FROM (
        SELECT *,
        CASE
            WHEN operation = "+" AND a + b = c THEN "valid"
            WHEN operation = "-" AND a - b = c THEN "valid"
            WHEN operation = "*" AND a * b = c THEN "valid"
            WHEN operation = "/" AND a / b = c THEN "valid"
            ELSE "invalid"
        END as vtest
        FROM  expressions
        ) temp
    WHERE vtest = "valid";
END

/* Solution 2 from Codefights
CREATE PROCEDURE expressionsVerification()
BEGIN
	select * 
        from expressions
        where elt(locate(operation, "+-*/"), a+b, a-b, a*b, a/b) = c;
END

"
/*
Solution 3 from Codefights

CREATE PROCEDURE expressionsVerification()
BEGIN
	SELECT * FROM expressions
    WHERE CASE operation
        WHEN '+' THEN a + b
        WHEN '-' THEN a - b
        WHEN '*' THEN a * b
        WHEN '/' THEN a / b
      END = c
    ORDER BY id;
END


  SELECT id, IF (given_answer = correct_answer, "correct",
    			   IF(given_answer is NULL, "no answer", "incorrect")) AS checks
    FROM answers
    ORDER BY id;
*/