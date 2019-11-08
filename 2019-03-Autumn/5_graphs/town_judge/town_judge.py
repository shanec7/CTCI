from collections import defaultdict

def find_judge(N: int, trust: list):
    # Edge case: if there are no trust pairs,
    # N has to be 1 to satisfy the rules (judging him/herself)
    if len(trust) == 0:
        return 1 if N == 1 else -1
    
    trust_vals = defaultdict(int)
    
    # trust someone else == give out 1 trust_val
    # being trusted == receive 1 trust_val
    for from_person, to_person in trust:
        trust_vals[from_person] -= 1
        trust_vals[to_person] += 1
        
    # find the judge
    for person, trust_val in trust_vals.items():
        # judge trusts no one (-0), and is trusted by everyone else (+N-1)
        if trust_val == N - 1:
            return person
        
    # there is no judge
    return -1

if __name__ == '__main__':
    tests = [([2, [[1,2]]], 2),
             ([3, [[1,3],[2,3],[3,1]]], -1)]
    for input, output in tests:
        assert(find_judge(*input) == output)
        print("find_judge(", input[0], ", ", input[1], ")", sep='')
        print("result:", find_judge(*input), "expected:", output)