def calculate_sigfigs(n):
    """
    Calculate the number of Significant Figures in a given value. Accurate up to 25 characters

    """
    digits = ("1","2","3","4","5","6","7","8","9")
    n = str(format(n,'n'))
    print(n)
    if "0" not in n:
        if "." in n:
            #e.g. 15.
            n = n.replace(".", "")
            print(int(n.count(""))-1)
        else:
            #e.g. 11
            print(int(n.count(""))-1)
    elif "0" in n:
        if "." in n:
            if n.endswith("0") and n.startswith(digits):
                #e.g. 150.0
                n = "".join(reversed(n))
                n = n.replace("0","",1)
                n = n.replace(".","")
                n = "".join(reversed(n))
                print(int(n.count(""))-1)
            elif n.startswith("0") and n.endswith(digits):
                n = n.replace("0","",1)
                n = n.replace(".","")
                print(n)
                while n.startswith("0"):
                    n = n.replace("0","",1)
                    print(n)
                print(int(n.count(""))-1)
            elif n.startswith("0") and n.endswith("0") and digits in n:
                n = n.replace("0","",1)
                n = n.replace(".","")
                while n.startswith("0"):
                    n = n.replace("0","",1)
                print(int(n.count(""))-1)
        else:
            #e.g. 1500
            n = n.replace("0", "")
            print(int(n.count(""))-1)

calculate_sigfigs(0.0000401)
