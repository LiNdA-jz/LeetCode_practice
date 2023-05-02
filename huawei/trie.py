# class Trie:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.data = []


#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """
#         self.data.append(word)


#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the trie.
#         """
#         return word in self.data


#     def startsWith(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """
#         reg_str = "^" + prefix
#         for i in self.data:
#             # print(re.findall(reg_str, i))
#             if re.findall(reg_str, i) != []:
#                 return True
#         return False

# much faster
# Trie，又称前缀树或字典树，是一棵有根树，其每个节点包含以下字段：

# 指向子节点的指针数组 children 对于本题而言，数组长度为 26
# children[0] 对应小写字母 a，children[1] 对应小写字母 b，children[25] 对应小写字母 z。
# 布尔字段 isEnd，表示该节点是否为字符串的结尾。

# 插入字符串

# 我们从字典树的根开始，插入字符串。对于当前字符对应的子节点，有两种情况：

# 子节点存在。沿着指针移动到子节点，继续处理下一个字符。
# 子节点不存在。创建一个新的子节点!!!，记录在 children 数组的对应位置上，然后沿着指针移动到子节点，继续搜索下一个字符。
# 重复以上步骤，直到处理字符串的最后一个字符，然后将当前节点标记为字符串的结尾。

# 查找前缀

# 我们从字典树的根开始，查找前缀。对于当前字符对应的子节点，有两种情况：

# 子节点存在。沿着指针移动到子节点，继续搜索下一个字符。
# 子节点不存在。说明字典树中不包含该前缀，返回空指针。
# 重复以上步骤，直到返回空指针或搜索完前缀的最后一个字符。

# 若搜索到了前缀的末尾，就说明字典树中存在该前缀。此外，若前缀末尾对应节点的 isEnd 为真，则说明字典树中存在该字符串。

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/QC3q1f/solution/shi-xian-qian-zhui-shu-by-leetcode-solut-un50/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/QC3q1f/solution/shi-xian-qian-zhui-shu-by-leetcode-solut-un50/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)