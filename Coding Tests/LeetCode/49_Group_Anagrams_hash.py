class Solution:
    def groupAnagrams(self, strs):
        anagram_dict = {}
        
        for word in strs:
            sorted_word = ''.join(sorted(word)) # convert to sorted string
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word) # if the sorted word is already in the dictionary, append the word to the list
            else:
                anagram_dict[sorted_word] = [word] # if the sorted word is not in the dictionary, create a new list and append the word to it
        return list(anagram_dict.values())


str = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(str))