from random import randint
alive = True
stamina = 10
def report(s):
    if s > 8:
        print (s,"The alien is strong! It resists your pathetic attack!")
    elif s > 5:
        print (s,"With a loud grunt, the alien stands firm.")
    elif s > 3:
        print (s,"Your attack seems to be having an effect! The alien stumbles!")
    elif s > 2:
        print (s,"The alien is certain to fall soon! It staggers and reels!")
    if s==0:
        print (s,"That's it! The alien is finished!")

def fight(stam): 
    while stam > 0:
        response = input("> Enter a move 1.Hit 2.attack 3.fight 4.run")
        if "hit" in response or "attack" in response:
            less = randint(0, stam)
            stam -= less 
            print(less)
            report(stam) 
        elif "fight" in response:
            print ("Fight how? You have no weapons, silly space traveler!")
        elif "run" in response:
            print ("Sadly, there is nowhere to run."),
            print ("The spaceship is not very big.")
        else:
            print ("The alien zaps you with its powerful ray gun!")
            return True
    return False
    
print ("A threatening alien wants to fight you!\n")
alive = fight(stamina)
if alive: 
    print ("\nThe alien lives on, and you, sadly, do not.\n")
else:
    print ("\nThe alien has been vanquished. Good work!\n")