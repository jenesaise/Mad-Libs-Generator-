#Build a program that takes user input and generates a funny story. This is great for practicing string manipulation.


#print("Make Sure That All Nouns And Verbs Enterred Are Related To A Fairy-Like Theme. ")
#noun1 = input("Enter A Noun To Describe Fairies = ")
#noun2 = input("Enter A Noun To Decribe Fairies =  ")
#verb2 = input("Enter A Verb To Describe Fairies = ")
#verb3 = input("Enter A Verb To Describe Fairies = ")
#noun3 = input("Enter A Noun To Describe Fairies = ")
#Madlib = f"Fairies are {noun1} mythical creatures. They have {noun2} which enable them to {verb2} around.They {verb3} their fairy-dust every where they go. A {noun3} fairy is tinkerbell."
#print(Madlib)


#import random
#print("Story For Fairies!")
#ChoiceNoun = "Beautiful", "Wings", "Dreamy", "Mythical", "Sparkly", "Twinkling", "Fluttery", "Shimmery", "Tinkering"
#ChoiceVerb = "Enchanted", "Playful", "Glowy", "Glide", "Glisten", "Divine" , "Heavenly", "Heaven Sent"
#Computer = [""] * 8
#while True:
    #for index in range(0, 8):
        #if index % 2 == 0:
            #Computer[index] = random.choice(ChoiceNoun)
        #else:
            #Computer[index] = random.choice(ChoiceVerb)
    
    #if len({Computer[0], Computer[1], Computer[3], Computer[5]}) == 4 and len({Computer[2], Computer[4], Computer[6], Computer[7]}) == 4:
        #break
#Madlib = f"In a {Computer[0]} glade, {Computer[1]} fairies with fluttery wings {Computer[2]} through the {Computer[3]} air. Their mythical forms, sparkly and {Computer[4]}, glisten as they {Computer[5]} with enchanted flowers, creating a {Computer[6]} and {Computer[7]} scene."
#print(Madlib) 


import random
print("Story For Fairies!")
ChoiceNoun = "Beautiful", "Wings", "Dreamy", "Mythical", "Sparkly", "Twinkling", "Fluttery", "Shimmery", "Tinkering"
ChoiceVerb = "Enchanted", "Playful", "Glowy", "Glide", "Glisten", "Divine" , "Heavenly", "Heaven Sent"
while True:
    Computer1 = random.choice(ChoiceNoun)
    Computer2 = random.choice(ChoiceNoun)
    Computer3 = random.choice(ChoiceVerb)
    Computer4 = random.choice(ChoiceNoun)
    Computer5 = random.choice(ChoiceVerb)
    Computer6 = random.choice(ChoiceNoun)
    Computer7 = random.choice(ChoiceVerb)
    Computer8 = random.choice(ChoiceVerb)

    if len({Computer1, Computer2, Computer4, Computer6}) == 4 and len({Computer3, Computer5, Computer7, Computer8}) == 4:
        break
Madlib = f"In a {Computer1} glade, {Computer2} fairies with fluttery wings {Computer3} through the {Computer4} air. Their mythical forms, sparkly and {Computer5}, glisten as they {Computer6} with enchanted flowers, creating a {Computer7} and {Computer8} scene."
print(Madlib)