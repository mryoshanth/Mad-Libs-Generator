import random
again = True

def random_noun():
    random_num = random.randint(0, 1)
    if random_num == 0:
        return noun[0]
    else:
        return noun[1]

def random_adjec():
    random_num = random.randint(0, 1)
    if random_num == 0:
        return adjec[0]
    else:
        return adjec[1]

def random_verb():
    random_num = random.randint(0, 1)
    if random_num == 0:
        return verb[0]
    else:
        return verb[1]


def process_string(madlib):
    pre_process = newline(madlib.split())
    for index, word in enumerate(pre_process):
        if word == "NOUN":
           pre_process[index] = random_noun()
        elif word == "ADJEC":
            pre_process[index] = random_adjec()
        elif word == "VERB":
            pre_process[index] = random_verb()
    return " ".join(pre_process)

def newline(list):
    full_list = len(list)
    start_list = 0
    sub_list = 12
    while start_list <= full_list:
        list.insert(sub_list, "\n")
        start_list += sub_list
        sub_list += sub_list
    return list


while again:
    noun_taken = 0
    adjec_taken = 0
    verb_taken = 0
    noun = []
    adjec = []
    verb = []
    while noun_taken < 2:
        print("Give me a noun (example: man, woman, car, toys)")
        user_input = input()
        noun.append(user_input)
        noun_taken += 1
    while adjec_taken < 2:
        print("Give me an adjective (example: tall, dark, blue, soft)")
        user_input = input()
        adjec.append(user_input)
        adjec_taken += 1
    while verb_taken < 2:
        print("Give me a verb that ends with -ing (example: working, running, sleeping, drinking)")
        user_input = input()
        verb.append(user_input)
        verb_taken += 1

    print("\nHere's a Mad Libs story for you..")
    print("    ")

    story = ("Post WW2, NOUN humbled themselves and started VERB harder. They focused their effort on developing NOUN \n"
             "that had ADJEC features. Japan's rise through VERB is a ADJEC and memorable one.")
    print(process_string(story))

    print("\nWanna have another go?")
    again = ("y" or "yes") in input().lower()