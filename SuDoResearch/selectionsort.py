import random
from typing import List
from pathlib import Path

home = str(Path.home())


def matrix_generator(number_of_participants=None):
    if number_of_participants is None:
        number_of_participants = input("Enter number of participants: ")
    else:
        pass

    print("Generating preference matrix...")

    row_template = list(range(1, number_of_participants + 1))
    matrix = []
    n = 1
    while n <= number_of_participants * 2:
        random.shuffle(row_template)  # modifies row_template in place
        matrix.append(row_template[:])  # make a copy of row_template
        n += 1

    for row in matrix:
        print(*row, sep=" ")

    return matrix


def coupling(n: int, matrix: List[List] = None):
    "Gale-Shapley algorithm for coupling."

    # Parse matrix into male and female preferences.
    if matrix == None:
        # Generate matrix if none is given.
        matrix = matrix_generator(n)
    else:
        pass

    male_pref = matrix[0:n]
    female_pref = matrix[n:]

    # Gale-Shapley algorithm
    single_male = [*range(1, n+1)]
    coupled_female = []
    coupled_pair = [None] * n

    def couple(m_id, f_id):
        single_male.remove(m_id)
        coupled_female.append(f_id)
        coupled_pair[m_id - 1] = f_id
        # indices start from zero, therefore "coupled[m_id-1]" for male position.

    def decouple(m_id, f_id) -> None:
        single_male.append(m_id)
        coupled_female.remove(f_id)
        coupled_pair[coupled_pair.index(f_id)] = None

    while single_male:
        # Iterate through male persons and analyse their preference lists.

        m_id = single_male[0]
        m = male_pref[m_id - 1]

        for f_id in m:
            # Iterate through female persons on current male preference list in order of his preference.
            print("M{} proposes to F{}...".format(m_id,
                                                  f_id))

            if f_id in coupled_female:
                # female is already attached.
                already_coupled_with = coupled_pair.index(f_id) + 1

                pref_old = female_pref[f_id - 1].index(already_coupled_with)
                pref_new = female_pref[f_id - 1].index(m_id)

                if pref_old > pref_new:
                    # female prefers current male more than the original bf.
                    print("F{} accepts the courtship and leaves M{} for M{}.".format(f_id,
                                                                                     already_coupled_with,
                                                                                     m_id))

                    decouple(already_coupled_with, f_id)
                    couple(m_id, f_id)

                    break

                else:
                    print("F{} rejects M{} and stays with her current boyfriend.".format(f_id,
                                                                                         m_id))

                    continue  # Current male protagonist looks to next female on the list.                                                                      m_id))

            else:
                # female is single.
                print("F{} is single and accepts M{}'s courtship.".format(f_id,
                                                                          m_id))
                couple(m_id, f_id)
                break

    print(coupled_pair)

    return coupled_pair


if __name__ == "__main__":

    coupling(5)

    # pref_matrix = [[1, 2, 3],
    #                [1, 2, 3],
    #                [2, 1, 3],
    #                [3, 2, 1],
    #                [3, 1, 2],
    #                [2, 1, 3]]
    # coupling(3, pref_matrix)
