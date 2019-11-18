def smallestPalindrome(s):
        if s == s[::-1]: return s

            len_s = len(s)

                stopval = len_s//2
                    if len_s % 2 == 0: stopval -= 1

                        for i in range(len_s - 1, stopval, -1):
                                    new_s = s[:i] + s[:len_s - i][::-1]
                                            if new_s == new_s[::-1] and new_s >= s: return new_s

                                                if len_s % 2: # odd length string
                                                            if s[len_s//2] == 'z':
                                                                            itr = len_s//2 - 1
                                                                                        while s[itr] == 'z': itr -= 1
                                                                                        # won't have a word of only z's at this point
                                                                                                    halfstr = s[:itr] + chr(ord(s[itr])+1) + 'a' * (len_s//2 - itr - 1)
                                                                                                                return halfstr + 'a' + halfstr[::-1]
                                                                                                                    return s[:len_s//2] + chr(ord(s[len_s//2]) + 1) + s[:len_s//2][::-1]

                                                                                                                    else: # even length string
                                                                                                                                if s[len_s//2 - 1] > s[len_s//2]:
                                                                                                                                                return s[:len_s//2] + s[:len_s//2][::-1]
                                                                                                                                                    if s[len_s//2 - 1] == 'z':
                                                                                                                                                                    itr = len_s//2 - 2
                                                                                                                                                                                while s[itr] == 'z': itr -= 1
                                                                                                                                                                                            halfstr = s[:itr] + chr(ord(s[itr])+1) + 'a' * (len_s//2 - itr - 1)
                                                                                                                                                                                                        return halfstr + halfstr[::-1] # answer = s up to itr, then itr increased by one val, then a's to fill up, then make palindrome
                                                                                                                                                                                                            return s[:len_s//2 - 1] + chr(ord(s[len_s//2 - 1]) + 1)*2 + s[:len_s//2 - 1][::-1]
