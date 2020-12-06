a = 6
b = 2
try:
	print(a)
	x = a/b
	print(x)
except Exception:
	print("not possible Sir")
finally:
    print("Done")
a = 6
b = 0
try:
	x = a/b
	print(x)
except Exception:
	print("not possible Sir")	
finally:
    print("Done")






6
3.0
Done
not possible Sir
Done
