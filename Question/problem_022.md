Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
- Mat size must be **N X M**. ( **N** is an odd natural number, and **M** is **3** times **N**.)
- The design should have 'WELCOME' written in the center.
- The design pattern should only use |, . and - characters.

**Sample Designs**
```python
Size: 7 x 21 
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------

Size: 11 x 33
---------------.|.---------------
------------.|..|..|.------------
---------.|..|..|..|..|.---------
------.|..|..|..|..|..|..|.------
---.|..|..|..|..|..|..|..|..|.---
-------------WELCOME-------------
---.|..|..|..|..|..|..|..|..|.---
------.|..|..|..|..|..|..|.------
---------.|..|..|..|..|.---------
------------.|..|..|.------------
---------------.|.---------------
```

**Input Format**  
A single line containing the space separated values of **N** and **M**.

**Constraints**
- **5 &lt; N &lt; 101**
- **15 &lt; M &lt; 303**

**Output Format**  
Output the design pattern.

**Sample Input**
```python
9 27
```

**Sample Output**
```python
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
```