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
