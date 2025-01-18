import re

for i in logs:
    if 500 in str(i).rfind(500):
        print(i)