users=["kjhbgvc","lkjhgc","kjhgfdx"]
password =("kjhgc","kjhg","oiuygfc")

# check= zip(users,password)
# check= list(zip(users,password))
check= dict(zip(users,password))
print(type(check))
for key,value in check.items():
    print(key +":" + value)