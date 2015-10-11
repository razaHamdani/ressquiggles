DICT_FILENAME = "dict.txt"
CHALLENGE_INPUT_FILENAME = 'input_rs.txt'

def spellChecker(magic_dict, challenger_file):
    with open(challenger_file) as fp:
        for word in fp:
            word = word.strip()
            if word != '':
                list_of_relevant_words = magic_dict[word[0]]
                magic_string = ' '.join(list_of_relevant_words)
                letters = map(lambda x:x, word)
                realtimeword = ''
                misspelled_flag = 0
                for letter in letters:
                    realtimeword += letter
                    if misspelled_flag == 0:
                        if realtimeword not in magic_string:
                            realtimeword += "<"
                            misspelled_flag = 1
                
                print realtimeword
    
    

def makeDict(filename):
    res = {}
    with open(filename) as fp:
        for word in fp:
            word = word.strip()
            if word != '':
                first_letter  = word[0]
                if res.get(first_letter,None) is not None:
                    res[first_letter].append(word)
                else:
                    res[first_letter] = []
                    res[first_letter].append(word)
    return res
    

if __name__ == "__main__":
    customized_dict= makeDict(DICT_FILENAME)
    spellChecker(customized_dict, CHALLENGE_INPUT_FILENAME)
    
