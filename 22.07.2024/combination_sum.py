def combination_sum(candidates, target):
    def backtrack(remain, combo, start):
        if remain == 0:
            result.append(list(combo))
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remain:
                continue
            combo.append(candidates[i])
            backtrack(remain - candidates[i], combo, i)
            combo.pop()
    result = []
    backtrack(target, [], 0)
    return result
print(combination_sum([2,3,6,7], 7))  
