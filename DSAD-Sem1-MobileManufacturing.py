# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 22:15:30 2020

@author: hgupta23
"""

import os
import Mobile

class MobileManufacturing:
    
    def _trackMobiles(self, mobiles, mobile):
        '''This function reads from the inputPS1.txt file the mobile ids, oarts manufactoring and assembly time.
        The input data is used to populate the AVL tree. To apply greedy algorithm to select the mobile 
        ‘parts manufacturing’ and ‘assembling’ in such a way that total production time is minimized,
        AVL tree has been constructed using parts manufacturing time as the key of the tree.
        '''
        mobileData = mobile.split('/')
        if(mobiles is None):
            mobiles = Mobile.MobileTree()
        mobiles.insert(int(mobileData[0]), int(mobileData[1]), int(mobileData[2]))
        return mobiles  
    
    def _displayOrderAndTime(self, mobiles):
        '''This function calculate the production time required to monufacture and assemble all mobiles 
        and total time assembly machine has been idle. Calculated result is stored in outputPS1.txt file.
        '''
        productionOrder = []
        productionTime = 0
        partsRunningTime = 0
        idleTime = 0
        mobile = None
        mobiles = mobiles.inorder_traverse()
        for mobile in mobiles:
            productionOrder.append(mobile.MobileID)
            partsRunningTime += mobile.PartsManufTime
            if productionTime < partsRunningTime:
                #Assembling unit will be idle. Calculating idle time.
                currentIdleTime = partsRunningTime - productionTime
                productionTime += mobile.AssembleTime + currentIdleTime
                idleTime += currentIdleTime
            elif productionTime >= partsRunningTime:
                productionTime += mobile.AssembleTime
        
        rptOut = 'Mobiles should be produced in the order: ' + str(productionOrder)[1:-1] + '\n'    
        rptOut += 'Total production time for all mobiles is: ' + str(productionTime) + '\n'
        rptOut += 'Idle Time of Assembly unit: ' + str(idleTime) + '\n'
        outFile.write(rptOut)
    
    def _closeFiles(self):
        '''
        This will close all the files at end.
        '''
        attFile.close()
        outFile.close()
        
if __name__ == "__main__":
    # Declaring and initializing variables
    mobiles = None
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
        outFile.write("Nothing to process. Mobile manufacturing data file is empty. Thus, Tree is empty \n")

    if inputPS1Empty is False:
        # To get the headcount - This will be print at the start of report by default as given in sample output.
        tracker._displayOrderAndTime(mobiles)
    
    # Closing all the files
    tracker._closeFiles()