

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 15:41:30 2019

@author: bjopet
"""




import random
     
     
def num(z): # Updating the numbers of dices to roll
    l = 1
    
    new_lst5 = []
    print(z, 'Inside the function that will update the list of dices')
    #print(new_lst2, "This is new lst2")
    for q in range(z):
        new_lst5.append(l) # Need to create a new list to compare with old and removing the difference
        l += 1
    print(new_lst5)
    #print(len(new_lst5))
    h = len(new_lst5) # Number to remove from list
    print(h)
    for e in range(h): # Removing from 
        list
        new_lst2.pop()
        print(new_lst2, "This is new_lst2")
        '''
        Gör en till klass som kan retuneras om inte lst_2 har ändrats
        dom får jämföras och om new_lst2 != lstX så är det den som gäller
        '''
        
    return new_lst2
        
 
 
 
class Roll:
    """ This class is only rolling the dices,
    """
 
    def __init__(self, dice, new_lst, dict1, new_dict1, new_lst2):
        dice_num = new_lst2
        self.dice_num = dice_num
        #self.dice_value = dic_value
        self.new_lst = new_lst
        self.dict1 = dict1
        self.new_dict1 = new_dict1
        print("Let's see what the dices are showing")
        for x in dice_num:
            x = random.randint(1, 6)
            print(x)
            self.new_lst.append(x) # added self to indicate that's a class' attribute
 
 
class SelectDices(Roll):
    global z # Making it global so it can be used outside
    
    """ This class is for displaying and selecting the dices
    """
    def __init__(self):
        #self.dice_value = dice_value
        self.lat = []
        self.bi = []
        self.left_dices = {}
        Roll.__init__(self, dict, new_lst, dict1, new_dict1, new_lst2)
        print("The dices has been rolled!!!")
 
        self.dict1 = dict(zip(dice, new_lst))  # Creating a dictonary from dice and new_lst
 
 
        for key, value in self.dict1.items():
            self.new_dict1.setdefault(value, set()).add(key)
 
        self.dict1 = {}
        
 
        for key, value in self.new_dict1.items():  
            if  len(value) > 1 and len(value) < 3: # If user has 2 dices with same and not more
                print("you have a a pair of: %s with dices: %r" % (key, value))
                suum = key * 2
                print("This is worth {}".format(suum), 'points')
                self.lat.append(key)
                self.bi.append(value)
                # print(self.bi, self.lat)
                self.left_dices = dict(zip(self.lat, self.bi)) 
                print(self.left_dices, "pair")
                self.dice_value = 2
            
            elif len(value) > 2 and len(value) < 4: # If user has three of a kind
                print("you have three of a kind: %s with dices: %r" % (key, value))
                suum = key * 3
                print("This is worth {}".format(suum), 'points')
                self.lat.append(key)
                self.bi.append(value)
                # print(self.bi, self.lat)
                self.left_dices = dict(zip(self.lat, self.bi))
                print(self.left_dices, "three of a kind")
                self.dice_value = 3
               
            elif len(value) > 3: # If user has four of a kind
                print("You have four of a kind: %s with dices: %r" % (key, value))
                suum = key * 4
                print("This is worth {}".format(suum), 'points')
                self.lat.append(key)
                self.bi.append(value)
                # print(self.bi, self.lat)
                self.left_dices = dict(zip(self.lat, self.bi))
                print(self.left_dices, "four of a kind")
                self.dice_value = 4
                
            elif len(value) < 1: # If user has nothing (ToDo save highest dice value...)
                print("You have nothing...")
                suum = key * 0
                
                self.lat.append(key)
                self.bi.append(value)
                # print(self.bi, self.lat)
                self.left_dices = dict(zip(self.lat, self.bi))
                
                self.dice_value = 0
 
        val = input('Do you want to save them? (y/n)')
 
 
        if val == 'y':
            print('ok \n')  # ToDo
 
 
        elif val == 'n':
            print('okidoki \n')  # ToDo
 
        else:
            print('Please select y/n \n') #ToDo
 
    def ret(self,):
        
        global z # added to point to z by reference, making it to change the global variable.
        z = self.dice_value
        print('{}'.format(z), "dices to save")
       
        
        
        return z #Returning the value
 
 
 
if __name__ == "__main__":
    
    z = 0 # added to recognize it inside of the functions
    print("Welcome to Yatzy!!!")
    dice = ['Dice1', 'Dice2', 'Dice3', 'Dice4', 'Dice5']
    new_lst = []
    new_lst2 = [1,2,3,4,5]
    new_dict1 = {}
    dict1 = {}
    s = SelectDices()
    s.ret()

    num(z) 
    print(new_lst2,'This is how many dices left')

