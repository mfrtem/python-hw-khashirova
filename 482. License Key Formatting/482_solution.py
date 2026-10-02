class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()

        first = len(s) % k

        if first:
            result = [s[:first]]
            start = first
        else:
            result = []
            start = 0

        for i in range(start, len(s), k):
            result.append(s[i:i + k])

        return "-".join(result)
