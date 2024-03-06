def display_results(AAP, BJP, Congress, BSP, Nota):
    print("\nTotal Votes:")
    print("AAP:", AAP)
    print("BJP:", BJP)
    print("Congress:", Congress)
    print("BSP:", BSP)
    print("NOTA:", Nota)

    # Determine the winner
    max_votes = max(AAP, BJP, Congress, BSP, Nota)
    if max_votes == AAP:
        print("AAP wins!")
    elif max_votes == BJP:
        print("BJP wins!")
    elif max_votes == Congress:
        print("Congress wins!")
    elif max_votes == BSP:
        print("BSP wins!")
    else:
        print("NOTA wins!")

def main():
    AAP = 0
    BJP = 0
    Congress = 0
    BSP = 0
    Nota = 0

    while True:
        print("Welcome to the Voting System")
        print("1. Vote for AAP")
        print("2. Vote for BJP")
        print("3. Vote for Congress")
        print("4. Vote for BSP")
        print("5. Vote for NOTA")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            AAP += 1
            print("You have voted for AAP.")
        elif choice == '2':
            BJP += 1
            print("You have voted for BJP.")
        elif choice == '3':
            Congress += 1
            print("You have voted for Congress.")
        elif choice == '4':
            BSP += 1
            print("You have voted for BSP.")
        elif choice == '5':
            Nota += 1
            print("You have voted for NOTA.")
        elif choice == '6':
            display_results(AAP, BJP, Congress, BSP, Nota)
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()