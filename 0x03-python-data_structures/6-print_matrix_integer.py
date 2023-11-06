#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    else:
        for sub_mat in matrix:
            if len(sub_mat) == 0:
                print()
            else:
                for i in range(len(sub_mat)):
                    print("{:d}".format(sub_mat[i]),
                            end="\n" if i == len(sub_mat) else " ")
