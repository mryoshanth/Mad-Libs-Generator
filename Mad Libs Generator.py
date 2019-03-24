import random
again = True

def random_noun():
    ran_noun = random.choice(noun)
    pos = noun.index(ran_noun)
    str_noun = str(noun.pop(pos))
    return str_noun

def random_adjec():
    ran_adjec = random.choice(adjec)
    pos = adjec.index(ran_adjec)
    str_adjec = str(adjec.pop(pos))
    return str_adjec


def random_verb():
    ran_verb = random.choice(verb)
    pos = verb.index(ran_verb)
    str_verb = str(verb.pop(pos))
    return str_verb


while again:
    noun_taken = 0
    adjec_taken = 0
    verb_taken = 0
    noun = []
    adjec = []
    verb = []
    while noun_taken < 2:
        print("Give me a noun (example: man, woman, car, toys)")
        user_input = input().lower()
        noun.append(user_input)
        noun_taken += 1
    while adjec_taken < 2:
        print("Give me an adjective (example: tall, dark, blue, soft)")
        user_input = input().lower()
        adjec.append(user_input)
        adjec_taken += 1
    while verb_taken < 2:
        print("Give me a verb that ends with -ing (example: working, running, sleeping, drinking)")
        user_input = input().lower()
        verb.append(user_input)
        verb_taken += 1

    print("\nHere's a Mad Libs story for you..")
    print("    ")

    story = ("Post WW2, "+random_noun()+" humbled themselves and started "+random_verb()+" harder. They focused their effort on developing \n"+random_noun()+
                " that had "+random_adjec()+" features. Japan's rise through "+random_verb()+" is a "+random_adjec()+" and memorable one.")
    print(story)

    print("\nWanna have another go?")
    again = ("y" or "yes") in input().lower()

print("Good game, see ya!")