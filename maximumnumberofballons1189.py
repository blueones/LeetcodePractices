class Solution:
    def maxNumberOfBalloons(self, text):
        characterdict={"b":0,"a":0,"l":0,"o":0,"n":0}
        for letter in text:
            if letter in characterdict:
                characterdict[letter]+=1
        #print(characterdict)
        characterdict['l']=characterdict['l']/2
        characterdict['0']=characterdict['0']/2
        return min(characterdict.values())

        