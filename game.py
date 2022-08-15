import time
import random

def game():
    name = ["John Doff,", "Sara Wills,", "Tim Joe,", "Mary Lee,", "Kim Deff,"]
    job = ["a mountain climber", "a cave explorer", "a gamer", "a student", "an adventure lover"]
    place = ["Mountains of Africa.", "Jungles of Africa.", "Jungles of India.", "Himalayas."]
    playname = random.choice(name)
    playjob = random.choice(job)
    playplace = random.choice(place)
    print("You are", playname, playjob,"exploring The",playplace,)
    caves = ["The Cave of Death", "The Cave of Treasures", "The Hell", "a cave full of snakes"]
    playcave = random.choice(caves)
    time.sleep(1)
    print("You wandered into", playcave, "looking for treasure. But you had no idea how dangerous it is.")
    time.sleep(1)
    choice1 = int(input("You have two caves in front of you. Which one will you choose? (Enter 1 for Cave 1 and 2 for Cave 2) "))
    treasure_cave = random.randint(1,2)
    if choice1 > 2 or choice1 < 1:
        print("Wrong choice!\n")
        game()
    if choice1 == treasure_cave:
        print("\nYou found THE TREASURE!!\n")
        choice = int(input("""What do you want to do with this?
        1  - Sell the treasure and buy a new car that costs $ 9,999,999,999
        2  - Sell the treasure and buy your girlfriend/boyfriend some new gifts which costs over $ 100,000,000
        3  - Sell the treasure and buy a new house 
        4  - Sell the treasure and deposit all the money in your bank account
        5  - Sell the treasure and buy some expensive video games
        6  - Sell the treasure and hire some hitmen
        7  - Sell the treasure and hire some bodyguards
        8  - Sell the treasure and buy the most expensive phone
        9  - Sell the treasure and buy all the food in the world (you'll be fat if you eat too much')
        10 - Sell the treasure and buy the cutest animals in the world
        11 - Sell the treasure and hide all the money in your secret base 
        12 - Do nothing and leave the place for good """))
        if choice >= 13 or choice <= 0:
            print("Wrong choice!\n")
            game()

        if choice == 1:
            luck = random.randint(1,2)
            luck1 = random.randint(1,2)
            if luck == luck1:
                time.sleep(1)
                print("\nYou bought one of the most expensive cars in the world! You took it to a ride and everyone were jealous.")
            else:
                time.sleep(1)
                print("\nYou were showing off with the car you just bought when a theif threatened you to give him the key of the car. You had no choice but to hand over the car to him and run as fast as you can.")
                print("It is so sad!! Bad luck I guess :(")

            restart = str(input("Do you want to play again? (y/n) "))
            if restart == 'y':
                print()
                time.sleep(1)
                game()
            else:
                time.sleep(1)
                a=str(input("Click Enter key to exit"))

        elif choice == 2:
            luck = random.randint(1,2)
            luck1 = random.randint(1,2)
            if luck == luck1:
                time.sleep(1)
                print("\nYour girlfriend/boyfriend LOVED your gift!! She/he considered herself/himself the luckiest person on the Earth!")
            else:
                time.sleep(1)
                print("\nYour girlfriend/boyfriend just died out of cringe to see your gifts as they were SO BAD. She \ he immediately left your house.")

            restart = str(input("\nDo you want to play again? "))
            if restart == 'y':
                print("")
                time.sleep(1)
                game()
            else:
                time.sleep(1)
                a = str(input("\nClick Enter key to exit."))

        elif choice == 3:
            luck = random.randint(1,2)
            luck1 = random.randint(1,2)
            if luck == luck1:
                time.sleep(1)
                print("\nYou sold the treasure and bought a brand new house, the most LUXURIOUS ONE!")
            else:
                time.sleep(1)
                print("\nYou just got ripped off by the house dealer by fooling you and selling you the smelliest and dirtiest house in the world.")
                print("It's so nasty you died just after seeing it. RIP")

            restart = str(input("\nDo you want to play again? "))
            if restart == 'y':
                print("")
                time.sleep(1)
                game()
            else:
                time.sleep(1)
                a = str(input("\nClick Enter key to exit."))
        
        elif choice == 4:
            luck = random.randint(1,2)
            luck1 = random.randint(1,2)
            if luck == luck1:
                time.sleep(1)
                print("\nnYou are now the richest person IN THE UNIVERSE!! Congrats")
            else:
                time.sleep(1)
                print("\nYou were accused of black money since you were the poorest person in the world. You got sent to jail shortly after.")
            
            restart = str(input("\nDo you want to play again? "))
            if restart == 'y':
                print("")
                time.sleep(1)
                game()
            else:
                time.sleep(1)
                a = str(input("\nClick Enter key to exit."))

        elif choice == 5:
            luck = random.randint(1,2)
            luck1 = random.randint(1,2)
            if luck == luck1:
                time.sleep(1)
                print("\nYou are now the only gamer in the world who own all of the most expensive video games.")
                print("You are now the world record holder of the 'Only Gamer Who Owns All of The Most Expensive Games'.")
            else:
                time.sleep(1)
                print("\nOh boy! Your mother killed you for spending all the money on video games. You shouldn't have bought it man!")
        
            restart = str(input("\nDo you want to play again? "))
            if restart == 'y':
                print("")
                time.sleep(1)
                game()
            else:
                time.sleep(1)
                a = str(input("\nClick Enter key to exit."))

        elif choice == 6:
            luck = random.randint(1,2)
            luck1 = random.randint(1,2)
            if luck == luck1:
                time.sleep(1)
                print("\nYou bought some hitmen from the black market. They are now serving you.")
            else:
                time.sleep(1)
                print("\nYou were not careful while accessing the black market and got fooled, loosing all of your money.")
                print("You were arrested slightly after for trying to hire a hitman from the black market.")

            restart = str(input("\nDo you want to play again? "))
            if restart == 'y':
                print("")
                time.sleep(1)
                game()
            else:
                time.sleep(1)
                a = str(input("\nClick Enter key to exit."))

        elif choice == 7:
            luck = random.randint(1,2)
            luck1 = random.randint(1,2)
            if luck == luck1:
                time.sleep(1)
                print("\nYou hired some bodyguards who are ready to die for saving your life. You recognised it after one of them saved you from a bullet")
            else:
                time.sleep(1)
                print("\nYou hired the worst bodyguards in the world. You got shot on the head and died immediately. RIP")

            restart = str(input("\nDo you want to play again? "))
            if restart == 'y':
                print("")
                time.sleep(1)
                game()
            else:
                time.sleep(1)
                a = str(input("\nClick Enter key to exit."))
        
        elif choice == 8:
            luck = random.randint(1,2)
            luck1 = random.randint(1,2)
            if luck == luck1:
                time.sleep(1)
                print("\nYou bought the most expensive phone in the world. Everyone who saw it were jealous of you. ")
            else:
                time.sleep(1)
                print("\nYou bought the most expensive phone in the world. But right after you inserted your sim card, the phone got stolen by a thief, who then escaped via a helicopter LOL")

            restart = str(input("\nDo you want to play again? "))
            if restart == 'y':
                print("")
                time.sleep(1)
                game()
            else:
                time.sleep(1)
                a = str(input("\nClick Enter key to exit."))

        elif choice == 9:
            luck = random.randint(1,2)
            luck1 = random.randint(1,2)
            if luck == luck1:
                time.sleep(1)
                print("\nYou bought all the food in the world and supplied everyone equal amount of healthy, high quality food. That's SO NICE of YOU!!")
            else:
                time.sleep(1)
                print("\nYou bought all the food in the world. You tried to eat it all by yourself but got raided by the hungry people the next minute you opened your secret locker in which you stored all the food. You shouldn't be so greedy afterall.")

            restart = str(input("\nDo you want to play again? "))
            if restart == 'y':
                print("")
                time.sleep(1)
                game()
            else:
                time.sleep(1)
                a = str(input("\nClick Enter key to exit."))

        elif choice == 10:
            luck = random.randint(1,2)
            luck1 = random.randint(1,2)
            if luck == luck1:
                time.sleep(1)
                print("\nYou bought all the cutest animals in the world.. AWW SO CUTE!! ")
            else:
                time.sleep(1)
                print("\nYou bought all the cutest animals in the world. Unfortunately, that included a hungry tiger, which ate you soon after you bought it. RIP.")

            restart = str(input("\nDo you want to play again? "))
            if restart == 'y':
                print("")
                time.sleep(1)
                game()
            else:
                time.sleep(1)
                a = str(input("\nClick Enter key to exit."))

        elif choice == 11:
            luck = random.randint(1,2)
            luck1 = random.randint(1,2)
            if luck == luck1:
                time.sleep(1)
                print("\nYou hid all your money on your secret base. You can now use it efficiently. Good choice...")
            else:
                time.sleep(1)
                print("\nYou remember putting all the money in the vault inside your secret base but you ACTUALLY FORGOT WHERE THE BASE IS LOL!!!")

            restart = str(input("\nDo you want to play again? "))
            if restart == 'y':
                print("")
                time.sleep(1)
                game()
            else:
                time.sleep(1)
                a = str(input("\nClick Enter key to exit."))
        
        elif choice == 12:
            luck = random.randint(1,2)
            luck1 = random.randint(1,2)
            if luck == luck1:
                time.sleep(1)
                print("You left the place for good. Good boii :)")
            else:
                time.sleep(1)
                print("You were brutally murdered by the bear which was at the exit of cave. Soo Baad :(")

            restart = str(input("\nDo you want to play again? "))
            if restart == 'y':
                print("")
                time.sleep(1)
                game()
            else:
                time.sleep(1)
                a = str(input("\nClick Enter key to exit."))

        

    

    else:
        print("\nYou weren't lucky enough to find the treasure. Better luck next time!")
        restart = str(input("\nDo you want to play again? "))
        if restart == 'y':
            print("")
            time.sleep(1)
            game()
        else:
            time.sleep(1)
            a = str(input("\nClick Enter key to exit."))
    

game()
