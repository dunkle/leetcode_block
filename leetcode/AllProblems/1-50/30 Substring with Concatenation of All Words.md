![image-20200910155046884](../.assert/image-20200910155046884.png)

给定一个字符串s，一个字典，其中字典中单词的长度都是相同的。将字典中的单词进行组合得到多个字符串，求出这些字符串中在s中出现的所有位置。

假设字典组成的字符串长度为l，则从0开始遍历，长度为0的字串是否是符合要求。

判断是否符合要求可以统计当前子串中单词出现的数量，与字典中单词出现次数进行比较。

~~~python
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        window_size = sum([len(x) for x in words])
        counter = Counter(words)
        result = []
        word_len = len(words[0])
        for i in range(0, len(s)-window_size+1):
            new_counter = dict()
            for j in range(i, i+window_size, word_len):
                current_word = s[j:j+word_len]
                if current_word in counter:
                    new_counter[current_word] = new_counter.get(current_word, 0) + 1
                    if new_counter[current_word] > counter[current_word]:
                        break
            right = True
            for key in counter:
                if key not in new_counter or new_counter[key] != counter[key]:
                    right=False
                    break
            if right:
                result.append(i)
            
        return result
~~~

## 优化算法

假设单词的长度为n，则将s分成三类，每次移动一个单词的长度。以n=3为例，分别从0，从1，从2开始移动，每次移动一个单词的长度。

