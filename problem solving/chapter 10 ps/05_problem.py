from random import randint


class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo

    def bookticket(self , fro , to ):
        print(f"Your ticket is booked in Tran no : {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"Train no : {self.trainNo}is runing on time")
        

    def  getFare(self, fro , to ):
        print(f"Ticket fare in train no : {self.trainNo} from {fro} to {to} is {randint(162,1615)}")




person = Train(1615)

person.bookticket("Delhi","pahad")
person.getstatus()
person.getFare("Delhi","pahad")