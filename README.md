#HWK6 Tester
Randomly generates epressions and tests your program with them.
#Usage (Requires Python 3)
UNIX-like *(NOTE: I haven't tried this on UNIX-like systems so I'm not sure if the subprocess stuff will work)*
```
$ python3 AutoTester.py <num testcases> <path to executable> > <output file> (optional)
```
Windows
```
py -3 AutoTester.py <num testcases> <path to executable> > <output file>  (optional)
```
###Sample Output:
```
-----------------------------------------
Test # 18
Expression:	 26+(43+(46))*(27)/(2*33/45)
Program Answer:	 1664.41
Correct Answer:	 1664.41
PASS
-----------------------------------------
Test # 19
Expression:	 12/(32)+24/17/(21*(11)*29)+1
Program Answer:	 9457.64
Correct Answer:	 1.38
FAIL! Extreme error of 9456.26 detected
-----------------------------------------
Test # 20
Expression:	 3/(25*(26/(44-(16/(21))*9/29/(47))*(13)))+(15)
Program Answer:	 15.01
Correct Answer:	 15.02
PASS, WARNING! 0.009999999999999787 error detected
-----------------------------------------
```
