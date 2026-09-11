
from member import Member
from trainer import Trainer
from membership import *
from gym_class import GymClass
from gym import Gym

gym = Gym("Fitness Club")

m1 = Member("Alice","M1",22,"111",BasicMembership())
m2 = Member("Ben","M2",30,"222",VIPMembership(14))
t1 = Trainer("Tom","T1",35,"333","Yoga")

gym.members.extend([m1,m2])
gym.trainers.append(t1)

c1 = GymClass("Yoga","Monday")
c1.add_member(m1)
c1.add_member(m2)

while True:
    print("\n1 Average Age")
    print("2 Search Person")
    print("3 Count Class Members")
    print("0 Exit")

    choice = input("Choice: ")

    if choice == "1":
        print(gym.avg_age())

    elif choice == "2":
        name = input("Name: ")
        result = gym.find_person(name)
        for p in result:
            print(p.details())

    elif choice == "3":
        print(c1.count_members())

    elif choice == "0":
        break
