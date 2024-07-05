

#My Tarot Reader App


# from the CCodeCademy IE, 
# I added the random num gens to come up wiuth a different pair geach time. 
# need to add:
# - Basic definitons of each card to give a 'reading' when 3 cards are drawn
# - Advanced Definitions of each card when paired/combined with other cards (why does it matter if these cards are matched)


import random


tarot = {
    1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"
    }

selection = random.sample(list(tarot.keys()), 3)
spread = {"past": tarot.pop(selection[0]), "present": tarot.pop(selection[1]),"future": tarot.pop(selection[2])}


print(spread)

for read, card in spread.items():
    print(f"Your", read, "is the", card, "card.")






#### MOOT CODE ####
# Generates random number from the tarot list to be used as the selected card. 
##rand_num_past = random.choice(list(tarot.keys()))
##rand_num_present = random.choice(list(tarot.keys()))
##rand_num_future = random.choice(list(tarot.keys()))


# fixes Key Error, if a selected tarot list number would be the same as a previous 
##while rand_num_present == rand_num_past:
    ##rand_num_present = random.choice(list(tarot.keys()))

##while rand_num_future == rand_num_past or rand_num_future == rand_num_past:
    ##rand_num_future = random.choice(list(tarot.keys()))

##spread["past"] = tarot.pop(rand_num_past)
##spread["present"] = tarot.pop(rand_num_present)
##spread["future"] = tarot.pop(rand_num_future) 
