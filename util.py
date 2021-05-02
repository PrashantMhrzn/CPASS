class Generator:

    def __init__(self, word, special):
        self.special = special
        self.word = word
        self.reverse = self.word[::-1]
        self.capital = self.word.capitalize()
        self.upper = self.word.upper()
    
    # Add number behind the word
    def first_phase(self, word):
        output = []
        temp = ''
        for i in range(1,2):
            temp = word + str(i)
            output.append(temp)
            for j in range(1, 9):
                temp = temp + str(j+1)
                output.append(temp)
        for i in range(9,8,-1):
            temp = word + str(i)
            output.append(temp)
            for j in range(9, 0, -1):
                temp = temp + str(j-1)
                output.append(temp)
        return output

    # Add '@' in between word and numebers
    def second_phase(self, word):
        output = self.first_phase(word)
        at = len(word)
        second_output = []
        for item in output:
            pre = item[0:at]
            post = item[at:-1]
            combo = pre + '@' + post
            second_output.append(combo)
        return second_output

    # Add '_' in between word and numebers
    def third_phase(self, word):
        output = self.first_phase(word)
        at = len(word)
        second_output = []
        for item in output:
            pre = item[0:at]
            post = item[at:-1]
            combo = pre + '_' + post
            second_output.append(combo)
        return second_output  

    def birthday(self, date):
        year = int(str(date)[4:])
        output = [str(date), str(date)[::-1]]
        for i in range(year-10, year+10):
            output.append(self.word+str(i))
            output.append(self.word+'@'+str(i))
            output.append(self.word+'_'+str(i))
            output.append(self.word+str(year))
            output.append(self.word+str(str(date)[::-1]))
        return output

    # Add special characters
    def add_special(self):
        output = []
        with open('special_char.txt', "r") as word_list:
            chars = word_list.read().split('\n')
        for char in chars:
            output.append(self.word+char)
        return output


    # compile the wordlist
    def compiler(self, word):
        master = []
        first = self.first_phase(word)
        second = self.second_phase(word)
        third = self.third_phase(word)
        fourth = self.add_special()
        for words in first:
            master.append(words)
        for words in second:
            master.append(words)
        for words in third:
            master.append(words)
        if self.special == True:
            for words in fourth:
                master.append(words)
        return master

    # Put all the words into one list
    def result(self):
        total = [self.word, self.reverse, self.capital, self.upper]
        result = [self.word, self.reverse, self.capital, self.upper]
        for item in total:
            result += self.compiler(item)
        return result