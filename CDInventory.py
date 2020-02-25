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

print('CD Inventory\n')
while True:
    print('\n[1] Read Inventory from CDInventory.txt\n[2] Add CD\n[3] Write Data to File')
    print('[4] Load current CD\'s in Memory\n[5] Delete options\n[0] exit')
    strChoice = input('Type 1-5 or 0 and press \'Enter\': ').lower()
    print()

    if strChoice == '0':
        break
            
    if strChoice == '1':
        lstTbl.clear
        with open(strFileName, 'r') as objFile:
            for row in objFile:
                lstRow =  row.strip().split(',')
                dicRow = {'ID': int(lstRow[0]), 'Artist': lstRow[1], 'Album': lstRow[2]}
                lstTbl.append(dicRow)
                print(dicRow)                
        pass

    elif strChoice == '2':
        strID = int(input('Enter ID Number: '))
        strArtist = input('Enter the Artist\'s Name: ')
        strAlbum = input('Enter the Album Title: ')
        intID = int(strID)
        dicRow = {'ID': intID, 'Artist': strArtist, 'Album': strAlbum}
        lstTbl.append(dicRow)
        pass
    
    elif strChoice == '3':
        with open(strFileName, 'w') as objFile:
            for row in lstTbl:
                strRow = ''
                for item in row.values():
                    strRow += str(item) + ','
                strRow = strRow[:-1] + '\n'
                objFile.write(strRow)
    
    elif strChoice == '4':
        lstTbl2 = lstTbl
        print('ID, Artist, Album')
        for row in lstTbl2:
            print(*row.values(), sep = ', ')
    
    elif strChoice == '5':
                
        while True:
            print('\n[l] List all current enteries\n[2] Delete a single entry\n[3] Delete all entries\n[4] Return')
            usrChoice1 = input('Select from 1 to 4 and press Enter: ')
            
            if usrChoice1 == '4':
                break
            
            if usrChoice1 == '1':
                lstTbl2 = lstTbl
                print('ID, Artist, Album')
                for row in lstTbl2:
                    print(*row.values(), sep = ', ')
            
            if usrChoice1 == '2':
                #elitem = None
                delitem = int(input('Enter CD ID to delete: ')) - 1
                print(lstTbl2)
                with open(strFileName, 'r') as objFile:
                    lstTbl.pop(delitem)
                    print('\nDeleted ID - ',delitem)
                    
            if usrChoice1 == '3':
                 while True:
                     usrChoice2 = input('Are you sure you want to delete all of your entries?'
                                        '\n\nType \'Yes\' or \'No\' and press Enter: ').lower()
                     print('\n[Yes] Delete all entries\n[No] Return')
                     
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
