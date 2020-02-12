# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 22:15:30 2020

@author: hgupta23
"""

import os
import Mobile

class MobileManufacturing:
    
    def _trackMobiles(self, mobiles, mobile):
        '''This function reads from the inputPS1.txt file the ids of employees entering and leaving the organization premises. 
        One employee id should be populated per line (in the input text file) indicating their swipe (entry or exit). 
        The input data is used to populate the tree. If the employee id is already added to the tree, 
        then the attendance counter is incremented for every subsequent occurrence of that employee id in the input file. 
        Use a trigger function to call this recursive function from the root node.
        '''
        mobileData = mobile.split('/')
        if(mobiles is None):
            mobiles = Mobile.MobileTree()
        mobiles.insert(int(mobileData[0]), int(mobileData[1]), int(mobileData[2]))
        return mobiles  
    
    def _displayMobiles(self, mobiles):
        '''This function reads from the inputPS1.txt file the ids of employees entering and leaving the organization premises. 
        One employee id should be populated per line (in the input text file) indicating their swipe (entry or exit). 
        The input data is used to populate the tree. If the employee id is already added to the tree, 
        then the attendance counter is incremented for every subsequent occurrence of that employee id in the input file. 
        Use a trigger function to call this recursive function from the root node.
        '''
        mobileOrder = mobiles.inorder_traverse()
        print('Mobiles should be produced in the order: ' + str(mobileOrder)[1:-1])
        rptOut = 'Mobiles should be produced in the order: ' + str(mobileOrder)[1:-1] + '\n'
        outFile.write(rptOut)
    
    def _displayProductionTme(self, mobiles):
        '''This function reads from the inputPS1.txt file the ids of employees entering and leaving the organization premises. 
        One employee id should be populated per line (in the input text file) indicating their swipe (entry or exit). 
        The input data is used to populate the tree. If the employee id is already added to the tree, 
        then the attendance counter is incremented for every subsequent occurrence of that employee id in the input file. 
        Use a trigger function to call this recursive function from the root node.
        '''
        productionTme = 0
        print('Total production time for all mobiles is: ' + str(productionTme))
        rptOut = 'Total production time for all mobiles is: ' + str(productionTme) + '\n'
        outFile.write(rptOut)
    
    def _displayAssemblyIdleTme(self, mobiles):
        '''This function reads from the inputPS1.txt file the ids of employees entering and leaving the organization premises. 
        One employee id should be populated per line (in the input text file) indicating their swipe (entry or exit). 
        The input data is used to populate the tree. If the employee id is already added to the tree, 
        then the attendance counter is incremented for every subsequent occurrence of that employee id in the input file. 
        Use a trigger function to call this recursive function from the root node.
        '''
        idleTme = 0
        print('Idle Time of Assembly unit: ' + str(idleTme))
        rptOut = 'Idle Time of Assembly unit: ' + str(idleTme) + '\n'
        outFile.write(rptOut)
    
    def _closeFiles(self):
        '''
        This will close all the files at end.
        '''
        attFile.close()
        outFile.close()
        
if __name__ == "__main__":
    # Declaring and initializing variables
    Eid = 0
    eId = 0
    mobiles = None
    StartId = 0
    EndId = 0
    inputPS1Empty = False

    # Creating instance of Main class
    tracker = MobileManufacturing()
    
    # Creating outPut file
    outFile = open(r'data\outputPS1.txt','w')
    
    # Reading inputPS1 file to load the day's swipe in/out data and populate the Binary Tree
    attFile = open(r'data\inputPS1.txt','r')
    if os.stat(r'data\inputPS1.txt').st_size != 0:
        for mobile in attFile.readlines():
            mobiles = tracker._trackMobiles(mobiles, str(mobile))
    else:
        inputPS1Empty = True
        outFile.write("Nothing to process. Swipe data file is empty. Thus, Tree is empty \n")

    if inputPS1Empty is False:
        # To get the headcount - This will be print at the start of report by default as given in sample output.
        tracker._displayMobiles(mobiles)
        tracker._displayProductionTme(mobiles)
        tracker._displayAssemblyIdleTme(mobiles)
    
    # Closing all the files
    tracker._closeFiles()