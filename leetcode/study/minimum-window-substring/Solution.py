class Solution:
    def init_alpha(self):
        alpha = {}
        for i in range(26):
            alpha[chr(ord('A')+i)] = 0
            alpha[chr(ord('a')+i)] = 0

        return alpha

    # alpha안에 store만큼의 str이 있는지 확인. 빈도수 확인
    def is_included(self, store, alpha):
        for st in store:
            if alpha[st] < store[st]:
                return False

        return True

    def minWindow(self, s: str, t: str) -> str:
        alpha = self.init_alpha()
        answer = []
        store = {}

        # 찾으려는 문자의 빈도 설정
        for st in t:
            if st in store:
                store[st] += 1
            else:
                store[st] = 1
        
        en = 0
        for st in range(len(s)):
            while en < len(s) and not self.is_included(store, alpha):
                alpha[s[en]] += 1
                en += 1

            if en == len(s):
                if not self.is_included(store, alpha):
                    break
            
            if not answer:
                answer = s[st:en]
            elif len(s[st:en]) < len(answer):
                answer = s[st:en]
            
            alpha[s[st]] -= 1

        return ''.join(answer)

s = input()
t = input()
print(Solution().minWindow(s, t))
