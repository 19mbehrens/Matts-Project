import math,random,time;
timerMultiplier = 1 #For slower readers.
print("You wake up with a massive headache, your back to the grass, the sunlight blinding.")
def wait(milliseconds):
    start_time = time.time();
    while 1:
      if time.time() > start_time + (milliseconds / 1000):
        break
def cls(): #Clear screen.
    for i in range(0,100):
        print ("")
wait(5000)
talkstat = 0 #Changes 'talk' command up a bit.
lookstat = 0 #In the cases where you need to look before you can go.
progress = 0 #Allows re-use of the commands and generally shows progress in the game.
look_options = ["look", "observe", "look around"]
move_options = ["walk","run", "move"]
talk_options = ["talk", "speak"]
getup_options = ["stand", "get up", "stand up"]
fight_options = ["attack", "strike", "hit", "fight"]
is_playing = True
while is_playing:
    cls();
    print ("Options:")
    print ("For one who wants to observe: " + ", ".join(look_options))
    print ("If you don't want to stand still: " + ", ".join(move_options))
    print ("For those who arn't silent: " + ", ".join(talk_options))
    print ("If you fall down at any point: " + ", ".join(getup_options))
    print ("If you are attacked: " + ", ".join(fight_options))
    response = raw_input("Input: ")
    if (response.lower() in look_options) and progress == 0:
        print ("Whilst lying down, all you can see is the sky and the tall grass surrounding you.")
        wait(timerMultiplier*2000)
    elif (response.lower() in fight_options) and progress == 0:
        print ("Even if there is something to fight, you should try to get up before looking.")
        wait(timerMultiplier*2750)
    elif (response.lower() in move_options) and progress == 0:
        print ("Your lying on the ground, you should get up before you try to walk.")
        wait(timerMultiplier*2000)
    elif (response.lower() in talk_options) and progress == 0:
        print ("You talk to the sky for a bit. It's not much of a conversationalist.")
        wait(timerMultiplier*2000)
        if talkstat == 0:
            talkstat += 1
    elif (response.lower() in getup_options) and progress == 0:
        print ("You get up, off the ground.")
        progress += 1 #Mark of progress                                                                                  /////
        wait(timerMultiplier*1500)
    elif (response.lower() in look_options) and progress == 1:
        print ("Around you is a grassy plains, in the distance, you can see smoke rising.")
        wait(timerMultiplier*2000)
        lookstat += 1
    elif (response.lower() in getup_options) and progress == 1:
        print ("Your not lying down.")
        wait(timerMultiplier*2000)
    elif (response.lower() in talk_options) and progress == 1:
        if talkstat == 0:
            print ("You talk to the air for a bit. Not much of a conversationalist.")
            talkstat += 1
            wait(timerMultiplier*2000)
        elif talkstat == 1:
            print ("You talk to the air for a bit. Like the sky, doesn't talk much.")
            talkstat += 1
            wait(timerMultiplier*2000)
        else:
            print ("The air didn't have anything to say.")
    elif (response.lower() in fight_options) and progress == 1:
        print ("Nothing is in the area at the moment.")
        wait(timerMultiplier*2000)
    elif (response.lower() in move_options) and progress == 1:
        if lookstat == 1:
            print ("You move towards the rising smoke, hoping to find someone.")
            wait(timerMultiplier*2000)
            progress += 1 #Mark of progress                                                                              /////
            print ("You reach an empty campsite.")
            wait(timerMultiplier*2500)
        else:
            print ("You don't really know where to go.")
            wait(timerMultiplier*2000)
    elif (response.lower() in talk_options) and progress == 2:
        if talkstat == 0:
            print ("You talk to the recently extinguished fire. Doesn't talk much.")
            wait(timerMultiplier*2000)
            talkstat += 3
        elif talkstat == 1:
            print ("You talk to the recently extinguished fire. It doesn't talk that much.")
            wait(timerMultiplier*2500)
            talkstat += 3
        elif talkstat == 2:
            print ("You talk to the recently extinguished fire. Seems like random objects here don't talk.")
            wait(timerMultiplier*3000)
            talkstat += 3
        else:
            print ("Your done talking to the fire.")
            wait (1500)
    elif (response.lower() in fight_options) and progress == 2:
        print ("You see a blob in the distence, but you don't have a weapon to fight with.")
        lookstat += 1
        wait(timerMultiplier*3250)
    elif (response.lower() in move_options) and progress == 2:
        print ("You walk meaninglessly around the camp.")
        wait(timerMultiplier*2000)
    elif (response.lower() in look_options) and progress == 2:
        print ("You look around the camp for something useful.")
        wait(timerMultiplier*2000)
        print ("You find a sword.")
        progress += 1 #Mark of progress                                                                                  /////
        wait(timerMultiplier*1000)
    elif (response.lower() in talk_options) and progress == 3:
        if talkstat == 0:
            print ("You talk to the recently extinguished fire. Doesn't talk much.")
            wait(timerMultiplier*2000)
            talkstat += 3
        elif talkstat == 1:
            print ("You talk to the recently extinguished fire. It doesn't talk that much.")
            wait(timerMultiplier*2500)
            talkstat += 3
        elif talkstat == 2:
            print ("You talk to the recently extinguished fire. Seems like random objects here don't talk.")
            wait(timerMultiplier*3000)
            talkstat += 3
        else:
            print ("Your done talking to the fire.")
            wait (1500)
    elif (response.lower() in look_options) and progress == 3:
        if lookstat == 1:
            print ("You look around the perimeter of the camp, and spot a blob-like creature.")
            lookstat += 1
            wait(timerMultiplier*2500)
        else:
            print ("You've already searched everywhere.")
            wait(timerMultiplier*1500)
    elif (response.lower() in move_options) and progress == 3:
        print ("You pace around the campsite a few times, wondering what to do next.")
        wait(timerMultiplier*3000)
    elif (response.lower() in fight_options) and progress == 3:
        if lookstat == 1:
            print ("You wave your sword around menacingly.")
            wait(timerMultiplier*2000)
        else:
            print ("You engage the blob-like thing.")
            progress += 1 #Mark of Progress                                                                              /////
            wait(timerMultiplier*1500)
            print ("(In battle, attack, strike, etc = attacking and move, walk, run = dodging.)")
            wait(timerMultiplier*3500)
    elif (response.lower() in move_options) and progress == 4:
        print ("You move to the side. The blob wasn't moving towards you anyway.")
        wait(timerMultiplier*2250)
    elif (response.lower() in talk_options) and progress == 4:
        print ("Now isn't the best time to try to talk.")
        wait(timerMultiplier*1500)
    elif (response.lower() in look_options) and progress == 4:
        print ("It appears to not care about what you're doing.")
        wait(timerMultiplier*2000)
    elif (response.lower() in fight_options) and progress == 4:
        print ("You swing at the blob, aiming to cut it in half.")
        wait(timerMultiplier*1500)
        print ("The slash itself didn't seem to do anything, but you see a heart-shaped gem in the centre. That may be its weakpoint!")
        progress += 1 #Mark of Progress                                                                                  /////
        wait (5250)
    elif (response.lower() in look_options) and progress == 5:
        print ("It still doesn't seem to care about what you're doing.")
        wait(timerMultiplier*2500)
    elif (response.lower() in move_options) and progress == 5:
        print ("You move to the side. The blob wasn't moving towards you anyway.")
        wait(timerMultiplier*2250)
    elif (response.lower() in talk_options) and progress == 5:
        print ("Now isn't the best time to try to talk.")
        wait(timerMultiplier*2000)
    elif (response.lower() in fight_options) and progress == 5:
        print ("You cut deeper into the blob, hitting the gem.")
        wait(timerMultiplier*1500)
        print ("The gem cracks, and the blob spazzes and jerks uncontrollably. Afterwards, it readies for attack.")
        progress += 1 #Mark of Progress                                                                                  /////
        wait(timerMultiplier*3000)
    elif (response.lower() in move_options) and progress == 6:
        print ("The blob charges at you, but you move to the side.")
        wait(timerMultiplier*2000)
        print ("It moves right past you, slowing to a stop.")
        wait(timerMultiplier*2000)
    elif (response.lower() in look_options) and progress == 6:
        print ("It seems angry.")
        wait(timerMultiplier*1000)
    elif (response.lower() in talk_options) and progress == 6:
        print ("Now it really seems like its not a good time to talk.")
        wait(timerMultiplier*3000)
    elif (response.lower() in fight_options) and progress == 6:
        print ("You strike at the blob again.")
        wait(timerMultiplier*1500)
        print ("The gem shatters, and the blob loses consistency, melting on the spot.")
        wait(timerMultiplier*3000)
        print ("Oddly enough, you find coins where the blob used to be.")
        wait(timerMultiplier*2500)
        progress += 1 #Mark of Progress                                                                                  /////
        break
    else: #not in an option
        print ("Command Unacceptable.")
        wait(timerMultiplier*1000)
print ("progress:", progress)