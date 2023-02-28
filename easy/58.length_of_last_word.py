def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    print(len(s.strip().split()[-1]))

lengthOfLastWord("Hello World")
lengthOfLastWord("   fly me   to   the moon  ")
lengthOfLastWord("luffy is still joyboy")