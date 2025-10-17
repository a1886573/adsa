#Aidan Matkovic a1886573    Assignment 3 Hash Tables    Last edited 17/10/25 3:12PM

def initialise_table():
    #forms a table with two coloumns, the first being the status either "never used", "tombstone" or "occupied", 
    #where the second stores the key of the word for all 26 letters
    #all 26 rows are initialised under "never used"
    return [{"status": "never used", "key": None} for _ in range(26)]

def hash_function(word):
    #the built in ord function converts a character into ACSII, where this line returns the index of the last letter of the word, i.e if b => 2
    return ord(word[-1]) - ord('a')

#search function, process referenced from the task sheet
def search(table, word):
    #returns the index of the last letter of the word
    hash_key = hash_function(word)
    #increments starts from this index and it will be used as a condition to terminate the loop. 
    start  = hash_key
    
    while True:
        #retrieve the corresponding table slot 
        slot = table[hash_key]
        
        #if the slot is under never used, exit loop as it is empty and the word does not exist in the table
        if slot["status"] == "never used":
              return -1
        #if occupied, return the key to the word 
        elif slot["status"] == "occupied" and slot["key"] == word:
            return hash_key
        
        #Then otherwise move to the next slot, process as linear probing 
        hash_key = (hash_key + 1) % 26
        
        #once completed a full loop, terminate
        if hash_key == start:
            return -1

#methodology followed as the one provided in the task sheet
def insert(table, word):
    
    #if word was found in the table via search function then return immediately as insertion is not necessary.
    if search(table,word) != -1:
        return
    
    #obtain the index 
    hash_key = hash_function(word)

    while True:
        #set corresponding slot
        slot = table[hash_key]
        
        #if the status is never used or tombstone then set key is set to that word, and the status is changed to occupied as the word is inserted
        if slot["status"] == "never used" or slot["status"] == "tombstone":
            slot["key"] = word
            slot["status"] = "occupied"
            return
        # move to next slot
        hash_key = (hash_key + 1) % 26

#deletion process also followed as the one described in the task sheet
def deletion(table, word):
    
    #if word does not already exist in the table return immediately as there is no word to delete
    if search(table,word) == -1:
        return
    
    #find the table index of that word
    index = search(table,word)
    #then set the status of that slot to tombstone.
    slot = table[index]
    slot["status"] = "tombstone"

#main function to process the inputs
def main():
    #firstly need to split up the command line
    commandLine = input().lstrip()
    parts = commandLine.split()
    
    #initialise table
    table = initialise_table()

    for move in parts:
        #first character either A or D
        modification = move[0]
        #then follows the word
        word = move[1:]

        if modification == 'A':
            #if A then insert is called
            insert(table, word)
        elif modification == 'D':
            #if D then deletion is called
            deletion(table, word)
    #initialise output list
    output = []
    #append the keys of all occupied slots to the output as these hold the final list post modification
    for slot in table:
        if slot["status"] == "occupied":
            output.append(slot["key"])
    
    #join the list and print
    print(" ".join(output))
    
#call main
if __name__ == "__main__":
    main()










        


    
