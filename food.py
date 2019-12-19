from pyDatalog import pyDatalog

pyDatalog.clear()

pyDatalog.create_terms('food, asian, eastern, western, rice, noodle, has soup, no soup, X')

food(X) <= asian(X)
food(X) <= eastern(X)
food(X) <= western(X)

+ asian('rice')
+ asian('noodle')
+ eastern('kebab')

print("asian :",pyDatalog.ask('asian(X)').answers)