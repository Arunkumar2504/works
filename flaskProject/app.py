from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/ticket_booking', methods=['POST', 'GET'])
def ticket_booking():  # put application's code here
    cost = 1000  # The basic cost of the ticket
    return_cost = cost + 750  # This the return ticket for the travel
    # ticket = 0  # The ticket count we need
    senior_count = 0  # It is for couunting the senior citizen
    # ages = []  # Empty list for age
    price = 0  # It is for total amount
    name = request.form.get("name")
    tickets = request.form.get("no_of_tickets")
    no_of_tickets = int(tickets)
    ages = []
    age1 = request.form.get("age1")
    age2 = 23
    #print(type(age1), type(no_of_tickets))
    ages.append(int(age1))
    # ages.append(age2)
    senior_count = senior(ages, no_of_tickets, senior_count)
    return_choice = request.form.get("return_choice")
    if return_choice == "yes":
        cost = return_cost
    print(return_cost)
    print(cost)

    price = amount(cost, no_of_tickets, price)
    #print(price)
    if senior_count > 0:
        price = senior_discount(senior_count, price, cost)
        #print(price)
    if no_of_tickets == 2:
        price = discount(price)
    #print(price, name)
    return render_template('/success.html', name=name, price=price)


def senior(ages, no_of_tickets, senior_count):
    for age in range(0, len(ages)):
        if ages[age] >= 60:
            senior_count += 1
    return senior_count


def amount(cost, ticket, price):
    price = ticket * cost
    return price


def discount(price):
    price -= ((price // 10) * 2)
    return price


def senior_discount(senior_count, price, cost):
    for age in range(0, senior_count):
        price -= ((cost // 10) * 5)
    return price


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/registration')
def registration():

    return render_template('/registration.html')




if __name__ == '__main__':
    app.run()
