
from member import Member
from trainer import Trainer
from equipment import Equipment
from gym_class import GymClass
from gym import Gym

gym = Gym("Fitness Club")

m1 = Member("Alice","M1",22,"111","basic")
m2 = Member("Ben","M2",30,"222","vip", vip_months=14)
t1 = Trainer("Tom","T1",35,"333","Yoga")

gym.members.extend([m1,m2])
gym.trainers.append(t1)

c1 = GymClass("Yoga","Monday")
c1.add_member(m1)
c1.add_member(m2)
c1.set_trainer(t1)

mat1 = Equipment("Yoga Mat","Flexibility")
gym.equipment.append(mat1)
c1.add_equipment(mat1)

while True:
    print("\n1 Average Age")
    print("2 Search Person")
    print("3 Count Class Members")
    print("4 Show Member Fees")
    print("5 Test Enrollment Rejection")
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

    elif choice == "4":
        for m in gym.members:
            print(f"{m.name}: N${m.get_fee():.2f}")

    elif choice == "5":
        try:
            c1.add_member(t1)
        except TypeError as e:
            print(f"Rejected: {e}")

    elif choice == "0":
        break
