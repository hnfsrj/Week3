word = input('Please enter a word to check: ')

print("Palindrome" if ''.join([word[i].lower() for i in range(len(word)-1,-1,-1)]) == word.lower() else word+" is not a Palindrome")

''' Longer and easier to read version
opposite = []

for i in range(len(word)-1,-1,-1):
    opposite.append(word[i].lower())

if ''.join(opposite) == word.lower():
    print('Palindrome')
else:
    print('The word '+word+' is not a palindrome because '+''.join(opposite)+' is not a palindrome.')

'''