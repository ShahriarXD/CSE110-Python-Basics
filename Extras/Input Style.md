##ast.literal_eval(node_or_string)
Safely evaluate an expression node or a Unicode or Latin-1 encoded string containing a Python literal or container display. The string or node provided may only consist of the following Python literal structures: strings, numbers, tuples, lists, dicts, booleans, and None.

This can be used for safely evaluating strings containing Python values from untrusted sources without the need to parse the values oneself. It is not capable of evaluating arbitrarily complex expressions, for example involving operators or indexing.

Warning It is possible to crash the Python interpreter with a sufficiently large/complex string due to stack depth limitations in Python’s AST compiler.


```python
import ast
x = ast.literal_eval(input())
print(x)
```
