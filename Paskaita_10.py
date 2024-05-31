
# class Animal():
#     def __init__(self, leg_amount = 4, has_fur = True):
#         self.legs = leg_amount # 1. suo.legs = leg_amount 2. kate.legs = leg_amount
#         self.nose = None
#         self.ears = 2
#         self.has_fur = has_fur # 1 suo

#     def run(self): # self = suo
#         print(f"I am running on my {self.legs} legs") # 1. suo.legs # monkey.legs
#     def addNose(self):
#         if self.nose == None:
#             self.nose = 1
#         else:
#             self.nose = self.nose + 1

#     def __str__(self) -> str: # self = suo
#         return f"has {self.legs} legs and {self.nose} noses"

# suo = Animal() # 1

# kate = Animal(4) # 2

# monkey = Animal(2)

# suo.addNose()


# # print(f"the dog has {suo.legs} legs and {suo.nose} noses")

# # print(f"the monkey has {monkey.legs} legs and {monkey.nose} noses")

# # suo.run() # 1
# # print("And the monkey...")
# # monkey.run()



# def sum(num1, num2 = 4):
#     return num1 + num2


# answer = sum(4)

# # print(answer)


# print(suo)

# print(kate)

# print(f"The monkey: {monkey}")


class Vehicle():
    def __init__(self, move_speed): 
        self.move_speed = move_speed
    def Move(self):
        print("I am moving")

class LandVehicle(Vehicle):
    def __init__(self, move_speed, distance_from_ground = 30):
        super().__init__(move_speed)
        self.distance_from_ground = distance_from_ground

    def Move(self):
        print("I am moving trough land")

class Car(LandVehicle): # car -> LandVehicle -> Vehicle
    def __init__(self, move_speed, wheel_amount = 4, distance_from_ground=30):
        super().__init__(move_speed, distance_from_ground)
        self.wheel_amount = wheel_amount
    def Move(self):
        print("I am moving trough land probably on a road")


    def Drive(self):
        print("I am driving")


vehicle = Vehicle(15)


land_veh = LandVehicle(30)

my_car = Car(50)

# print(f"vehicle speed is {vehicle.move_speed}")
# print(f"land_veh speed is {land_veh.move_speed}")
# print(f"my_car speed is {my_car.move_speed} and it has {my_car.wheel_amount} wheels")

vehicles = [vehicle,land_veh,my_car]

for v in vehicles:
    if isinstance(v, LandVehicle):
        v.Move()

print("Mano pridejimas")

print("Mano kitas pridejimas")