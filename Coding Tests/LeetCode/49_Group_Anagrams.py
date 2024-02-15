class Solution:
    def groupAnagrams(self,strs, result=None):
        if result is None:
            result = []
    
        if not strs:  # Base case: if strs is empty, return the result
            return result
        
        current_word = strs[0]
        anagrams = [current_word]
        sorted_current_word = sorted(current_word)
        
        # Iterate over the rest of the words
        for word in strs[1:]:
            if sorted(word) == sorted_current_word:
                anagrams.append(word)
        
        # Filter out the anagrams from the original list
        remaining_words = [word for word in strs if word not in anagrams] #
        
        # Append the group of anagrams to the result
        result.append(anagrams)
        
        # Recur with the remaining words
        return Solution().groupAnagrams(remaining_words, result)


str = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(str))