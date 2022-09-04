# 3.1.1.10 LAB - Spathiphyllum
flower = str(input("Please enter a flower name: "))

if flower == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif flower == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not {}!".format(flower))