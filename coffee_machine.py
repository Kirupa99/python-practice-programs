from coffee_menu import final_menu, coffee_mug

class Coffeemachine:
    def print_order(self):
        print("--------Hello, Welcome to Barista Coffee House!!!-----------")
        print(coffee_mug)
        print("Check the available coffee items from the below menu ")
        print(final_menu)
        print("="*50)

    def take_order(self):
        order_list=[]
        status=True
        while status:
            order=input("Type the coffee that you need, type exit if you are done: ").title().replace(" ","_")
            if order=='Exit':
                status=False
            elif order in final_menu :
                order_list.append(order)
            else:
                print("Sorry your order doesnt exist in the menu, Please check and try again.")
        return(order_list)

    def check_sugar(self):
        sugar_num=int(input("Enter the number of sugar cubes you want in your coffee(cost of 1 sugar cube = 0.20 £): "))
        sugar_cost=sugar_num * 0.2
        return sugar_cost

    def calculate_bill(self,order_list,sugar_cost,final_menu):
        global final_bill
        total=0
        for i in order_list:
            amount=final_menu.get(i)
            total+=amount
            final_bill=sugar_cost+total
        print("Your total bill is :",round(final_bill),"£")
        print("Have a great day ahead!!! A Coffee a day keeps your headache away!!! :)")


coffeemachine=Coffeemachine()
coffeemachine.print_order()
order_list = coffeemachine.take_order()
sugar_cost=coffeemachine.check_sugar()
print("This is your final order:",''.join(order_list))
coffeemachine.calculate_bill(order_list,sugar_cost,final_menu)
