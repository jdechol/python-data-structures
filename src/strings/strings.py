def is_unique(string):
    length = len(string)
    if length < 2:
        return True
    if length > 128:
        return False
    lookup = [False]*128

    for char in string:
        if lookup[ord(char)]:
            return False
        lookup[ord(char)] = True

    return True


# O(n*log(n))
def is_permutation(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True

    l1 = list(s1)
    l2 = list(s2)
    if len(l1) != len(l2):
        return False
    l1.sort()
    l2.sort()

    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True


# O(n)
def is_permutation2(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True
    l1 = list(s1)
    l2 = list(s2)
    if len(l1) != len(l2):
        return False
    lookup1 = [0]*128
    lookup2 = [0]*128

    for i in range(len(l1)):
        lookup1[ord(l1[i])] += 1
        lookup2[ord(l2[i])] += 1

    for i in range(len(lookup1)):
        if lookup1[i] != lookup2[i]:
            return False
    return True


# O(nlog(n)) Least performant but interesting to look at code
def is_permutation3(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True

    l1 = list(s1)
    l2 = list(s2)
    if len(l1) != len(l2):
        return False
    l1.sort()
    l2.sort()

    return len([different for i in range(len(l1)) if (different := different_at(i, l1, l2))]) == 0


def different_at(index, l1, l2):
    return l1[index] != l2[index]
