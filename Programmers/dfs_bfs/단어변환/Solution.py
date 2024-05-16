MAX = 55

dest = 0
mn = MAX
ad_words = dict()
check = set()

def dfs(cur, cnt):
    global mn, check

    if cur == dest:
        mn = min(mn, cnt)
        return
    
    for ad in ad_words[cur]:
        if ad not in check:
            check.add(ad)
            dfs(ad, cnt + 1)
            check.remove(ad)

def get_ad_words(words):
    ad_wds = dict({word : [] for word in words})
    
    for word in words:
        for comp_word in words:
            if (word == comp_word or comp_word in ad_wds[word]): continue
            diff_cnt = 0
            for i in range(len(comp_word)):
                if comp_word[i] != word[i]:
                    diff_cnt += 1
                if diff_cnt > 1: break
            if diff_cnt == 1:
                ad_wds[word].append(comp_word)
                ad_wds[comp_word].append(word)
    return ad_wds      

def solution(begin, target, words):
    global dest, ad_words, check
    answer = 0
    ad_words = get_ad_words([*words, begin])
    dest = target

    for ad in ad_words[begin]:
        check.add(ad)
        dfs(ad, 1)

    if mn == MAX:
        answer = 0
    else:
        answer = mn
    return answer

begin = input().rstrip()
target = input().rstrip()
words = list(input().split())
print(solution(begin, target, words))
