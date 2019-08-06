from workers.person import Person, StreetAddress, PobAddress
from workers.structure import Group, Worker, Engineer, SalesPerson


# import hwltd.reports


class Employees:
    def __init__(self, path="C:/Users/atlas/Downloads/excellentTeam/excellentTeam/prework-task2-data.txt"):
        file = open(path, "r")
        self.employeeDict = {}
        lines = file.read().splitlines()
        i = 0
        for line in lines:
            if i > 2:
                attributes = line.split(",")
                self.employeeDict.update({attributes[3] : attributes[0] + attributes[1]})
            i += 1
    pass


class HelloWolrd:
    def __init__(self, path="C:/Users/atlas/Downloads/excellentTeam/excellentTeam/prework-task2-data.txt"):
        self.structure = root
        file = open(path, "r")
        numofLines = len(open(path).readlines())
        lines = file.read().splitlines()
        i = 0
        for line in lines:
            if i > 2:
                attributes = line.split(",")
                #<last_name>, <first_name>, <year_of_birth>, <email>, <phones>, <address>, <team>, <role>, <data>
                #   0               1           2               3           4       5         6     7       8
                phones = attributes[4].strip().split(";")
                addressParts = attributes[5].strip().split(";")
                if len(addressParts) == 4:
                    address = StreetAddress(addressParts[0], addressParts[1], addressParts[3], addressParts[2])
                else:
                    if len(addressParts) == 3:
                       address = PobAddress(addressParts[0], addressParts[1], addressParts[2])
                    if len(addressParts) == 2:
                        address = PobAddress(addressParts[0], addressParts[1])
                myperson = Person(attributes[1].strip(),
                                  attributes[0].strip(), int(attributes[2].strip()), attributes[3].strip(),
                                  phones, address)
                if attributes[7].strip() == "staff":
                    myNewWorker = Worker(myperson, int(attributes[8].strip()))
                else:
                    dataArgs= attributes[8].strip().split(";")
                    if attributes[7].strip() == "engineer":
                        if len(dataArgs) == 2:
                            myNewWorker = Engineer(myperson, int(dataArgs[0]), int(dataArgs[1]))
                        else:
                            myNewWorker = Engineer(myperson, int(dataArgs[0]))
                    else:
                        if len(dataArgs)== 3:
                            myNewWorker = SalesPerson(myperson, int(dataArgs[0]), float(dataArgs[1]), dataArgs[2:])
                        else:
                            myNewWorker = SalesPerson(myperson, int(dataArgs[0]))
                add(myNewWorker, attributes[6].strip(), root)
            i += 1


def add(myNewWorker, team, rootName):
    assert (isinstance(myNewWorker, Worker))
    assert (isinstance(rootName, Group))
    # print("add :" + rootName.groupName)
    if rootName.groupName.lower() == team.lower():
        rootName.workerList.append(myNewWorker)
    else:
        if hasattr(rootName, "subGroupList"):
            for child in rootName.subGroupList:
                assert (isinstance(child, Group))
                add(myNewWorker, team, child)

    pass

#region organization structure
infrastructure = Group("Infrastructure", "Team", None, [])
app = Group("App", "Team", None, [])
drivers = Group("Drivers", "Team", None, [])
qa = Group("QA", "Team", None, [])
sw = Group("SW", "Group", None, [infrastructure, app, drivers, qa])

chip = Group("Chip", "Team", None, [])
board = Group("Board", "Team", None, [])
power = Group("Power", "Team", None, [])
hw = Group("HW", "Group", None, [chip, board, power])

cto = Group("CTO", "Group", None, [])
design = Group("Design", "Team", None, [])
poc = Group("Poc", "Team", None, [])
system = Group("System", "Group", None, [design, poc])
engineering = Group("Engineering", "Department", None, [sw, hw, cto, system])

tech = Group("Tech", "Team", None, [])
staff = Group("Staff", "Team", None, [])
recruitment = Group("Recruitment", "Group", None, [tech, staff])
culture = Group("Culture", "Group", None, [])
hr = Group("HR", "Department", None, [recruitment, culture])

salaries = Group("Salaries", "Group", None, [])
income = Group("Income", "Team", None, [])
outcome = Group("Outcome", "Team", None, [])
budget = Group("Budget", "Group", None, [income, outcome])
finance = Group("Finance", "Department", None, [salaries, budget])
root = Group("Hello World", "", None, [engineering, hr, finance])
#endregion

'''
print("========================================================")
testGroupChild = Group("testGroupChild", "", None, [])
testGroupChild2 = Group("testGroupChild2", "", None, [])

if testGroupChild.parentGroup is None:
    print("None")
if testGroupChild2.parentGroup is None:
    print("None")
testGroup = Group("testGroup", "", None, [testGroupChild, testGroupChild2])
print(testGroupChild.parentGroup.groupName)
print(testGroupChild2.parentGroup.groupName)

for parent in outcome.get_parents():
    if parent is not None:
        print(parent.groupName)
'''
helloworld = HelloWolrd("C:/Users/atlas/Downloads/excellentTeam/excellentTeam/prework-task2-data.txt")
'''
print(root.get_workers())
person2 = Person("israel", "sellam", 1991, "israel@hotmail.fr", "+333-444-4444", "")
person3 = Person("tsipora", "perez", 1996, "sephora.p96@gmail.com", "+333-444-4444", "")
person4 = Person("mickael", "balensi", 1997, "micka.balensi@gmail.com", "+333-444-4444", "")
person5 = Person("nathan", "balensi", 2000, "nathan.balensi@gmail.com", "+333-444-4444", "")

myworker2 = Worker(person2, "cto", "","")
myworker3 = Worker(person3, 300)
myworker4 = Worker(person4, 400)
myworker5 = Worker(person5, 500)



print(cto.get_workers())
add(myworker2, root)
print(cto.get_workers())
i=0
for wo in root.get_workers():
    print(i)
    i += 1
    print(type(wo))
    assert (isinstance(wo, Worker))
    print(wo.person.FIRSTNAME + wo.person.LASTNAME)
print(Employees().employeeDict)
'''

