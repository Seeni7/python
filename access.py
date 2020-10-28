# %%
import re
f = open("access.2020-08-12_1900.log","r")
text = f.read()
ip  = re.findall( r'[0-9]+(?:\.[0-9]+){3}',text)
byte = re.compile(r'(\d+$)')
get  = re.compile(r'(\d"GET)')
print(text)


# %%
