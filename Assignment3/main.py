def initialise_table():
    #forms a table with two coloumns, the first being the status either "never used", "tombstone" or "occupied", 
    #where the second stores the key of the word for all 26 letters
    #all 26 rows are initialised under "never used"
    return [{"status": "never used", "key": None} for _ in range(26)]

def hash_function(word):

    return ord(word[-1]) - ord('a')


def search(table, word):

    hash_key = hash_function(word)
    start  = hash_key
    
    while True:
        slot = table[hash_key]

        if slot["status"] == "never used":
              return -1
    
        elif slot["status"] == "occupied" and slot["key"] == word:
            return hash_key
        
        hash_key = (hash_key + 1) % 26

        if hash_key == start:
            return -1

def insert(table, word):

    if search(table,word) != -1:
        return
    
    hash_key = hash_function(word)

    while True:

        slot = table[hash_key]

        if slot["status"] == "never used" or slot["status"] == "tombstone":
            slot["key"] = word
            slot["status"] = "occupied"
            return
        
        hash_key = (hash_key + 1) % 26

def deletion(table, word):

    index = search(table,word)
    if index == -1:
        return
    
    slot = table[index]
    slot["status"] = "tombstone"

    #main function to process the inputs
def main():
    #firstly need to split up the command line and disect each of the tree modifications and order than it will be printed in
    commandLine = input().lstrip()
    parts = commandLine.split()
    #as the order is last in line, => -1
    table = initialise_table()
    
    for move in parts:
        #first character either A or D
        modification = move[0]
        #then follows the word
        word = move[1:]

        if modification == 'A':
            #if A then inserts
            insert(table, word)
        elif modification == 'D':
            #if D then deletes
            deletion(table, word)

    output = []
    for slot in table:
        if slot["status"] == "occupied":
            output.append(slot["key"])
    

    print(" ".join(output))
    
#call main
if __name__ == "__main__":
    main()










        


    
