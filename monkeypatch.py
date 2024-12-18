class Car:
    def start_engine(self):
        print("Engine started!")
car = Car()
print("Before patching-->")
car.start_engine()
def patched_start_engine(self):
    print("Engine started with a roar!")
Car.start_engine = patched_start_engine
print("After patching-->")
car.start_engine()  