class Node:
    def __init__(self):
        self.weights = []
        self.next = {}
    
    
class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.cache = {}
        self.prefixTrie = Node()
        self.prefixTrie.weights = range(len(words))
        self.suffixTrie = Node()
        self.suffixTrie.weights = range(len(words))
        for i in range(len(words)):
            word = words[i]
            node = self.prefixTrie
            for j in range(len(word)):
                c = word[j]
                if c not in node.next:
                    newNode = Node()
                    newNode.weights.append(i)
                    node.next[c] = newNode
                else:
                    node.next[c].weights.append(i)
                node = node.next[c]
            node = self.suffixTrie
            for j in reversed(range(len(word))):
                c = word[j]
                if c not in node.next:
                    newNode = Node()
                    newNode.weights.append(i)
                    node.next[c] = newNode
                else:
                    node.next[c].weights.append(i)
                node = node.next[c]
                
    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        if (prefix + "#" + suffix) in self.cache:
            return self.cache[prefix + "#" + suffix]
        
        node = self.prefixTrie
        for c in prefix:
            if c not in node.next:
                return -1
            node = node.next[c]
        prefixWeights = node.weights
        
        node = self.suffixTrie
        for c in reversed(suffix):
            if c not in node.next:
                return -1
            node = node.next[c]
        suffixWeights = node.weights        
        
        candidates = set(prefixWeights).intersection(set(suffixWeights))
        
        result = -1
        if candidates:
            result = max(candidates)
            
        self.cache[prefix + "#" + suffix] = result
        return result

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
