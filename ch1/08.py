from curses.ascii import islower


input_str = input(">")
input_str = "".join([chr(219 - ord(_)) if _.islower() else _ for _ in input_str])

print(input_str)

# islower()
# https://docs.python.org/ja/3/library/stdtypes.html

# encode()
# https://grapebanana.com/python-encoding-utf-8-7161/