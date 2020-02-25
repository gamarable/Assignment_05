#------------------------------------------#
# Title: CDInventory.py
# Desc: Script CDINventory to store CD Inventory data
# Change Log: (Who, When, What)
# GMarable, 2020-Feb-18, Created 
# Gmarable, 2020-Feb-23, File Modified to Assignment05
# 
#------------------------------------------#



strChoice = '' # User input
lstTbl = []  # list of lists to hold data
lstTbl2 = []
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object


# ---   MAIN MENU   --- #

print('CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('\n[1] Read Inventory from CDInventory.txt\n[2] Add CD\n[3] Write Data to File')
    print('[4] Load current CD\'s in Memory\n[5] Delete options\n[0] exit')
    strChoice = input('Type 1-5 or 0 and press \'Enter\': ').lower()  # convert choice to lower case at time of input
    print()
    
    # ---   Exit main while loop   --- #

    if strChoice == '0':
        break
    
    # ---   Read data from CDInventory.txt   --- #
    # Pulls the inventory and formats it into a dictionary and assigns it to lstTbl
    # With open opens the file and closes it when it's done. No need for objFile.close()
            
    if strChoice == '1':
        lstTbl.clear
        with open(strFileName, 'r') as objFile:
            for row in objFile:
                lstRow =  row.strip().split(',')
                dicRow = {'ID': int(lstRow[0]), 'Artist': lstRow[1], 'Album': lstRow[2]}
                lstTbl.append(dicRow)
                print(dicRow)                
        pass

    
    # ---   Add data to lstTbl to be saved later   --- #
    # Formats user input and stores it in memory
    # Append adds it on top of what is already in memory
    
    elif strChoice == '2':
        strID = int(input('Enter ID Number: '))
        strArtist = input('Enter the Artist\'s Name: ')
        strAlbum = input('Enter the Album Title: ')
        intID = int(strID)
        dicRow = {'ID': intID, 'Artist': strArtist, 'Album': strAlbum}
        lstTbl.append(dicRow)
        pass
    
    # ---   Write information from memory to CDInventory.txt   --- #
    # Uses with open
    # Processes the informatio with a nested for loop 
    # Writes the formated info to objFile
    
    elif strChoice == '3':
        # 3. Display the current data to the user each time the user wants to display the data
        with open(strFileName, 'w') as objFile:
            for row in lstTbl:
                strRow = ''
                for item in row.values():
                    strRow += str(item) + ','
                strRow = strRow[:-1] + '\n'
                objFile.write(strRow)
    
    # ---   Show data loaded into memory   --- #
    # Takes whatever is in lstTbl and assigns it to lstTble2
    # Keeps my lstTbl data formated the way I want it 
    # Format lstTbl2 to a more digestible way and display it
    
    elif strChoice == '4':
        lstTbl2 = lstTbl
        print('ID, Artist, Album')
        for row in lstTbl2:
            print(*row.values(), sep = ', ')
          
    # ---   Delete menu   --- #   
    
    elif strChoice == '5':
                
        # ---   New while loop for delete menu   --- #
        # Gives options for deleting items or deleting everything
        while True:
            print('\n[l] List all current enteries\n[2] Delete a single entry\n[3] Delete all entries\n[4] Return')
            usrChoice1 = input('Select from 1 to 4 and press Enter: ')
            
            # ---   Exit the second while loop   --- #
            
            if usrChoice1 == '4':
                break
            
            # ---   Show data loaded into memory   --- #
            # Same basic idea as in the main loop
            
            if usrChoice1 == '1':
                lstTbl2 = lstTbl
                print('ID, Artist, Album')
                for row in lstTbl2:
                    print(*row.values(), sep = ', ')
            
            # ---   Delete single item in lstTble   --- #
            # Deletes one item but does not save the result
            
            if usrChoice1 == '2':
                #elitem = None
                delitem = int(input('Enter CD ID to delete: ')) - 1
                print(lstTbl2)
                with open(strFileName, 'r') as objFile:
                    lstTbl.pop(delitem)
                    print('\nDeleted ID - ',delitem)
                    

            # ---   Delete everything menu   --- #
            # Wanted to give an option to delete everything
            # Probably an easier way to do this
            
            if usrChoice1 == '3':
                 while True:
                     usrChoice2 = input('Are you sure you want to delete all of your entries?'
                                        '\n\nType \'Yes\' or \'No\' and press Enter: ').lower()
                     print('\n[Yes] Delete all entries\n[No] Return')
                     
                     # ---   Confirm with a typed yes or no   --- #
                     
                     if usrChoice2 == 'yes':
                         with open(strFileName, 'r') as objFile:
                             lstTbl.clear()
                             print('\nAll CD inventory deleted and file saved')
                             break
                             break 
                        
                     if usrChoice2 == 'no':
                         break
                        
    else:
        print('Please choose either 1, 2, 3, 4, 5 or 0!')