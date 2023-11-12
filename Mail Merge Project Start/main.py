#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



names = open('Mail Merge Project Start/Input/Names/invited_names.txt').readlines()


letter_content = open("Mail Merge Project Start/Input/Letters/starting_letter.txt",'r').read()

for name in names:
    strippep_name = name.strip()
    new_letter_content = letter_content.replace("[name]",strippep_name)
    
    result = open(f"Mail Merge Project Start/Output/ReadyToSend/letter_for_{strippep_name}.txt",'w')
    result.write(new_letter_content)






