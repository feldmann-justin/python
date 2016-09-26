'''
Created on Mar 29, 2016

@author: bf197158
'''

from tkinter import *
import globalVars

class OregonTrail(Frame):
    def __init__(self, otg):
        
        '''Sets up the window and widgets.'''
        Frame.__init__(self)
        self.master.title("Oregon Trail")
        self.master.geometry('649x780')
        self.grid()
        
        self._gif1 = PhotoImage(file = 'oregontrail.gif')
        self._imageLabel = Label(self, image = self._gif1)
        self._imageLabel.grid(row = 0, column = 0, columnspan = 3, sticky = N+W)
        
        self._textOutput = Text(self,
                               width = 80,
                               height = 30,
                               wrap = WORD,
                               bg = '#006bff',
                               fg = 'white')
        self._textOutput.grid(row = 1, column = 0, columnspan = 3, sticky = W+E+N+S)
        self._textOutput.rowconfigure(0, weight = 2)
        self._textOutput.columnconfigure(0, weight = 2)
                
        self._choiceLabel = Label(self,
                                  text = "Make your choice below: ")
        self._choiceLabel.grid(row = 2, column = 1)
        
        '''Sets up the option buttons.'''
        self._oneBtn = Button(self, text = "1", command = lambda: self._one(otg))
        self._oneBtn.config(font = ('helvetica', 15))
        self._oneBtn.grid(row = 3, column = 0)
        
        self._twoBtn = Button(self, text = "2", command = lambda: self._two(otg))
        self._twoBtn.config(font = ('helvetica', 15))
        self._twoBtn.grid(row = 3, column = 1)
        
        self._threeBtn = Button(self, text = "3", command = lambda: self._three(otg))
        self._threeBtn.config(font = ('helvetica', 15))
        self._threeBtn.grid(row = 3, column = 2)
        
        self._write(otg.intro())
     
    def _one(self, otg):
        if globalVars.stepNum == 1:
            self._write(otg.step1(1))
        elif globalVars.stepNum == 2:
            self._write(otg.step2(1))
        elif globalVars.stepNum == 3:
            self._write(otg.step3(1))
        elif globalVars.stepNum == 4:
            self._write(otg.step4(1))
        elif globalVars.stepNum == 5:
            self._write(otg.step5(1))
        elif globalVars.stepNum == 6:
            self._write(otg.step6(1))
        elif globalVars.stepNum == 7:
            self._write(otg.step7(1))
        elif globalVars.stepNum == 8:
            self._write(otg.step8(1))
            
    def _two(self, otg):
        if globalVars.stepNum == 1:
            self._write(otg.step1(2))
        elif globalVars.stepNum == 2:
            self._write(otg.step2(2))
        elif globalVars.stepNum == 3:
            self._write(otg.step3(2))
        elif globalVars.stepNum == 4:
            self._write(otg.step4(2))
        elif globalVars.stepNum == 5:
            self._write(otg.step5(2))
        elif globalVars.stepNum == 6:
            self._write(otg.step6(2))
        elif globalVars.stepNum == 7:
            self._write(otg.step7(2))
        elif globalVars.stepNum == 8:
            self._write(otg.step8(2))
    
    def _three(self, otg):
        if globalVars.stepNum == 1:
            self._write(otg.step1(3))
        elif globalVars.stepNum == 2:
            self._write(otg.step2(3))
        elif globalVars.stepNum == 3:
            self._write(otg.step3(3))
        elif globalVars.stepNum == 4:
            self._write(otg.step4(3))
        elif globalVars.stepNum == 5:
            self._write(otg.step5(3))
        elif globalVars.stepNum == 6:
            self._write(otg.step6(3))
        elif globalVars.stepNum == 7:
            self._write(otg.step7(3))
        elif globalVars.stepNum == 8:
            self._write(otg.step8(3))
            
    def _write(self, txt):
        #self.output.insert()
        self._textOutput.delete(1.0, END) #Clears the text field
        self._textOutput.insert(1.0, txt)

##################################################################################

class oregontrailgame():
        
    def __init__(self):
        #ot = OregonTrail()
        return
        
    #ot = OregonTrail
    def intro(self):
        return "\nThis is Oregon Trail (sorta), and it is very ironic. Don't get butt hurt. If you select the incorrect answer, click the other options instead until you happen upon the correct one. This is more of a comedic game, so we hope you enjoy.\nThere is a river, do you:\n1. ford the river\n2. build a raft and cross\n3. go downstream to find a more shallow crossing"
    
    def step1(self, btnNum):
        while True:                     #first step of the journey
            if btnNum == 1:
                return "\nYou drowned, dingus!"              
            
            elif btnNum == 2:
                globalVars.stepNum += 1
                return "\nYou made it across but are dying of dysentery, tweedle dongus!\nYou might be able to get rid of your dysentary, do you:\n1. eat dirt\n2. throw up"
                #return stepNum
                
            elif btnNum == 3:
                return "\nYou made it across the river but later die of pneumonia, tweedle dingus!"
            '''
            while btnNum != 2:
                break
            '''
    def step2(self, btnNum):
        while True:    #second step of the journey
            if btnNum == 1:
                globalVars.stepNum += 1
                return "\nYou're now cured and will continue on your journey.\nYou continue past the river, and the hershey squirts, but you are attacked by a bear. Do you:\n1. Climb a tree\n2. Fight the bear\n3. Run around until your wife can load the gun and shoot the bear"
                    
            elif btnNum == 2:
                return "\nWay to go! You're dehydrated even MORE! You're sure to die now! GAME OVER!"
                
            while btnNum != 1:
                break
    
       
    def step3(self, btnNum):
        while True:      #third step of journey
            if btnNum == 1:
                globalVars.stepNum += 1
                return "\nYou climb a tree and watch as your wife is eaten by the bear.\nWomen are worthless during this century anyway, so it's ok.\nYou continue on, stepping over the skeletal remains of your wife, towards Oregon.\nThis game is horribly depressing. Why would people go to Oregon with all this stuff happening?\nMove to Missouri! There are still large plots of nothing and it's 2016!\nYou could've just stayed here, but 'NOOOOOOO I want to go to Oregon'. You're dumb!\n\nAnyway, you drive your wagon continually west until you come upon a family of Oregon bound people. Do you:\n1. Shoot them all in the head with your gun\n2. Take them on as fellow travelers, while also serving the ulterior motive of consoling yourself for your wife's death which you could've prevented if you had kept your gun loaded\n3. Continue on past them giving a friendly nod to their jail-bait daughter"
                
            elif btnNum == 2:
                return "\nWhat are you, STUPID? You're on your way to Oregon. Grizzly bears live here, you can't beat up a grizzly bear!\nYou died, dummy. GAME OVER!"
                
            elif btnNum == 3:
                return "\nDon't you know women can't do anything right? Your wife failed to load the gun, OBVIOUSLY, and you died. Then some Indians came by and saved her.\n Now she lives with them, happy, and you're dead. Maybe you should keep your gun loaded, stupid! You're dead. GAME OVER!"
                
            while btnNum != 1:
                break  
        
    def step4(self, btnNum):
        while True:    #fourth step of journey
            if btnNum == 1:
                return "You shoot them all in the head and continue on, and are later hanged for your crime. GAME OVER, JERK!"
                    
            elif btnNum == 2:
                globalVars.stepNum += 1
                return "You take them on as fellow travelers. A few days later, the father of their family dies of a broken leg. You take them as your own family. Yay, new family!\nYou and your new family decide to stop at Fort Bridger in Wyoming to rest and form new emotional bonds.\nYou decide to play a game of cards to show your new family that you are fun.\nDo you:\n1. cheat\n2.let the kids win \n3. play fair"
            
            elif btnNum == 3:
                return "The daughter nods back and grins. Her father notices this, and pulls out his gun that he keeps LOADED because he isn't dumb and he shoots you. You're dead because you're a creep. GAME OVER!"
                   
            while btnNum != 2:
                break
            
    def step5(self, btnNum):
        while True:    #fifth step of journey
            if btnNum == 1:
                return "Why would you cheat, you jerk?! You are trying to get these people to like you! Your wife sees that you are a jerk\nand since she can't divorce you, she poisons you and gets another new husband at the fort. GAME OVER, JERK!"
                      
            elif btnNum == 2:
                return "Your new children know that you are letting them win and decide that you are a push over. They make you buy a dog which gets rabies and bites you. You die! GAME OVER!"
            
            elif btnNum == 3:
                globalVars.stepNum += 1
                return "Your new family forms a new level of respect for you. They all yell 'Yay, new dad is cool!' while looking as happy as the stereotypical nuclear family you'd find on a Jenga game box.\nYou and your new family leave Fort Bridger to continue on to Oregon. You're sort of almost there. You're walking along and you are attacked by a tribe of Injuns.\nWhat do you do?\nDo you\n1: attempt to trade with them\n2: fight them\n3: offer them a child sacrifice"
            
            while btnNum != 3:
                break
            
    def step6(self, btnNum):
        while True:     #sixth step of journey
            if btnNum == 1:
                return "\nWhat?! You think you can buy your freedom with TRINKETS?!?! You get hit in the head with a tomahawk and your family is taken prisoner. Way to go! GAME OVER, JERK!"
                      
            elif btnNum == 2:
                return "\nI just said a TRIBE of Injuns. There are way too many to fight! You're shot in the neck with 10 arrows and collapse, dead. GAME OVER, LOSER!"
                    
            elif btnNum == 3:
                globalVars.stepNum += 1
                return "\nThe Injuns approach with their war cry and you hold up your youngest son like Simba in Lion King. The war party halts and looks at the son and at you, back and forth.\nThey take the baby and ride away. It's ok though, because later that week the guys from Fort Bridger massacre them and they recover the baby.\nA few years later you're reunited with him so it's all good. But for now you continue on, sad.\nYou and your new family are pretty bummed out about having sacrificed your youngest\nfamily member, although they know it was the only thing to do. They look to you for guidance.\nWhat do you do?\nDo you:\n1. turn to alcohol for solace\n2. go three wagon trains over to get counseling from the pastor there\n3. cry... ALOT"
            
            while btnNum != 3:
                break        
    
    def step7(self, btnNum):
        while True:    #seventh step of journey
            if btnNum == 1:
                return "\nYou drink two bottles of whiskey, go out and get into a fight with the town hard-ass. It escalates quickly, and he challenges you to a gun duel. The next day at high noon he shoots you in the face. You're dead. GAME OVER!"
                     
            elif btnNum == 2:
                globalVars.stepNum += 1
                return "\nYou and your family decide the best way of coping is to seek professional help.\nYou all think it is worth going a bit out of your way from your trek to Oregon to see the local town's pastor.\nThe pastor, once he listens to your tale, says 'something something Lord forgives you, something something forgive yourself'.\n You silently groan, 'Now I remember why I never paid attention in church...'\nRelieved, you all continue on, and are nearing the Wyoming-Idaho border when a figure begins to seep over the horizon.\nWeary, but unwilling to be deterred, you move on, and as your family and the figure get closer, you see...\n1. the presumed-dead father of your new family\n2. a successful prospector returning home with his gold\n3. a mirage"
                
            elif btnNum == 3:
                return "\nTears?! Tear ducts weren't even invented until the hippie revolution in the 1960s.\nYou're simply hallucinating after eating a couple of wild peppers.\nIn reality, there's a severe downpour and you're smack dab in the middle of it! You're actually drowning. GAME OVER!"
            
            while btnNum != 2:
                break
                     
    def step8(self, btnNum):
        while True:     #eighth step of journey
            if btnNum == 1:
                return "\nThe father apparently had faked his death in order to avoid being killed over stealing a local Indian chief's headdress, an act unbeknownst to his family.\nSeeing your new tight-knit relationship with his ex-wife and children, he seems to be proud and a bit jealous of your success.\nYou agree to let him journey with the rest of you all for a while, but your kindness backfires when, as you lay sleeping, the aforementioned Indian tribe finds you with the stolen headdress atop your head. You are executed by horse-quartering. GAME OVER!"
            
            elif btnNum == 2:
                globalVars.stepNum += 1
                return "The figure turns out to be a prospector who recently struck it rich in California and is headed back home to Texas. Why he took the scenic route, he doesn't say. He exclaims he doesn't really need the money, as his father is a well-off oil tycoon. He says he just made the trip for the thrill of it\n*cue canned laughter as your family all look at each other with exhausted glares* The man notices the awful shape you all are in, and as a wonderfully kind gesture, he offers to give you the majority of his find. Quite obviously stunned, you at first hesitate but accept it.\nAfter all, what the hell are you all going out to Oregon for, anyway? The fun of it? I think that aspect of this trip was over a looooooooooooong time ago...\nNevermind that, even if you went to Oregon, you'd still be hundreds of miles away from the nearest gold mine.\nYou seriously need better planning next time around!\nAnyways......\n\n\nYOU WIN!!!\nThe gentleman hitches a ride with you and you all head back home with him as your guide. The end."
            
            elif btnNum == 3:
                return "\nThe figure was nothing but a tumbleweed blowing in your direction. You all are severely dehydrated!\nJeez, dude, how hard can it really be to pack a few canteens of liquids with you?! Is it just you couldn't be bothered or what?\nWell, if it was, you see where that got you all now, huh? GAME OVER!"
    

