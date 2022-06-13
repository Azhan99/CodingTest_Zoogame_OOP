class Bill:
    """
    Object that contains data about Bill, such as
    total amount and period of the bill.
    """
    def __init__(self,amount,period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flat mate person who lives in the flat
    and pays a share of the Bill.
    """
    
    def __init__(self,name,days_in_house):
        self.days_in_house = days_in_house
        self.name=name

    def pays(self,bill,flatmate2):
        weight= self.days_in_house/(self.days_in_house+flatmate2.days_in_house)
        to_pay=bill.amount*weight
        return(to_pay)

class PdfReport:
    '''
    Creates a pdf file that contains data about the flatmates
    such as their names, due amount and period of the bill
    '''
    
    def __init__(self,filename):
        self.filename = filename

    def generate(self,flatemate1,flatemate2):
        pass

the_bill=Bill(amount=120,period='March 2021')
john=Flatmate(name='John',days_in_house=20)
marry=Flatmate(name='Marry',days_in_house=25)

print('John pays:', john.pays(bill=the_bill,flatmate2=marry))
print('Marry pays:', marry.pays(bill=the_bill,flatmate2=john))



