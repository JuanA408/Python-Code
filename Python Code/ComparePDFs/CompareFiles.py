
import hashlib 
from difflib import SequenceMatcher 

    
def hashedInstance(fileName):
    hash = hashlib.sha1()
    with open(fileName, "rb") as file: 
            chunk = 0
            while chunk != b'': 
                chunk = file.read(1024) 
                hash.update(chunk) 
    return hash
            

def hashedFile(fileName1, fileName2): 
  
    hash1 = hashedInstance(fileName1) 
    hash2 = hashedInstance(fileName2) 
    
    return hash1.hexdigest(), hash2.hexdigest() 
    
def results(msgX, msgY): 
    if(msgX != msgY): 
        print("The two file are not identical") 
    else: 
        print("The two files are identical") 

msg1, msg2 = hashedFile("IMG_2810.pdf", "Resume_JA-2.pdf") 
msg3, msg2 = hashedFile("R2.pdf", "Resume_JA-2.pdf") 


results(msg1, msg2)
results(msg3, msg2)
  
