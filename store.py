class Store:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories
    def __str__(self):
        output = f"{self.name}\n"
        for idx, category in enumerate(self.categories):
            output += " " + str(idx+1) + ", " + category + "\n"

        return output


my_store = Store("The Dugout", ["Running", "Baseball", "Basketball"])

print(my_store)

selection = input("Select the number of a department:")
print("The user selected " + str(selection))
