# Class to store data about the wine
class Wine:
    def __init__(
        self,
        name,
        name2,
        location,
        price,
        productnr,
        alcohol_procentage,
        suger_amount,
        taste_and_usage,
    ):
        self.name = name
        self.name2 = name2
        self.location = location
        self.price = price
        self.productnr = productnr
        self.alcohol_procentage = alcohol_procentage
        self.suger_amount = suger_amount
        self.taste_and_usage = taste_and_usage
