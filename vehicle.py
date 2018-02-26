class Vehicle():

    vehicles_running = 0
    
    def __init__(self):
        self.fuel = 100
        self.running = False
    
    def start(self):
        print("Starting up the Vehicle")
        Vehicle.vehicles_running += 1
        self.fuel -= 1
        self.running = True
    
    def stop(self):
        print("Stopping the Vehicle")
        Vehicle.vehicles_running -= 1
        print("You have {0} vehicles running".format(Vehicle.vehicles_running))
        self.running = False
    
    def fuelgauge(self):
        print("You have {0} liters of fuel left".format(self.fuel))

v = Vehicle()
# v.start()

# t = Vehicle()
# t.start()
# t.stop()

v.fuelgauge()
v.start()
v.fuelgauge()