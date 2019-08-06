import re


def valid_email(email):
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))


def checkNumber(number):
    return bool(re.search(r"^\++[0-9+\-]+$", number)) or bool(re.search(r"^[0-9+\-]+$", number))


class Person:
    class_counter = 0

    def __init__(self, firstname, lastname, yearOfBirth, email, phones, address):
        if firstname != "":
            self.FIRSTNAME = firstname
        if lastname != "":
            self.LASTNAME = lastname

        self.yearOfBirth = yearOfBirth

        if valid_email(email):
            self.EMAIL = email
        self.ID = Person.class_counter
        Person.class_counter += 1
        myphones = []
        for phoneN in phones:
            if checkNumber(phoneN):
                phoneElement = Phone(phoneN)
                myphones.append(phoneElement)
        self.phones = myphones

        if isinstance(address, Address):
            self.address = address


class Phone:
    def __init__(self, phoneNumber):
        if checkNumber(phoneNumber):
            self.phoneNumber = phoneNumber


#region adresses
class Address:
    def __init__(self, country, city):
        if country != "":
            self._country = country
        if city != "":
            self._city = city

    def getDetails(self):
        return self._country + " " + self._city


class PobAddress(Address):
    def __init__(self, country, city, post_office_box_number=0):
        super().__init__(country, city)
        if isinstance(post_office_box_number, int):
            self.post_office_box_number = post_office_box_number

    def getDetails(self):
        return self.post_office_box_number


class StreetAddress(Address):
    def __init__(self, country, city, numHouse, streetName):
        super().__init__(country, city)
        if isinstance(numHouse, int):
            self.numHouse = numHouse
        if streetName != "" and isinstance(streetName, str):
            self.streetName = streetName

    pass

    def getDetails(self):
        return self.streetName + " " + self.numHouse
#endregion
