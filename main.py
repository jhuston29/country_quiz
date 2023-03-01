import time, random
from datetime import datetime, timedelta

def get_final_time(added_time,current_time):
    new_time = current_time + timedelta(minutes=added_time)
    return new_time

def get_current_datetime():
    now = datetime.now()
    return now

def txt_to_list(file):
    cap_list = []
    country_file = open(file)
    for line in country_file:
        if line.startswith("#") or line.startswith("\n"):
            continue
        else:
            key,value,number = line.split("|")
            item = [key.strip(),value.strip(),number.strip()]
            cap_list.append(item)
    return cap_list

def get_current_a(answers_list,switch):
    if switch:
        current_a = answers_list[0]
        return current_a[0]
    else:
        current_a = answers_list[0]
        return current_a[1]

def check_answer(answer, guess):
    if answer == guess or answer.lower() == guess:
        return True
    else:
        return False

def divideList(list,option):
    quiz_list = list;
    if option=="North America":
        new_list = [x for x in quiz_list if '1' in x[2]]
        return new_list
    if option=="South America":
        new_list = [x for x in quiz_list if '2' in x[2]]
        return new_list
    if option=="Europe":
        new_list = [x for x in quiz_list if '3' in x[2]]
        return new_list
    if option=="Asia":
        new_list = [x for x in quiz_list if '4' in x[2]]
        return new_list
    if option=="Africa":
        new_list = [x for x in quiz_list if '5' in x[2]]
        return new_list
    if option=="Oceania":
        new_list = [x for x in quiz_list if '6' in x[2]]
        return new_list

def removeDups(list):
    no_dups = list
    new_list = [i[0] for i in list];
    oc_set = set()
    indices = []
    for idx, val in enumerate(new_list):
        if val not in oc_set:
            oc_set.add(val)
        else:
            indices.append(idx)
    for i in indices:
        no_dups.pop(i)
    return no_dups

def timer():
    current_time = time.time()
    return current_time

def getMC_choices(list,switch):
    ints = random.sample(range(1, len(list)), 4)
    if switch:
        choice1 = list[ints[0]]
        choice2 = list[ints[1]]
        choice3 = list[ints[2]]
        choice4 = list[ints[3]]
        return choice1[0], choice2[0], choice3[0], choice4[0]
    else:
        choice1 = list[ints[0]]
        choice2 = list[ints[1]]
        choice3 = list[ints[2]]
        choice4 = list[ints[3]]
        return choice1[1], choice2[1], choice3[1], choice4[1]
