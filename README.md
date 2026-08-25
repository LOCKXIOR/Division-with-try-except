# Division-with-try-except
A small Python script experimenting with division and basic error handling.

## Division with try/except — March 2026

I made this tiny script while I was learning how `try/except` works in Python.
At the time, I didn’t fully understand how exceptions affected variable assignment,
so the code still contains the original UnboundLocalError I ran into. I decided to
leave it exactly as it was because it reflects my real learning process.

This was just a small experiment: I wanted to divide two numbers and see how Python
reacted when something went wrong (invalid input, division by zero, etc.).
It wasn’t meant to be perfect — just a simple test I wrote one evening.

## Improvements (Newer code)

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
    except (ZeroDivisionError, UnboundLocalError):
        print("b != 0 et n'utilise pas de virgule !!!")
    else:
        print("Divison effectuée avec succès.")
    finally:
        print("fin")
        
div()

