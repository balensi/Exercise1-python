# import person
from typing import List

import workers
from workers import person
import copy
from workers.person import Person


class Group:
    def __init__(self, groupeName, description, parentGroup, myList):
        flag: bool = True
        assert (isinstance(groupeName, str))
        assert (isinstance(description, str))
        if parentGroup is not None:
            assert (isinstance(parentGroup, Group))
        self.groupName = groupeName
        self.description = description
        self.parentGroup = parentGroup
        if isinstance(myList, List):
            for w in myList:
                if isinstance(w, Worker):
                    # if isinstance(w, myWorker):
                    flag = True
                else:
                    flag = False
            if flag or len(myList) == 0:
                self.workerList = myList
            else:
                self.subGroupList = myList
                for subGroup in self.subGroupList:
                    assert (isinstance(subGroup, Group))
                    subGroup.parentGroup = self
        pass

    pass

    def get_workers(self):
        if hasattr(self, "workerList"):
            return self.workerList
        else:
            totalWorker = []
            for g in self.subGroupList:
                assert (isinstance(g, Group))
                for myW in g.get_workers():
                    totalWorker.append(myW)
            return totalWorker

    def get_parents(self):
        result = []
        if self.parentGroup is None:
            return result
        else:
            result.append(self.parentGroup)
            for gdprt in self.parentGroup.get_parents():
                result.append(gdprt)
            return result


class Worker:
    def __init__(self, myperson, salary):
        if isinstance(myperson, Person):
            self.person = myperson
        if isinstance(salary, int):
            self.salary = salary

    pass
    '''
    class myWorker(Person):
        def __init__(self, firstname, lastname, yearofBirth, email, phone, address, team, role, data):
            self.person = Person(firstname, lastname, yearofBirth, email, phone, address)
            self.team = team
            self.role = role
            self.data = data

        pass
    '''
    '''
    def __init__(self, copyWorker):
        if isinstance(copyWorker, Worker):
            self = copyWorker
            self.copy_constructor(copyWorker)
    '''
    '''
    def __copy__(self):
        """

        :type self: object
        """
        return Worker(self.__getattribute__(person), self.__getattribute__(Worker.salary))
    '''

    def getSalary(self):
        return self.salary

    '''
    def augmenteSalary(self, sum):
        assert isinstance(sum, int)
        self.salary += sum
    '''


class Engineer(Worker):
    def __init__(self, myperson, salary, bonus=0):
        super().__init__(myperson, salary)
        self.bonus = bonus

    pass

    def getSalary(self):
        return self.salary + self.bonus


class SalesPerson(Worker):
    def __init__(self, myperson, salary, commission=0, deals=[]):
        super().__init__(myperson, salary)
        self.commission = commission
        self.deals = deals  # list des quantite des deals

    pass

    def getSalary(self):
        return self.salary + self.commission * sum(self.deals)


'''
p = Person("deborah", "balensi", 1994, "deborqhbqlensi@hotmail.fr", "+333-444-4444", "")
w = Worker(p, 123)
w3 = copy.copy(w)
w3.augmenteSalary(111)
person2 = Person("israel", "sellam", 1991, "israel@hotmail.fr", "+333-444-4444", "")
person3 = Person("tsipora", "perez", 1996, "sephora.p96@gmail.com", "+333-444-4444", "")
person4 = Person("mickael", "balensi", 1997, "micka.balensi@gmail.com", "+333-444-4444", "")
person5 = Person("nathan", "balensi", 2000, "nathan.balensi@gmail.com", "+333-444-4444", "")

myworker2 = Worker(person2, 200)
myworker3 = Worker(person3, 300)
myworker4 = Worker(person4, 400)
myworker5 = Worker(person5, 500)

workerList2: List[Worker] = [w, w3]
grandparentGroup = Group("grandParentGroup", "", None, [])
parentGroup = Group("parentGroup", "groupe parent root", grandparentGroup, [])
myGroup2 = Group("testGroup2", "group d'essai2", None, [myworker2, myworker3])
myGroup3 = Group("testGroup3", "group d'essai3", None, [myworker4, myworker5])
myGroup = Group("testGroup", "group d'essai", parentGroup, [myGroup2, myGroup3])

print(myGroup.get_workers())

for wonkier in myGroup.get_workers():
    print(wonkier.person.FIRSTNAME)
    print(wonkier.person.LASTNAME)
    
print(myGroup.get_parents())
for parent in parentGroup.get_parents():
    print(parent.groupName)

for parent in myGroup.get_parents():
    print(parent.groupName)
'''
