def checkPassiveOrActive(sentence):
    x = sentence.lower().split()
    check_list = ["be","am","is","was","were","am","been"]
    for i in check_list:
        if i in x:
            return print("This sentence is most likely passive!")
    return print("This sentence is most likely active!")

checkPassiveOrActive("My teacher gave me instructions")