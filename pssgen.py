import random as rn
import string as str
class generation:
    def userid():
        digi=str.digits
        punc=str.punctuation
        user=input("Enter first name of user : ").lower()
        new_rann=""
        for i in range(3):
            rann=rn.choice(digi)
            new_rann=rann+new_rann
        ranp=rn.choice(punc)
        ranno=user+ranp+new_rann
        return ranno
    def password():
        digi=str.digits
        low=str.ascii_lowercase
        upp=str.ascii_uppercase
        punc=str.punctuation
        gen=digi+low+upp+punc
        len=int(input("Enter the maximum length of password you want : "))
        new_ran=''
        for i in range(1,len+1):
            ran=rn.choice(gen)
            new_ran=ran+new_ran
        return new_ran