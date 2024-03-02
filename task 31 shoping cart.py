# task 31
# shoping cart

class item:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

class cart(item):
    def __init__(self):
        self.items = {}

    def additem(self, item):
        if item.name in self.items:
            self.items[item.name][1] += item.quantity
        else:
            self.items[item.name] = [item.price, item.quantity]

    def showitem(self):
        return self.items

    def removeitem(self, item):
        if item.name in self.items:
            self.items[item.name][1] -= item.quantity
            if self.items[item.name][1] <= 0:
                del self.items[item.name]
            else:
                print(f"Removed {item.name} from the cart")
        else:
            print(f"{item.name} not found in the cart")

    def totalprice(self):
        self.total_price = sum(price * quantity for price, quantity in self.items.values())
        return self.total_price

    def checkout(self):
        items = self.showitem()
        total_price = self.totalprice()
        print('The items in your cart are:', items)
        print('Total amount is:', total_price)

if __name__ == '__main__':
    item1 = item('pen', 5)
    item2 = item('pencil', 3)
    item3 = item('chalk', 2)

    cart = cart()

    while True:
        d = int(input('Enter 1 to add items to cart\n2 to remove items from your cart\n3 to view the items\n4 to checkout your cart\n'))
        if d == 1:
            a = int(input('\nEnter the item to add:\n1 for pen\n2 for pencil\n3 for chalk\nEnter 0 to finalize\n'))
            if a == 1:
                cart.additem(item1)
            elif a == 2:
                cart.additem(item2)
            elif a == 3:
                cart.additem(item3)
        elif d == 2:
            b = int(input('\nEnter the item to remove:\n1 for pen\n2 for pencil\n3 for chalk\n'))
            if b == 1:
                cart.removeitem(item1)
            elif b == 2:
                cart.removeitem(item2)
            elif b == 3:
                cart.removeitem(item3)
        elif d == 3:
            print('\n', cart.showitem())
        elif d == 4:
            print('\n--------------checkout----------')
            cart.checkout()
            break  # Exit the loop after checkout

        