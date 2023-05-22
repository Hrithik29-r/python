



# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

sample_string = 'The quick Brow Fox'
u,l = 0,0
for i in sample_string:
   if (i>='A'and i<='Z'):
         
        u=u+1
   if (i>='a'and i<='z'):
         
        l=l+1  
         
print('No.Upper case characters: ',u)
print('No.Lower case characters: ',l)