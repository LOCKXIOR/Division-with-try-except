def division():
    a=input("Quelle est ton nombre ? : ")
    b=input("Un autre : ")
    try:
        a, b=float(a),float(b)
        print(a/b)
    except ValueError:
        print("Un vrai nombre !")
    except ZeroDivisionError:
        print("b != 0")
    else:
        print("Division effectuée avec succès.")
    finally:
        print("fin")

def div():
    try:
        a=float(input("Un nombre : "))
        b=float(input("Un autre nombre : "))
    except ValueError:
        print("Laisse tomber")
    try:
        print(a/b)
    except ZeroDivisionError:
        print("b != 0")
    else:
        print("Divison effectuée avec succès.")
    finally:
        print("fin")
        
div()