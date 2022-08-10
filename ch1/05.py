s="I am an NLPer"
ss=s.split(" ")

char_bi_gram = [s[i:i+2] for i in range(len(s)-1)]
word_bi_gram = [ss[i:i+2] for i in range(len(ss)-1)]

print(char_bi_gram)
print(word_bi_gram)

# n-gramについて
# https://mojitoba.com/2019/09/23/what-is-ngram/