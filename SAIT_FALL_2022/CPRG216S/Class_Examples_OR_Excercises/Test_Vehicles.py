PStart = float(input("Enter Starting Postition (in metres)"))
PEnd = float(input("Enter Ending Postition (in metres)"))

StartTime = float(input("Enter Starting Time (in seconds)"))
EndTime = float(input("Enter End Time (in seconds)"))

PDelta = PEnd - PStart
TDelta = EndTime - StartTime

AverVelocity = PDelta / TDelta
AverAcceleration = AverVelocity / TDelta

print("Calculated Average Velocity: ", AverVelocity, "m/s")
print("Calculated Average Acceleration: ", AverAcceleration, "m/s^2")


