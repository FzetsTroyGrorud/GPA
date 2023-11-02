print("Hi I'm Troy grorud I created this file; GPA.py")
print("This file purpose is to see id your GPA makes you qualified for any titles")
print("I have a 3.87 GPA I Qualify for the Deans list. Type zzz to quit the program")
#Header
firstname=[]
lastname=[]
#names
ni=0 #Number index its like using a forloop inside the while loop but you can change when the index changes when everyou want and you don't have to make a forloop outside the While loop or inside
# this helps me be able to say the students name and tell the students gpa with ez

gpa=[] #gpa list

student="start" #This doesn't need to even have anything but qoutes, but i student a value thats not "done" to have the While loop, instead or having a Break in the code by prefernce
while not student=="done": # runs the while loop
    l= input("What is your last name?").lower()# lower allows
    lastname.append(l.title())
    if l =="zzz":#quits program
        print("GoodBye")
        student="done"
    else:
        f= input("What is your first name?")
        firstname.append(f.title())
        name=(f"{firstname[ni]}, {lastname[ni]}")
        traffic="red" #This makes a red light for anyone who didn't put in their GPA
        while not traffic=="green":#If traffic isn't green, but this text is;Well that means you didn't put the GPA in correctly
            try:
                print("Don't type any letters please")
                g=float(input(f" hi {name} whats your gpa?"))#this is GPA input
                if g<0:#No negative numbers can be on a GPA so i made negative GPA won't add tp the list
                    print("possitive numbers only")
                    continue
                elif g>4.3:
                    print("only 4.3's or lower")#max amount of GPA so you can't type you have like a 23GPA
                    continue
                traffic="green"
                

            except:#Makes sure your GPA has no letters.
                print("make sure you type numbers no letters")
                continue
            gpa.append(g)
            #This is just responses for if someone got a good GPA they a givin a thumbs up  if they have a subpar or bad GPA thier are messages a incouragement and help offerings  
            if gpa[ni]>=3.5:
                print(f"{gpa[ni]} is an awesome GPA {name} You've just qualified for the Dean's list Good Job" )
            elif gpa[ni]>=3.25:
                print(f"{name} You have a {gpa[ni]} GPA good job! You made it to honnor roll  ")
            elif gpa[ni]>=3:
                print(f"Sorry {name} Your {gpa[ni]} GPA is good but didn't make it to honnor roll but you're close and doing well ")
            elif gpa[ni]<2:
                print(f"{name} your {gpa[ni]} needs improvement C'mon!!! I believe you can do better. You need to go to study tables once a week ")
            elif gpa[ni]<3:
                print(f"Hey {name} you have a {gpa[ni]}GPA this might need improvement feel free to visit study tables")
            


        ni=ni+1 #This adds the index so i don't greet the first person constantly
    
