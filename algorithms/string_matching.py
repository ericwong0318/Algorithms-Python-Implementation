import functools


def simple_match(s, t) -> int:
    """
    Match substring s in the text t.

    Time complexity is O(len(s) * len(t)).

    :param s: substring
    :param t: text
    :return: first index of matched string in text, -1 if not found
    """
    for i in range(len(t) - len(s) + 1):
        if s == t[i: i + len(s)]:
            return i
    return -1


def rabin_karp(s: str, t: str) -> int:
    """
    Match substring s in the text t.

    Time complexity is O(len(s) + len(t)).

    :param s: substring
    :param t: text
    :return: index of matched string in text, -1 if not found
    """
    if len(s) > len(t):
        return -1

    base = 128

    """preprocess"""
    h_s = 0
    h_t = 0
    for c in s:
        h_s = h_s * base + ord(c)
    for c in t[:len(s)]:
        h_t = h_t * base + ord(c)
    if h_s == h_t and t[:len(s)] == s:
        return 0

    """rolling hash"""
    for i in range(len(s), len(t)):
        h_t = h_t - ord(t[i - len(s)]) * (base ** (len(s) - 1))
        h_t = h_t * base + ord(t[i])
        if h_s == h_t and t[i + 1 - len(s):i + 1] == s:
            return i + 1 - len(s)

    return -1


def rabin_karp_2(s, t) -> int:
    """
    Match substring s in the text t.

    Time complexity is O(len(s) + len(t)).

    :param s: substring
    :param t: text
    :return: index of matched string in text, -1 if not found
    """
    if len(s) > len(t):
        return -1

    base = 128

    t_hash = functools.reduce(lambda h, c: h * base + ord(c), t[:len(s)], 0)
    s_hash = functools.reduce(lambda h, c: h * base + ord(c), s, 0)
    power_s = base ** max(len(s) - 1, 0)

    for i in range(len(s), len(t)):
        if t_hash == s_hash and t[i - len(s):i] == s:
            return i - len(s)

        # rolling hash
        t_hash -= ord(t[i - len(s)]) * power_s
        t_hash = t_hash * base + ord(t[i])

    # match
    if t_hash == s_hash and t[-len(s):] == s:
        return len(t) - len(s)

    return -1
