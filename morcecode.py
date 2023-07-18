import time
from playsound import playsound

val = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.'
,'H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---',
'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--',
'X':'-..-','Y':'-.--','Z':'--..','1':'.----','2':'..---','3':'...--','4':'....-',
'5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'-----',' ': '/'}


def enc(text):
    enc_text = ""
    for letters in text:
        if letters != " ":
            enc_text = enc_text + val.get(letters) + " "
        else:
            enc_text += " "
    print(enc_text)
    # sound(enc_text)


def dec(text):
    text += " "
    kl = list(val.keys())
    vl = list(val.values())
    morse = ""
    normal = ""
    for letters in text:
        if letters != " ":
            morse += letters
            blank = 0
        else:
            blank += 1
            if blank == 2:
                normal += " "
            else:
                normal = normal + kl[vl.index(morse)]
                morse = ""
    print(normal)


a=int(input("Are you ready \npress 1\n"))
while (a==1):
    print("\n\t\tMorse code converter\n")
    ch = int(input(" 1) Encode \n 2) Decode \n 3) Exit\n\tenter choice : "))

    if ch == 1:
        ETM = input("Enter text : ").upper()
        enc(ETM)
    elif ch==2:
        MTE = input("Enter morse : ")
        dec(MTE)
    else:
        print("goodbye........!!!!")
        break