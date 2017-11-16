/* You are the chairman of your university's drawing club, which isn't doing very well right now. The club meets two times a week to exchange drawing advice, talk about new techniques, and draw something together. But the members are starting to get bored during these meetings, so you've decided to add an additional activity to the routine.

In order to do this, you decided to collect information about the students, which is now stored in the table people_interests, which has the following columns:

name - the unique name of a person;
interests - the set of interests or hobbies this person has, given as a comma-joined string. This column has datatype set('reading','sports','swimming','drawing','writing','acting','cooking','dancing','fishkeeping','juggling','sculpting','videogaming').

This information gave you the idea that reading might be an interesting theme for the next meeting, so you announced that the next meeting will be reading-related. Now you're interested in the number of members that will come.

Given the people_interests table, find the people who will attend the next meeting, i.e. those who are fond of both drawing and reading. The resulting table should consist of a single name column, and the records should be sorted by people's names.

Example

For the following table people_interests

+--------+-----------------------------------------------------+
| name   | interests                                           |
+--------+-----------------------------------------------------+
| August | cooking,juggling                                    |
+--------+-----------------------------------------------------+
| Buddy  | reading,swimming,drawing,acting,dancing,videogaming |
+--------+-----------------------------------------------------+
| David  | juggling,sculpting                                  |
+--------+-----------------------------------------------------+
| Dennis | swimming,cooking,fishkeeping                        |
+--------+-----------------------------------------------------+
| James  | reading,drawing                                     |
+--------+-----------------------------------------------------+

the output should be:

+-------+
| name  |
+-------+
| Buddy |
+-------+
| James |
+-------+

Solution:
The solution is expecting and only allows a specific solution, which is looking to use the bitwise AND operator & on the set interests. So you basically have to provide the decimal equivalent of the binary equivalent placing a 1 for whichever values in the set that you want to match on. The set is given below:

reading','sports','swimming','drawing','writing','acting','cooking','dancing','fishkeeping','juggling','sculpting','videogaming'

To match on 'reading', the first  ... would need to be 000000000001 or decimal 1.
To match on 'drawing', the second ... would need to be 000000001000 or decimal 8.

000000000000 0
000000000001 1
000000000010 2
000000000011 3
000000000100 4
000000000101 5
000000000110 6
000000000111 7
000000001000 8
000000001001 9

*/

/*Solution 1*/
CREATE PROCEDURE interestClub()
    SELECT name
    FROM people_interests
    WHERE interests & 1 AND interests & 8
    ORDER BY name


