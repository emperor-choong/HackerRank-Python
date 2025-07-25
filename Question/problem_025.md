You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, `alison heck` should be capitalised correctly as `Alison Heck`.

**a**lison **h**eck ⇒ **A**lison **H**eck

Given a full name, your task is to capitalize the name appropriately.

**Input Format**  
A single line of input containing the full name, **S**.

**Constraints**
- **0 &lt; len(S) &lt; 1000**
- The string consists of alphanumeric characters and spaces.

**Note:** in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

**Output Format**  
Print the capitalized string, **S**.

**Sample Input**
```python 
chris alan
```

**Sample Output**
```python 
Chris Alan
```