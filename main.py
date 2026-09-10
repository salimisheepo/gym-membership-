from member import Member
from trainer import Trainer
from membership import BasicMembership, PremiumMembership, VIPMembership
from gym_class import GymClass
from equipment import Equipment
from gym import Gym


def build_sample_gym():
    gym = Gym("Downtown Fitness Club")

    # Members, each with a different Membership (composition)
    alice = Member("Alice Nguyen", "M001", 28, "081-000-0001", BasicMembership())
    ben = Member("Ben Carter", "M002", 34, "081-000-0002", PremiumMembership())
    cara = Member("Cara Diaz", "M003", 41, "081-000-0003", VIPMembership(14))
    dan = Member("Dan Okafor", "M004", 23, "081-000-0004", BasicMembership())

    gym.add_member(alice)
    gym.add_member(ben)
    gym.add_member(cara)
    gym.add_member(dan)

    # Trainers (inheritance from Person)
    tom = Trainer("Tom Reyes", "T001", 30, "082-000-0001", "Yoga & Mobility")
    priya = Trainer("Priya Shah", "T002", 27, "082-000-0002", "HIIT & Spinning")

    gym.add_trainer(tom)
    gym.add_trainer(priya)

    # Equipment
    yoga_mats = Equipment("Yoga Mats", "Flooring")
    spin_bikes = Equipment("Spin Bikes", "Cardio")

    gym.add_equipment(yoga_mats)
    gym.add_equipment(spin_bikes)

    # Classes (aggregation: trainer, members, equipment)
    yoga_class = GymClass("Yoga Basics", "Mon/Wed 7:00 AM")
    spin_class = GymClass("Spin Sprint", "Tue/Thu 6:00 PM")

    tom.lead_class(yoga_class)
    priya.lead_class(spin_class)

    yoga_class.add_equipment(yoga_mats)
    spin_class.add_equipment(spin_bikes)

    gym.add_class(yoga_class)
    gym.add_class(spin_class)

    # Enroll members into classes
    gym.enroll_member(alice, yoga_class)
    gym.enroll_member(cara, yoga_class)
    gym.enroll_member(ben, spin_class)
    gym.enroll_member(dan, spin_class)
    gym.enroll_member(cara, spin_class)

    return gym, yoga_class, spin_class, tom, priya


def main():
    gym, yoga_class, spin_class, tom, priya = build_sample_gym()

    print("--- Inheritance: print_info() for members and trainers ---")
    everyone = gym.members + gym.trainers
    for person in everyone:
        print(person.print_info())

    print("")
    print("--- Polymorphism: get_monthly_fee() per member ---")
    for member in gym.members:
        plan_name = type(member.get_membership()).__name__
        fee = member.get_monthly_fee()
        print(member.get_name() + ": $" + str(fee) + " (" + plan_name + ")")
    print("Total monthly revenue: $" + str(gym.total_monthly_revenue()))

    print("")
    print("--- Type-checking method: GymClass.add_member() ---")
    print("Trying to enroll a Trainer (Tom) into the Yoga class by mistake...")
    try:
        yoga_class.add_member(tom)
    except TypeError as err:
        print("Rejected as expected:", err)

    print("")
    print("--- Basic algorithm: counting members per class ---")
    for gym_class in gym.classes:
        print(gym_class.get_name() + ": " + str(gym_class.count_members()) + " member(s)")

    print("")
    print("--- Basic algorithm: average member age ---")
    print("Average member age:", gym.average_member_age())

    print("")
    print("--- Basic algorithm: searching by name ---")
    matches = gym.search_by_name("a")
    for person in matches:
        print(person.print_info())

    print("")
    print("--- Filtering by membership type: VIP members ---")
    vip_members = gym.members_by_membership_type("VIPMembership")
    for member in vip_members:
        print(member.print_info())


if __name__ == "__main__":
    main()
