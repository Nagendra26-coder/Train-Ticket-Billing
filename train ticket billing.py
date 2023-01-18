def booking():

    print("Welcome to Rajapalayam Railway station")

booking()

print("1-Rjpm to Srivi\n2-Rjpm to Sivakasi\n3-Rjpm to Madurai")


a=int(input("Select the station\n"))

p=("Ticket Ammount Rs.")


if a == 1:
      print("1.Rjpm to Srivi = Rs.20\n")
      
      b = int(input("Num of tickets you wants\n"))

      p = b * 20

      print("Total Ammount Rs.= ",p)
elif a == 2:
      print("1.Rjpm to Sivkasi = Rs.25\n")
      
      b = int(input("Num of tickets you wants\n"))

      p = b * 25

      print("Total Ammount Rs.= ",p)

elif a == 3:
      print("1.Rjpm to Madurai = Rs.30\n")
      
      b = int(input("Num of tickets you wants\n"))

      p = b * 30

      print("Total Ammount Rs.= ",p)

else :
    print("Invaild input")
