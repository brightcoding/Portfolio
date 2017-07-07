#usrInput = input("Type left or right.")

left_bartender = ""
right_professor = ""


start = ''' You wake up Friday morning to the sound of barking. You go outside and find a lone dog. No owner to be found. It is time to find the owner.
'''
print(start)

print("Type 'left' to follow an abandoned leash or 'right' to follow a missing paper")
left_bartender = input()
right_professor= input()
if left_bartender == "left":
    print("You follow the leash. You read the name on the collar. Choose left or right.")
    if left_bartender == "left":
            print ("If you decide to go left you discover the name matches the name on the leash.")
    if left_bartender == "right":
             print ("If you decide to go right you discover the name does not match the leash.")
             print ("Type 'yes' if you agree to continue with your outcome")
                if left_bartender == "yes":
                print ("The owner appears frantically looking for their dog. The dog and the owner reunite in a slow motion run to each other.")
elif right_professor == "right":
    print ("You follow the missing paper. You read the name on the collar. Choose left or right.")
        if right_professor == "left":
        print ("You chose left you discover the name does not match the name on the flyer.")
            if right_professor == "right":
            print ("You chose right you discover the dog does not respond to the name on the flyer.")
            print ("Type 'yes' if you agree to continue with your outcome.")
            if right_professor == "yes"
                print ("The dog runs away because it spots a squirrel.")
