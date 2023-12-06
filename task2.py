pattern = (input('Please enter the pattern to be printed: '))


if pattern not in ['a','e','i','o','u']:
    if len(pattern) == 1:
        for i in range(1,6):
            print(pattern*(2*i-1))
    else:
        print('The length of the character should be 1.')

else:
    print('Vowels are not allowed in the input.')
