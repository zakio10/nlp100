import pandas as pd


df = pd.read_csv('popular-names.txt', sep='\t', header=None)

names = df[0].unique()

print(len(names)) # 136
print(names)
'''
['Mary' 'Anna' 'Emma' 'Elizabeth' 'Minnie' 'Margaret' 'Ida' 'Alice'
 'Bertha' 'Sarah' 'John' 'William' 'James' 'Charles' 'George' 'Frank'
 'Joseph' 'Thomas' 'Henry' 'Robert' 'Annie' 'Edward' 'Clara' 'Florence'
 'Ethel' 'Bessie' 'Harry' 'Helen' 'Ruth' 'Marie' 'Lillian' 'Mildred'
 'Dorothy' 'Frances' 'Walter' 'Evelyn' 'Virginia' 'Richard' 'Betty'
 'Donald' 'Doris' 'Shirley' 'Barbara' 'Patricia' 'Joan' 'Nancy' 'Carol'
 'David' 'Ronald' 'Judith' 'Linda' 'Sandra' 'Carolyn' 'Sharon' 'Michael'
 'Susan' 'Donna' 'Larry' 'Kathleen' 'Deborah' 'Gary' 'Karen' 'Debra'
 'Pamela' 'Cynthia' 'Mark' 'Steven' 'Lisa' 'Jeffrey' 'Lori' 'Kimberly'
 'Tammy' 'Angela' 'Michelle' 'Jennifer' 'Melissa' 'Christopher' 'Brian'
 'Amy' 'Laura' 'Tracy' 'Julie' 'Jason' 'Scott' 'Stephanie' 'Heather'
 'Nicole' 'Matthew' 'Rebecca' 'Jessica' 'Amanda' 'Daniel' 'Kelly' 'Joshua'
 'Crystal' 'Ashley' 'Megan' 'Brittany' 'Andrew' 'Justin' 'Samantha'
 'Lauren' 'Emily' 'Brandon' 'Tyler' 'Taylor' 'Nicholas' 'Jacob' 'Hannah'
 'Austin' 'Alexis' 'Rachel' 'Madison' 'Abigail' 'Olivia' 'Ethan' 'Anthony'
 'Isabella' 'Ava' 'Sophia' 'Chloe' 'Alexander' 'Mia' 'Jayden' 'Noah'
 'Aiden' 'Mason' 'Liam' 'Charlotte' 'Harper' 'Benjamin' 'Elijah' 'Amelia'
 'Logan' 'Oliver' 'Lucas']
 '''