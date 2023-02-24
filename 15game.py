from os import system
from random import shuffle
# from playsound import playsound


class Puzzle:
    def __init__(self) -> None:
        self.steps=0
        self.lst=list(map(str,range(1,16)))+[" "]
        self.lst2=self.lst.copy()
        self.user=''
        self.start()

    def start(self):
        shuffle(self.lst)
        self.Print()
        while not self.tugatildi():
            self.user=input("Raqam kiriting : ")
            if self.user in self.lst2[:15]:
                self.check()
                system("clear")
                self.steps+=1
                self.Print()
        print("siz yutdingiz")
        # playsound('yutdi.wav')

    def check(self):
        i=self.lst.index(self.user)
        if i%4>0 and self.lst[i-1]==" ":
            self.lst[i],self.lst[i-1]=self.lst[i-1],self.lst[i]
            # playsound("to'g'ri.wav")
        elif i%4<3 and self.lst[i+1]==" ":
            self.lst[i],self.lst[i+1]=self.lst[i+1],self.lst[i]
            # playsound("to'g'ri.wav")
        elif i>3 and self.lst[i-4]==" ":
            self.lst[i],self.lst[i-4]=self.lst[i-4],self.lst[i]
            # playsound("to'g'ri.wav")
        elif i<12 and self.lst[i+4]==" ":
            self.lst[i],self.lst[i+4]=self.lst[i+4],self.lst[i]
            # playsound("to'g'ri.wav")
        # else:
            # playsound('xato.wav')
    def tugatildi(self):
        return self.lst2==self.lst           

    def Print(self):
        print(f"Urinishlar : {self.steps}")
        chiz="+----"*4+"+"
        print(chiz)
        for i in range(16):
            print(f"|{' '*(3-len(self.lst[i]))}{self.lst[i]}",end=' ')
            if i%4==3:
                print(f"|\n{chiz}")

Puzzle()