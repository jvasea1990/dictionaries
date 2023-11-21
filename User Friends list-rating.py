user={
    'username':"johny777", 
    'online':True, 
    'email':"johny777@lucky.me", 
    'rating':0,
    'friends': ['marry888', 'candy001', 'peter99']
}

# add the name of a new friend
while True:
    new_friend=input("Introduce the name of the new friend : ")
    if new_friend=="":
        break
    else:
        user['friends'].append(new_friend)
print (user['friends'])
Name_to_check=input ("Introduce the name of a friend to be verified : ")
#dacă userul există în lista de prieteni
if Name_to_check!="":
    if Name_to_check in user['friends']:
        print ("This Name exists")
    else:
        Add_friend=input("This name does not exist in your list. Would you like to add it? Yes/No :")
        if Add_friend=="Yes":
            user['friends'].append(Name_to_check)
print(user['friends'])
print()
if user['rating']>=1e9:
    
    rating=user['rating']/1e9
    print (f"You have {rating:0.1f}G likes")
elif user['rating']>=1e6:
    
    rating=user['rating']/1e6
    print (f"You have {rating:0.1f}M likes")
elif user['rating']>=1e3:
    
    rating=user['rating']/1e3
    print (f"You have {rating:0.1f}k likes")
elif user['rating']>0: 
    print(f"You have {user['rating']} likes")
else:
    print(f"You have No likes")

