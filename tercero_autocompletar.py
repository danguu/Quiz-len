class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node['end'] = True

    def autocomplete(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return []
            node = node[char]
        return self._find_words(node, prefix)

    def _find_words(self, node, prefix):
        words = []
        if 'end' in node:
            words.append(prefix)
        for char, child in node.items():
            if char != 'end':
                words.extend(self._find_words(child, prefix + char))
        return words
