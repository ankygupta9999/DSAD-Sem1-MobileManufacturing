# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 22:25:47 2020

@author: hgupta23
"""

class MobileNode:
    def __init__(self, MobileID, PartsManufTime, AssembleTime):
        self.MobileID = MobileID
        self.PartsManufTime = PartsManufTime
        self.AssembleTime = AssembleTime
        self.left = None 
        self.right = None

class MobileTree():
    def __init__(self):
        self.MobileNode = None 
        self.height = -1  
        self.balance = 0;
                
    def height(self):
        if self.MobileNode: 
            return self.MobileNode.height 
        else: 
            return 0 
    
    def is_leaf(self):
        return (self.height == 0) 
    
    def insert(self, MobileID, PartsManufTime, AssembleTime):
        tree = self.MobileNode
        
        newMobileNode = MobileNode(MobileID, PartsManufTime, AssembleTime)
        
        if tree == None:
            self.MobileNode = newMobileNode 
            self.MobileNode.left = MobileTree() 
            self.MobileNode.right = MobileTree()
        
        elif PartsManufTime < tree.PartsManufTime: 
            self.MobileNode.left.insert(MobileID, PartsManufTime, AssembleTime)
            
        elif PartsManufTime > tree.PartsManufTime: 
            self.MobileNode.right.insert(MobileID, PartsManufTime, AssembleTime)
        else:
            if AssembleTime > tree.AssembleTime:
                self.MobileNode.left.insert(MobileID, PartsManufTime, AssembleTime)
            else:
                self.MobileNode.right.insert(MobileID, PartsManufTime, AssembleTime)
            
            
        self.rebalance() 
        
    def rebalance(self):
        ''' 
        Rebalance a particular (sub)tree
        ''' 
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1:
                if self.MobileNode.left.balance < 0:  
                    self.MobileNode.left.lrotate() # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()
                
            if self.balance < -1:
                if self.MobileNode.right.balance > 0:  
                    self.MobileNode.right.rrotate() # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()
 
    def rrotate(self):
        # Rotate left pivoting on self
        #print ('Rotating ' + str(self.MobileNode.MobileID) + ' right') 
        A = self.MobileNode 
        B = self.MobileNode.left.MobileNode 
        T = B.right.MobileNode 
        
        self.MobileNode = B 
        B.right.MobileNode = A 
        A.left.MobileNode = T 

    
    def lrotate(self):
        # Rotate left pivoting on self
        #print ('Rotating ' + str(self.MobileNode.MobileID) + ' left') 
        A = self.MobileNode 
        B = self.MobileNode.right.MobileNode 
        T = B.left.MobileNode 
        
        self.MobileNode = B 
        B.left.MobileNode = A 
        A.right.MobileNode = T 

    def update_heights(self, recurse=True):
        if not self.MobileNode == None: 
            if recurse: 
                if self.MobileNode.left != None: 
                    self.MobileNode.left.update_heights()
                if self.MobileNode.right != None:
                    self.MobileNode.right.update_heights()
            
            self.height = max(self.MobileNode.left.height,
                              self.MobileNode.right.height) + 1 
        else: 
            self.height = -1 

    def update_balances(self, recurse=True):
        if not self.MobileNode == None: 
            if recurse: 
                if self.MobileNode.left != None: 
                    self.MobileNode.left.update_balances()
                if self.MobileNode.right != None:
                    self.MobileNode.right.update_balances()

            self.balance = self.MobileNode.left.height - self.MobileNode.right.height 
        else: 
            self.balance = 0 
    
    def inorder_traverse(self):
        if self.MobileNode == None:
            return [] 
        
        inlist = [] 
        l = self.MobileNode.left.inorder_traverse()
        for i in l: 
            inlist.append(i) 

        inlist.append(self.MobileNode)

        l = self.MobileNode.right.inorder_traverse()
        for i in l: 
            inlist.append(i) 
    
        return inlist 