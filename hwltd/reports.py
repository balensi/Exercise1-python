import copy
import random
from typing import List
import workers
from hwltd import organization
from workers.person import Person
import hwltd.organization
from workers.structure import Worker, Group


def get_average_salary2(group):
    numWorker: int = 0
    salarySum: int = 0

    for w in group:
        assert isinstance(w, Worker)
        numWorker += 1
        salarySum += w.getSalary()
    return salarySum / numWorker


def get_average_salary(group):
    assert (isinstance(group, Group))
    numWorker: int = 0
    salarySum: int = 0

    for w in group.get_workers():
        numWorker += 1
        salarySum += w.getSalary()
    return salarySum / numWorker


def search(worker, group=organization.root):
    assert (isinstance(group, Group))
    if hasattr(group, "subGroupList"):
        for sub in group.subGroupList:
            assert (isinstance(sub, Group))
            if worker in sub.get_workers():
                return search(worker, sub)
    else:
        return group.get_workers()


def get_relational_salary(worker):
    assert (isinstance(worker, Worker))
    myteamates = search(worker)
    myteamates.remove(worker)
    result = {}
    for t in myteamates:
        assert (isinstance(t, Worker))
        if t.person.ID != worker.person.ID and t.person.FIRSTNAME != worker.person.FIRSTNAME and t.person.LASTNAME != worker.person.LASTNAME:
            # print(str(t.person.ID) + " " + str(worker.person.ID))
            result.update({t.person.FIRSTNAME + " " + t.person.LASTNAME: t.getSalary() / worker.getSalary()})
    return result


def get_num_employees(department, depth):
    if depth == 0:
        return
    if department is None:
        return
    else:
        assert (isinstance(department, Group))
        mykey = department.groupName + " - " + str(len(department.get_workers())) + " workers"
        i = len(department.get_parents())
        space = ""
        while 0 < i:
            i -= 1
            space += "  "
        print(space + mykey)
        myvalues = {}
        if hasattr(department, "subGroupList") and depth > 1:
            depth += -1
            for childGroup in department.subGroupList:
                myvalues.update(get_num_employees(childGroup, depth))
        return {mykey: myvalues}


'''
def test():
    print("testFunction")


def test2():
    return 2


test()
x = test2()
print(x)
p2 = Person("hanna", "levy", 1994, "hannalevy@hotmail.fr", "+333-444-4444", "")
test()

print(p2.FIRSTNAME)

ww2: Worker = Worker(p2, 123)
print(ww2.person.FIRSTNAME)
ww3 = copy.copy(ww2)
# w2 = Worker(w)
print(ww3.person.FIRSTNAME)
ww3.augmenteSalary(111)
print(ww2.salary)

print(ww3.salary)

workerList: List[Worker] = [ww2, ww3]
test()
result = get_average_salary(workerList)
print(result)

mydict = {}
mydict.update({"key ": "value"})
print(mydict)
mydict.update({"key2 ": "value2"})
print(mydict)
mydict2 = {"dict1": mydict}
#mydict3 = {"testKey": "testValue", mydict}
#print(mydict3)'''

helloworld = hwltd.organization.HelloWolrd(
    "C:/Users/atlas/Downloads/excellentTeam/excellentTeam/prework-task2-data.txt")

worker = random.choice(organization.root.get_workers())
print(worker.person.LASTNAME + " " + worker.person.FIRSTNAME)
print(get_relational_salary(worker))
