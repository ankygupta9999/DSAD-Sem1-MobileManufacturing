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
            print("Inserted Mobile [" + str(MobileID) + "]")
        
        elif PartsManufTime < tree.PartsManufTime: 
            self.MobileNode.left.insert(MobileID, PartsManufTime, AssembleTime)
            
        elif PartsManufTime >= tree.PartsManufTime: 
            self.MobileNode.right.insert(MobileID, PartsManufTime, AssembleTime)
        
        else: 
            print("Mobile [" + str(MobileID) + "] could not be inserted in tree.")
            
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
        print ('Rotating ' + str(self.MobileNode.MobileID) + ' right') 
        A = self.MobileNode 
        B = self.MobileNode.left.MobileNode 
        T = B.right.MobileNode 
        
        self.MobileNode = B 
        B.right.MobileNode = A 
        A.left.MobileNode = T 

    
    def lrotate(self):
        # Rotate left pivoting on self
        print ('Rotating ' + str(self.MobileNode.MobileID) + ' left') 
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

    def delete(self, key):
        # debug("Trying to delete at node: " + str(self.MobileNode.key))
        if self.MobileNode != None: 
            if self.MobileNode.key == key: 
                print("Deleting ... " + str(key))  
                if self.MobileNode.left.MobileNode == None and self.MobileNode.right.MobileNode == None:
                    self.MobileNode = None # leaves can be killed at will 
                # if only one subtree, take that 
                elif self.MobileNode.left.MobileNode == None: 
                    self.MobileNode = self.MobileNode.right.MobileNode
                elif self.MobileNode.right.MobileNode == None: 
                    self.MobileNode = self.MobileNode.left.MobileNode
                
                # worst-case: both children present. Find logical successor
                else:  
                    replacement = self.logical_successor(self.MobileNode)
                    if replacement != None: # sanity check 
                        print("Found replacement for " + str(key) + " -> " + str(replacement.key))  
                        self.MobileNode.key = replacement.key 
                        
                        # replaced. Now delete the key from right child 
                        self.MobileNode.right.delete(replacement.key)
                    
                self.rebalance()
                return  
            elif key < self.MobileNode.key: 
                self.MobileNode.left.delete(key)  
            elif key > self.MobileNode.key: 
                self.MobileNode.right.delete(key)
                        
            self.rebalance()
        else: 
            return 

    def logical_predecessor(self, node):
        ''' 
        Find the biggest valued node in LEFT child
        ''' 
        node = node.left.MobileNode 
        if node != None: 
            while node.right != None:
                if node.right.MobileNode == None: 
                    return node 
                else: 
                    node = node.right.MobileNode  
        return node 

    def logical_successor(self, node):
        ''' 
        Find the smallese valued node in RIGHT child
        ''' 
        node = node.right.MobileNode  
        if node != None: # just a sanity check  
            
            while node.left != None:
                print("LS: traversing: " + str(node.key))
                if node.left.MobileNode == None: 
                    return node 
                else: 
                    node = node.left.MobileNode  
        return node 

    def check_balanced(self):
        if self == None or self.MobileNode == None: 
            return True
        
        # We always need to make sure we are balanced 
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.MobileNode.left.check_balanced() and self.MobileNode.right.check_balanced())  
        
    def inorder_traverse(self):
        if self.MobileNode == None:
            return [] 
        
        inlist = [] 
        l = self.MobileNode.left.inorder_traverse()
        for i in l: 
            inlist.append(i) 

        inlist.append(self.MobileNode.MobileID)

        l = self.MobileNode.right.inorder_traverse()
        for i in l: 
            inlist.append(i) 
    
        return inlist 

    def display(self, level=0, pref=''):
        '''
        Display the whole tree. Uses recursive def.
        TODO: create a better display using breadth-first search
        '''        
        self.update_heights()  # Must update heights before balances 
        self.update_balances()
        if(self.MobileNode != None): 
            print ('-' * level * 2, pref, self.MobileNode.MobileID, "[" + str(self.height) + ":" + str(self.balance) + "]", 'L' if self.is_leaf() else ' '    )
            if self.MobileNode.left != None: 
                self.MobileNode.left.display(level + 1, '<')
            if self.MobileNode.left != None:
                self.MobileNode.right.display(level + 1, '>')