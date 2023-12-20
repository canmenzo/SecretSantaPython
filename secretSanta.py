import random

def clear_screen():
    # Print 50 empty lines to simulate clearing the screen
    print('\n' * 50)

def get_participants():
    while True:
        try:
            num_participants = int(input("Enter the number of participants (even number): "))
            if num_participants % 2 == 0 and num_participants >= 2:
                break
            else:
                print("Error: Please enter an even number greater than or equal to 2.")
        except ValueError:
            print("Error: Please enter a valid number.")

    participants = []
    for i in range(1, num_participants + 1):
        name = input(f"{i}- Enter participant name: ")
        participants.append(name)

    return participants

def secret_santa(participants):
    # Shuffle the participants to randomize the assignment
    random.shuffle(participants)

    # Create a dictionary to store the pairs
    secret_santa_pairs = {}

    # Assign each participant a Secret Santa
    for i in range(len(participants)):
        # Avoid assigning a participant to themselves
        j = (i + 1) % len(participants)
        secret_santa_pairs[participants[i]] = participants[j]

    # Print the Secret Santa pairs starting from the first participant
    for participant in participants:
        # Clear the screen before displaying each participant's match
        clear_screen()

        # Print instructions for the participant
        print(f"{participant}, please press Enter when you are ready.")
        input("Press Enter to continue...")

        # Display the Secret Santa match for the participant
        santa = secret_santa_pairs[participant]
        clear_screen()
        print(f"{participant}, you were matched with {santa}")

# Get participants from user input
participants_list = get_participants()

# Run Secret Santa algorithm
secret_santa(participants_list)
