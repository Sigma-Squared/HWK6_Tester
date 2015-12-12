#HWK6 Tester
Randomly generates epressions and tests your program with them.
#Usage (Requires Python 3)
UNIX-like *(NOTE: I haven't tried this on UNIX-like systems so I'm not sure if the subprocess stuff will work)*
```
$ python3 AutoTester.py num_testcases path_to_executable > outputfile.txt (optional)
```
Windows
```
py -3 AutoTester.py num_testcases path_to_executable > outputfile.txt (optional)
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
```
