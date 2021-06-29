class PC:
    def __init__(self, manufacturer, name, yearOfIssue, price):
        self.manufacturer = manufacturer
        self.name = name
        self.yearOfIssue = yearOfIssue
        self.price = price

    def __repr__(self):
        return '<String - {}>'.format(self.name)

    def __eq__(self, value):
        if not isinstance(self.name, str):
            return self.name == value.name

    def __ne__(self, value):
        return self.name != value.name

pc1 = PC('Билл Гейтс', 'MicrosoftPC', 1999, 2000000)
pc2 = PC('Стив Джобс', 'iMac', 2008, 99999999)
pc3 = PC('Sanya', 'шайтан-коробка', 3729, 100)

