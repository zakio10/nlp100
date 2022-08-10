import random
random.seed(0)

# s = input(">")
s = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

s = [_ if len(_) <= 4 else _[0] + "".join(random.sample(_[1:-1], len(_)-2)) + _[-1] for _ in s.split(" ")]

print(s)