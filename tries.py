class TrieNode:
    def __init__(self):
        self.children = {}
        self.top5 = []   # list of words (already sorted)


class AutocompleteSystem:
    def __init__(self):
        self.root = TrieNode()
        self.freq = {}   # word -> frequency

    def insert(self, word):
        # Update global frequency
        self.freq[word] = self.freq.get(word, 0) + 1

        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

            # Remove word if already present
            if word in cur.top5:
                cur.top5.remove(word)

            # Add word
            cur.top5.append(word)

            # Sort by (-frequency, lexicographically)
            cur.top5.sort(key=lambda w: (-self.freq[w], w))

            # Keep only top 5
            if len(cur.top5) > 5:
                cur.top5.pop()

    def search(self, prefix):
        cur = self.root

        # Traverse prefix (O(L))
        for c in prefix:
            if c not in cur.children:
                return []
            cur = cur.children[c]

        # Directly return stored top 5 (O(1))
        return cur.top5
obj = AutocompleteSystem()

obj.insert("apple")
obj.insert("app")
obj.insert("apple")
obj.insert("ape")
obj.insert("april")
obj.insert("app")
obj.insert("application")

print(obj.search("ap"))