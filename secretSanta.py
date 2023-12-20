import random
import time

def clear_screen():
    # Print 50 empty lines to simulate clearing the screen
    print('\n' * 50)

def secret_santa(participants):
    # Check if the number of participants is valid
    if len(participants) < 2 or len(participants) > 4:
        print("Error: Number of participants should be between 2 and 4.")
        return

    # Shuffle the participants to randomize the assignment
    random.shuffle(participants)

    # Create a dictionary to store the pairs
    secret_santa_pairs = {}

    # Assign each participant a Secret Santa
    for i in range(len(participants)):
        # Avoid assigning a participant to themselves
        j = (i + 1) % len(participants)
        secret_santa_pairs[participants[i]] = participants[j]

    # Print the Secret Santa pairs
    for participant, santa in secret_santa_pairs.items():
        print(f"{participant} is the Secret Santa for {santa}")
        input("Press Enter to continue...")
        clear_screen()

# Example usage with 4 participants
participants_list = ["Alice", "Bob", "Charlie", "David"]
secret_santa(participants_list)
