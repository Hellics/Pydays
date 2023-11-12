#Third day project a story that uses if elif else statment

#variables
green ='\u001b[92m'
red ='\u001b[31m'

#welcome message

print(red+"         Welcome to the Netdoor.")

print(green +'''
                    
                 uuuuuuu
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
   uuu        $$u$ $ $ $ $u$$       uuu
  u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$ 
u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
 """      ""$$$$$$$$$$$uu ""$"""
           uuuu ""$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  $$$$$$$$$$""""           ""$$$$$$$$$$$"
   "$$$$$"                      ""$$$$""
     $$$"                         $$$$"
''')

print('\u001b[31m'+"Let your soul fly, maybe you're not dying.")
print('\u001b[92m'+"------------------------------------------")

choice=input('Welcome to the Netdoor, if you want to enter chose the right side. Left/Right\n').lower()

if choice == "right":
    print("""

             You are in... Your eyes begun to see briliant light all around.
             Instantly everyting change now there are black spot in a light green sky
             your foot are bigger and you have only one shoe but it could be your only foot.
             This is THE NET.


          """)
    print("     Don't waste your time, every second behind the NETDOOR burn your soul")


    choice2 =input("Time is running stop floating, start flyng! Where do you want to go? up, down, left, right\n")

    if choice2 == "right":
        print("""

              Now you are really near to the final destination.

              Your soul became a tiny piece of paper
              every kind of notice were written on you for hundred years.

              Your mind is near to collapse for the incredible ammount of information
              you feel the knowledge as you can feel your blood.

              There is no motivation for your action.

              What are you doing?

              Why are you here?


              """)
        choice3=input("Three coloured black hole apear in front of you 'Red','Green' and 'Blu', chose one for the treasure\n").lower()
        if choice3=="green":
            print("""

                  Everyting around you became symbols of different shapes and colour,

                  is beautiful and you feel better and better
                  
                  Your pleasure is growing...
                  
                  Then, you DIE.

                  """)
        elif choice3 == "red":
            print("""

                  You pass the red hole, everything became black,
                  there is only a litle, blinking, orange spot,
                  you can't move,
                  you can only watch at the spot.


                  The time goes, you DIE.

                  """)

        elif choice3 == "blu":
                  print('\u001b[31m'+ """

                        You are finaly in, money folder are in front of you
                        You have only to catch them

                        Now you are rich

                        Money fly to your bank

                        The sound of your breathing break in your ears

                        YOU WIN

                        Disconnected...

                        """)
        else:
            print("""

                  BURN, BURn, BUrn, Burn, burn, bur, bu, b, ...
                  You are DEAD.""")
    else:
        print("You lose too much time... your soul evaporate. You are DEAD.")



else:
    print("Your live simply expires... YOU ARE DEAD.")
