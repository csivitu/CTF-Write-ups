import requests


url = 'http://very.uniquename.xyz:2095'
flags = ['c29tZXRpbWVzIHRoZSBrZXkgdG8gdW5sb2NraW5nIHRoZSBhbnN3ZXIgaXMgdGhlIHF1ZXN0aW9uIGl0c2VsZi4uLiBidXQgbXkgZmF2b3JpdGUgaXMgY2hvY28gY2hpcA==']


while (flags[-1]!='EOF'):
    x = requests.get(url, cookies={'flag': flags[-1]}).text
    flags.append(x[9:-3 ])

for i in flags[1:-1]:
    print(i)