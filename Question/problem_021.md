You are given a string **S** and width **w**.  
Your task is to wrap the string into a paragraph of width **w**.

**Function Description**  
Complete the wrap function in the editor below.  
wrap has the following parameters:
- string string: a long string
- int max_width: the width to wrap to

**Returns**
- string: a single string with newline characters ('\n') where the breaks should be

**Input Format**  
The first line contains a string, **string**.  
The second line contains the width, **max_width**.

**Constraints**
- **0 &lt; len(string) &lt; 1000**
- **0 &lt; max_width &lt; len(string)**

**Sample Input 0**
```python
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
```

**Sample Output 0**
```python
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
```


