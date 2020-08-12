
# coding: utf-8

# In[1]:


import hashlib


# In[ ]:


print("**********************PASSWORD CRACKER************************")

#To check if the passwd is found or not

pass_found = 0

input_hash = input("Enter the Hashed Password:")

pass_doc = input("\nEnter password filename including path(root / home/):")

try:
    #trying to open the passwd file
    pass_file = open(pass_doc, 'r')
except:
    print("Error:")
    print(pass_doc, "is not found.\nPlease provide the correct path.")
    quit()

#Comparing the hashes with the input_hash to find passwd

for word in pass_file:
    #encoding the word to utf-8
    enc_word = word.encode('utf-8')
    
    hash_word = hashlib.md5(enc_word.strip())
    
    digest = hash_word.hexdigest()
    
    if digest == input_hash:
        print("Password found.\nThe password is: ", word)
        pass_found = 1
        break
if not pass_found:
    print("Password is not found in the",pass_doc, "file")
    print('\n')
print("**********************THANK YOU************************")

