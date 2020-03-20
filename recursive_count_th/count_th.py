'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # base case, if the word has fewer than 2 letters in it, there's no 'th's left
    if len(word) < 2:
        return 0
    
    # check last two letters to see if they are 'th'
    th_count = 0
    if word[-2:] == 'th':
        th_count += 1
    
    # repeat this process on the word minus the last letter
    return th_count + count_th(word[:-1])
