import random

def cardno_generator():
    card_no=''
    for i in range(16):
        a=str(random.randint(1,9))
        card_no+=a
    return card_no
def cvv_generator():
    cvv=random.randint(100,999)
    return cvv

def pin_generator():
    pin=random.randint(1000,9999)
    return pin
