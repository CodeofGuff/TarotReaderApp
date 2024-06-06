

#My Tarot Reader App


# from the CCodeCademy IE, 
# I added the random num gens to come up wiuth adifferen tpairn geach time. 
# need to add:
# - Basic definitons of each card to give a 'reading' when 3 cards are drawn
# - Advanced Definitions of each card when paired/combined with other cards (why does it matter if these cards are matched)


import random


tarot = {
    1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"
    }

rand_num_past = random.choice(list(tarot.keys()))
rand_num_present = random.choice(list(tarot.keys()))
rand_num_future = random.choice(list(tarot.keys()))

spread = {}

spread["past"] = tarot.pop(rand_num_past)
spread["present"] = tarot.pop(rand_num_present)
spread["future"] = tarot.pop(rand_num_future)
print(spread)

for read, card in spread.items():
    print(f"Your", read, "is the", card, "card.")
