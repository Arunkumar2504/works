cost=1000
return_cost=cost+750
ticket=0
senior_count=0
ages=[]
price=0



def tickets(ticket):
    ticket=int(input("how many tickets you need= "))
    return ticket


def senior(ages,ticket,senior_count):
    for age in range(0,ticket):
        ages.append(int(input("ENTER YOUR AGE= ")))
    
    for age in range(0,len(ages)):
        if ages[age]>60:
            senior_count += 1
    return senior_count

def amount(cost,ticket,price):
    price=ticket*cost
    return price

def discount(price):
    price -= ((price//10)*2)
    return price


def senior_discount(senior_count,price,cost):
    for age in range(0,senior_count):
        price -=((cost//10)*5)
    return price




def train_tickets(cost,price,return_cost,ages,ticket,senior_count):
    ticket= tickets(ticket)

    senior_count= senior(ages,ticket,senior_count)

    choice=input("do you want a return ticket= ")
    if(choice=="yes"):
        cost=return_cost
    
    price= amount(cost,ticket,price)
    if(ticket>=4):
        price=discount(price)
    if(senior_count>0):
        price= senior_discount(senior_count,price,cost)
    

    print("your total bill cost= "+ str(price))


    seller_choice=input("do you want to continue the sale= ")
    if(seller_choice=="yes"):
        train_tickets(cost,price,return_cost,ages,ticket,senior_count)


train_tickets(cost,price,return_cost,ages,ticket,senior_count)










