# 21. Check whether a character is a vowel or consonant.
#A, E, I, O, and U
Character =input("Enter the Character  = ")

#Approach  1

if Character == 'a' or Character == 'A' :
    print(f"Entered Character= {Character} is Vowel ")
elif Character == 'e' or Character == 'E' :
    print(f"Entered Character= {Character} is Vowel ")  
elif Character == 'i' or Character == 'I' :
    print(f"Entered Character= {Character} is Vowel ")
elif Character == 'o' or Character == 'O' :
    print(f"Entered Character= {Character} is Vowel ")
elif Character == 'u' or Character == 'U' :
    print(f"Entered Character= {Character} is Vowel ")    

else:
    print(f"Entered Character= {Character} is consonant ")

#Approach  2
count=0
for Character1 in 'aeiouAEIOU' :
        if Character1 == Character :
            print(f"Entered Character= {Character} is Vowel ")
        elif  Character1 != Character :
            count=count+1
            continue
        
if (count == len('aeiouAEIOU')):
    print(f"Entered Character= {Character} is consonant  ")
    
    
#Approach  3

if Character.isalpha() :
    print(f"Enter Charecter is alphabatic")
else:
    print(f"Enter Charecter is other than alphabatic and charecter is  {Character}")