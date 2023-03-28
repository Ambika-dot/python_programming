"""
Q-14:the goal is to tokenize the following 5 sentences into words, excluding the stop words.
input:
sentences = ["a new world record was set","in the holy city of ayodhya","on the eve of diwali on tuesday",
"with over three lakh diya or earthen lamps","lit up simultaneously on the banks of the sarayu river"]
stopwords = ['for','was', 'a','the','and','to','in','on','with']
"""

sentences = ["a new world record was set",
             "in the holy city of ayodhya",
             "on the eve of diwali on tuesday",
             "with over three lakh diya or earthen lamps",
             "lit up simultaneously on the banks of the sarayu river"]
stopwords = ['for','was', 'a','the','and','to','in','on','with']
result=[]
for sentence in sentences:
    row_data=[]
    for word in sentence.split():
        if word not in stopwords:
            row_data.append(word)
    result.append(row_data)
print(result)

#list comprehension
print([[word for word in sentence.split() if word not in stopwords]for sentence in sentences])

