def ui(title) :
    if len(title) % 2 == 0 :
        print(f"{ title }".center(30, "="))
        
    else :
        print(f"{ title }".center(29, "="))
        

def sep(sign, amount):
    print(sign * amount)



def menu(*args):
    for num, item in enumerate(args, start=1)  :
        print(f"{num}. {item}")


def get_int():
    try :
        return int(input("Choose a number: ").strip())

    except ValueError:
        print("Invalid input")