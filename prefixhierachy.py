#given a list of names, 
# determin the number of names in that list for which a given query string is a prefix. 
# the prefix must be at least 1 character less than the entire name string.
class PrefixHierachy:
    def find_prefix(self, input_array, prefix_array):
        #build trie with prefix_array
        #for each of word in input_array, check each one in the trie, if has passed a node with a word in prefix array, then return True.