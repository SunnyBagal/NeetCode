from collections import Counter

class Solution:
  def minWindow(self, s: str, t: str) -> str:
    if not s or not t or len(s) < len(t):
        return ""

    need = Counter(t)
    required = len(need)      # distinct chars we must satisfy
    have = 0                  # distinct chars currently satisfied
    window = {}

    res, res_len = (-1, -1), float("inf")
    left = 0

    for right, c in enumerate(s):
        window[c] = window.get(c, 0) + 1
        if c in need and window[c] == need[c]:
            have += 1

        while have == required:
            # update result if this window is smaller
            if (right - left + 1) < res_len:
                res = (left, right)
                res_len = right - left + 1

            # shrink from the left
            lc = s[left]
            window[lc] -= 1
            if lc in need and window[lc] < need[lc]:
                have -= 1
            left += 1

    l, r = res
    return s[l:r + 1] if res_len != float("inf") else ""