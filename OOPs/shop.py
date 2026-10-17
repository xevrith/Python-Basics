# Shop and Grocery Shop (List)

class Shop:

    def __init__(self,shop_name):
        self.shop_name = shop_name
        self.items = []

    def add_items(self,item):
        self.items.append(item)
        print("Item Added")

    def show_items(self):
        for item in self.items:
            print(item)


class Grocery(Shop):
    def total_items(self):
        print(len(self.items))

    def has_item(self,name):
        if name in self.items:
            return True

        else:
            return False

    def remove_item(self,name):

        if name in self.items:
            self.items.remove(name)
            print("Item Removed")

        else:
            print("Item Not Found")



c1 = Grocery("MKC")
c1.add_items("Milk")
c1.add_items("Oil")
c1.add_items("Cold Drink")

c1.show_items()
c1.remove_item("Milk")
c1.show_items()