def findPairs(ListNumbers, target):
    seen = {}
    pairs = []

    for num in ListNumbers:
        #if ListNumbers don't have any integer or have any string it'll show an error
        for number in ListNumbers:
            if not isinstance(number, int):
                raise TypeError("The numbers in the list must be integers")
        
        #if ListNumbers isn't a list it'll show an error
        if not isinstance(ListNumbers, list):
            raise TypeError("List numbers must be a list")
        
        '''
        The subtraction is performed between the number being compared from the list and the target 
        value to see how much is needed for that number to reach the target value. If that complement is already 
        added to the 'seen' dictionary, it means that the two numbers sum up to the target value
        '''
        complement = target - num
        if complement in seen and seen[complement] > 0:
            pair = (num, complement)
            pairs.append(pair)
            seen[complement] -= 1
            print("Found a pair:", pair)

        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1
        
        print("Seen numbers:", seen)
    if pairs:
        print("Pairs that sum to the target:", target)
        for pair in pairs:
            print(pair[0], "+", pair[1])
    else:
        print("No pairs found that sum to the target:",target)
    
    return pairs

# You can test with these to verify that the code only accepts integer data types and lists
# ListNumbers = ['hi',2,'works',4]
# target = 'hi'

ListNumbers = [4,6,9,1,3,5,7,8,-5]
target = input('Please enter the target number :')

#if target isn't an integer it'll show an error
if not target.isdigit():
    raise TypeError("Target must be an integer")

target = int(target)
findPairs(ListNumbers, target)


