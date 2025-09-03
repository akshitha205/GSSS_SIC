import re

s = "hello world"
match = re.search("world", s)
if match:
    print(match.start())  # 6
else:
    print(-1)