'''
Created on Apr 26, 2016

@author: Sue
'''
from oregontrailgame import oregontrailgame
from oregontrailgame import OregonTrail



def main():
    otg = oregontrailgame() #create the object here and pass it to wherever you need it
    OregonTrail(otg).mainloop() #pass the otg to the init
    
main()