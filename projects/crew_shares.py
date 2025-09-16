#IC 1st Crew Shares

print("The crew earned a whole bunch of money on the last outing, but the captain didn't have time to divvy it all up before release everyone to port." "He gave each member of the crew 500 dollars for the evening and then sat down with his first mate to properly divide the shares. The captain of the crew gets 7 shares. The first mate gets 3 share. Each member of the crew then gets 1 share but the crew members have all already received $500.")

crenum = int(input"How many crew members are there:" )
                
outing_money = float(input("how much money did they ? "))

final_money = (outing_money/crenum * 500)

caps_share = float(round(outing_money * (7/11),2))
print(caps_share)
firstmate_share = float(round((outing_money * (3/11),2)))
print(firstmate_share)
crew_share
