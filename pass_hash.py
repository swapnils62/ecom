from argon2 import PasswordHasher

ph=PasswordHasher()

def Hashpass(plaintex_pass:str)->str:
    return ph.hash(plaintex_pass)

def verify(userpass:str, plaintexpass:str)->str:
    return ph.verify(userpass,plaintexpass)
