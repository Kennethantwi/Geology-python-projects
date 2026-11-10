height = int(input("Enter height: "))
distance = int(input("Enter distance: "))
slope = height / distance
print("Slope is:", slope)

if slope > 1:
    print("STEEP - Dangerous! Don't build here")
elif slope > 0.5:
    print("MEDIUM - Be careful")
else:
    print("FLAT - Safe to build")
