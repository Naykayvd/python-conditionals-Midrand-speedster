# Compulsory Task: Midrand speedster
# JHB Metro Police Demerit System Program

driver_speed = int(input("what was the drivers speed in km/h"))
average_road_speed = int(input("what was the allowed speed on the road"))
demerits = (driver_speed-average_road_speed)/5

if demerits >= 12:
    print("Going to jail")
else:
    print("points: " + str(demerits))