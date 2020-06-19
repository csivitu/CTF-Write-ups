# arg2

Author: [roerohan](https://github.com/roerohan)

This challenge can be solved by just reading the Python code properly.

# Requirements

- Python

# Source

- [lemon_zest.py](./lemon_zest.py)
- [Reverse Engineering](http://cyberhomectf.eastus.cloudapp.azure.com/challenges?category=reverse-engineering)

# Exploitation

```python
def main():
	auth = CheckingPasswd()
	if auth == True:
		print("so... The flag can be the password.")
		print("You deserve it!Gj")
	else:
		print("Incorrect password!")
		print("F.O.C.U.S S.T.U.P.I.D H.U.M.A.N")
		AnotherMain()
```

As you can see in the `main()` function, the `CheckingPasswd()` function is called, let's see what that does.

```python
def CheckingPasswd():
	UserWrote = input("Enter your *PASSWD*: ")
	if UserWrote[13:19] == "n6_c4n":
		if UserWrote[0:4] == "cbrh":
			if UserWrote[19:25] == "_b3_qu":
				if UserWrote[4:8] == "{r3v":
					if UserWrote[25:31] == "173_c0":
						if UserWrote[8:13] == "3r533":
							if UserWrote[31:36] == "0l_bu":
								if UserWrote[40:46] == "7_w17h":
									if UserWrote[50:54] == "h0n}":
										if UserWrote[46:50] == "_py7":
											if UserWrote[36:40] == "7_n0":
												return True	
	else:
		return False
```

It checks if a parts of the string the user enters into the `UserWrote` variable matches a certain string, and returns `True` upon success. So we could just assign `UserWrote` those strings using python. Note that the `}` is checked at index `53`, so the length of the flag must be 53.

```python
>>> UserWrote = [None]*53
>>> UserWrote[13:19] = "n6_c4n"
>>> UserWrote[0:4] = "cbrh"
>>> UserWrote[19:25] = "_b3_qu"
>>> UserWrote[4:8] = "{r3v"
>>> UserWrote[25:31] = "173_c0"
>>> UserWrote[8:13] = "3r533"
>>> UserWrote[31:36] = "0l_bu"
>>> UserWrote[40:46] = "7_w17h"
>>> UserWrote[50:54] = "h0n}"
>>> UserWrote[46:50] = "_py7"
>>> UserWrote[36:40] = "7_n0"
>>> print(''.join(UserWrote))
cbrh{r3v3r533n6_c4n_b3_qu173_c00l_bu7_n07_w17h_py7h0n}
```

That gives you the flag. The flag is:

```
cbrh{r3v3r533n6_c4n_b3_qu173_c00l_bu7_n07_w17h_py7h0n}
```