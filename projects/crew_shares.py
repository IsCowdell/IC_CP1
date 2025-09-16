#IC 1st Crew Shares

print("The crew earned a whole bunch of money on the last outing, but the captain didn't have time to divvy it all up before release everyone to port." "He gave each member of the crew 500 dollars for the evening and then sat down with his first mate to properly divide the shares. The captain of the crew gets 7 shares. The first mate gets 3 share. Each member of the crew then gets 1 share but the crew members have all already received $500.")

crenum = int(input("How many crew members are there:"))
                
outing_money = float(input("how much money did they ? "))

divider = crenum + 10
shares = outing_money/divider


caps_share = (shares * 7)

firstmate_share = float(shares * 3)


crew_share = (shares-500)

print(f"this is how much the crew earns {crew_share:.2f}")
print(f"this is how much the firstmate earns {firstmate_share:.2f}")
print(f"this is how much the captains earns {caps_share:.2f}")
print(f"this is how much the group earns {shares:.2f}")