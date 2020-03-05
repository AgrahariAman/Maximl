from collections import defaultdict, Counter


def SmallestSubString(S):
    # Write your code here
    # abcda
    p = ''.join(set(S))
    # Dictionary which keeps a count of all the unique characters in t.
    dict_t = Counter(p)

    # Number of unique characters in t, which need to be present in the desired window.
    required = len(dict_t)

    # left and right pointer
    l = 0
    r = 0

    # curr_window_uniq_chars_count is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
    # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus curr_window_uniq_chars_count would be = 3 when all these conditions are met.
    curr_window_uniq_chars_count = 0

    # Dictionary which keeps a count of all the unique characters in the current window.
    curr_window_uniq_dict = {}

    # ans tuple of the form (window length, left, right)

    min_window_len = float("inf")
    desired_window_l = None
    desired_window_r = None

    while r < len(S):

        # Add one character from the right to the window
        curr_window_uniq_dict[S[r]] = curr_window_uniq_dict.get(S[r], 0) + 1

        # If the frequency of the current character added equals to the desired count in t then increment the curr_window_uniq_chars_count count by 1.
        if S[r] in dict_t and curr_window_uniq_dict[S[r]] == dict_t[S[r]]:
            curr_window_uniq_chars_count += 1

        # Try and contract the window till the point where it ceases to be 'desirable'.
        while l <= r and curr_window_uniq_chars_count == required:

            # Save the smallest window until now.
            if r - l + 1 < min_window_len:
                min_window_len = r - l + 1
                desired_window_l = l
                desired_window_r = r

            # The character at the position pointed by the `left` pointer is no longer a part of the window.
            curr_window_uniq_dict[S[l]] -= 1
            if S[l] in dict_t and curr_window_uniq_dict[S[l]] < dict_t[S[l]]:
                curr_window_uniq_chars_count -= 1

            # Move the left pointer ahead, this would help to look for a new window.
            l += 1

        # Keep expanding the window once we are done contracting.
        r += 1
    return "" if min_window_len == float("inf") else len(S[desired_window_l: desired_window_r + 1])


S = input()

out_ = SmallestSubString(S)
print(out_)