from mimetypes import init


class Atm:
    def __init__(self,cardNumber,pin) :
        self.cardNumber=cardNumber
        self.pin=pin
    def check_balance(self):
        print('Your balance is 50000')
    def withdrawl(self,amount):
        new_amount = 50000-amount
        print("you have withdrawn "+ str(amount)+". Your Remaining balance is"+str(new_amount))
     