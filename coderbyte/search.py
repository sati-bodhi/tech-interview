"""
Using the Python language, have the function PatternChaser(str)
take str which will be a string and return the longest pattern
within the string. A pattern for this challenge will be defined as:
if at least 2 or more adjacent characters within the string repeat
at least twice. So for example "aabecaa" contains the pattern aa,
on the other hand "abbbaac" doesn't contain any pattern. Your program
should return yes/no pattern/null. So if str were "aabejiabkfabed" the
output should be yes abe. If str were "123224" the output should return
no null. The string may either contain all characters (a through z only),
integers, or both. But the parameter will always be a string type.
The maximum length for the string being passed in will be 20 characters.
If a string for example is "aa2bbbaacbbb" the pattern is "bbb" and not "aa".
You must always return the longest pattern possible.
Input:"da2kr32a2"
Output:"yes a2"
Input:"sskfssbbb9bbb"
Output:"yes bbb"
"""

def SearchingChallenge(s):
    hash_set = set()
    matches = {}
    dup = False

    for i in range(len(s) - 1):
        pat = s[i:i + 2]
        if pat in hash_set:
            if dup == True:  # Checks for consecutive match.
                repeated = s[dup_id:i + 2]  # Update to longest pattern
                matches[dup_id] = repeated  # Store result in dict
            else:
                dup_id = i  # Note start position of repeating pattern
                dup = True  # Set value for next loop to know if prev pattern is matching.

                if pat == list(hash_set)[-1]:
                    pass

                else:
                    matches[dup_id] = pat

        else:
            hash_set.add(pat)
            dup = False

    # print(matches)

    # Output conditionals

    if matches:

        if len(matches) > 1:
            longest_possb = matches[
                max(matches, key=lambda k: len(matches[k]))
            ]

            return "yes " + longest_possb

        else:

            return "yes " + next(iter(matches.values()))

    else:

        return "no null"


print(SearchingChallenge("abbbaac"))
