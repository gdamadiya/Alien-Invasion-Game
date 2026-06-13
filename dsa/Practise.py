import re

test= 'hello python'

modified=re.sub(r'\s','_',test)
print(modified)
