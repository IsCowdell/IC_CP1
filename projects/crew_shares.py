#IC 1st Crew Shares

def calculate_shares(total_treasure, num_crew_members):
    # Total shares: Captain (7) + First Mate (3) + Crew (1 each)
    total_shares = 7 + 3 + num_crew_members

    # Value of one share
    share_value = total_treasure / total_shares

    # Calculate individual payouts
    captain_share = 7 * share_value
    first_mate_share = 3 * share_value
    crew_share = share_value

    # Adjust crew payout (they already received $500)
    crew_remaining = crew_share - 500

    # Display results
    print(f"Total treasure: ${total_treasure:,.2f}")
    print(f"Number of crew members: {num_crew_members}")
    print(f"Each share is worth: ${share_value:,.2f}")
    print(f"Captain receives: ${captain_share:,.2f}")
    print(f"First Mate receives: ${first_mate_share:,.2f}")
    print(f"Each crew member still needs to be given: ${crew_remaining:,.2f}")

# Example usage
# You can change these values or prompt the user for input
total_treasure = float(input("Enter total treasure amount in dollars: "))
num_crew_members = int(input("Enter number of crew members: "))
