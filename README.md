# Record-Breaker-GOOGLE-KICKSTART-Question-2020 (Solution using Python)

Problem
Isyana is given the number of visitors at her local theme park on N consecutive days. The number of visitors on the i-th day is Vi. A day is record breaking if it satisfies both of the following conditions:
The number of visitors on the day is strictly larger than the number of visitors on each of the previous days.
Either it is the last day, or the number of visitors on the day is strictly larger than the number of visitors on the following day.
Note that the very first day could be a record breaking day!

Please help Isyana find out the number of record breaking days.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the integer N. The second line contains N integers. The i-th integer is Vi.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the number of record breaking days.

Sample


Input
 	 
4   #Number of Cases

8   #Number of Days

1 2 0 7 2 0 2 0       #Visitors at each day

6      #Number of Days

4 8 15 16 23 42       #Visitors at each day

9      #Number of Days

3 1 4 1 5 9 2 6 5     #Visitors at each day

6      #Number of Days

9 9 9 9 9 9           #Visitors at each day


Output

Case #1: 2

Case #2: 1

Case #3: 3

Case #4: 0


  
In Sample Case #1, the bold and underlined numbers in the following represent the record breaking days: 1 2 0 7 2 0 2 0.


In Sample Case #2, only the last day is a record breaking day.


In Sample Case #3, the first, the third, and the sixth days are record breaking days.


-----------GOOD LUCK-----------


In Sample Case #4, there is no record breaking day.
