import sys
import numpy as np
import time

#define score values
match_score = None
mismatch_score = None
gap_score = None

def local_align(s1,s2):
    """
    :param s1: the first sequence
    :param s2: the second sequence
    :return: the local alignment dynamic programming scoring matrix, the location of the maximum score
    """
    start = time.time()
    columns = len(s1) + 1
    rows = len(s2) + 1
    dp_matrix = [[0 for j in range(columns)] for i in range(rows)]

    best_score = -1
    best_loc = (0,0)
    for i in range(1, rows):
        for j in range(1, columns):
            if s1[j-1] == s2[i-1]:
                score = max([0,dp_matrix[i-1][j]+gap_score,dp_matrix[i][j-1]+gap_score,dp_matrix[i-1][j-1]+match_score])
            else:
                score = max([0,dp_matrix[i-1][j] + gap_score, dp_matrix[i][j-1] + gap_score, dp_matrix[i-1][j-1] + mismatch_score])
            dp_matrix[i][j] = score
            if score > best_score:
                best_score = score
                best_loc = (i,j)
    print("local alignment execution time:  " + str((time.time()-start)))
    return dp_matrix,best_loc

def get_move_local(matrix,idx):
    """
    :param matrix: the matrix of alignment scores
    :param idx: location in matrix
    :return: if the next move is diagonal, up, or left in the matrix
    """
    i,j = idx
    up = matrix[i-1][j] + gap_score
    left = matrix[i][j-1] + gap_score
    if i > 0 and j > 0:
        diagonal = matrix[i - 1][j - 1]
        if seq1[j - 1] == seq2[i - 1]:
            diagonal += match_score
        else:
            diagonal += mismatch_score
    else:
        diagonal = -np.inf

    if diagonal == matrix[i][j]:
        if matrix[i-1][j-1] == 0:
            return "end"
        else:
            return "diagonal"
    elif left == matrix[i][j]:
        if matrix[i][j-1] == 0:
            return "end"
        else:
            return "left"
    elif up == matrix[i][j]:
        if matrix[i-1][j] == 0:
            return "end"
        else:
            return "up"
    else:
        return "error"

def align_seqs_local(matrix,idx,s1, s2):
    """
    :param matrix: alignment scores matrix
    :param idx: index of highest score
    :param seq1: first sequence
    :param seq2: second sequence
    :return: the local alignment of seq1,seq2
    """
    s1_align = []
    s2_align = []
    move = get_move_local(matrix,idx)
    i,j = idx
    while move != "end":
        if move == "diagonal":
            s1_align.append(seq1[j-1])
            s2_align.append(seq2[i-1])
            i += -1
            j += -1
        elif move == "left":
            s2_align.append('-')
            s1_align.append(seq1[j-1])
            j += -1
        else:
            s2_align.append(seq2[i-1])
            s1_align.append('-')
            i += -1
        move = get_move_local(matrix,(i,j))

    s1_align.append(seq1[j-1])
    s2_align.append(seq2[i-1])

    return ''.join(reversed(s1_align)), ''.join(reversed(s2_align))

def fitting_align(s1,s2):
    """
    :param s1: the first sequence
    :param s2: the second sequence
    :return: the fitting alignment dynamic programming scoring matrix, the location of the maximum score
    """
    start = time.time()
    columns = len(s1) + 1
    rows = len(s2) + 1
    dp_matrix = [[0 for j in range(columns)] for i in range(rows)]
    for i in range(rows):
        for j in range(columns):
            if i == 0:
                dp_matrix[i][j] = gap_score*j

    best_score = -np.inf
    best_loc = (0,0)
    for i in range(1,rows):
        for j in range(1,columns):
            if s1[j-1] == s2[i-1]:
                score = max([dp_matrix[i-1][j]+gap_score,dp_matrix[i][j-1]+gap_score,dp_matrix[i-1][j-1]+match_score])
            else:
                score = max([dp_matrix[i-1][j] + gap_score, dp_matrix[i][j-1] + gap_score, dp_matrix[i-1][j-1] + mismatch_score])
            dp_matrix[i][j] = score
            if j == columns-1:
                if score > best_score:
                    best_score = score
                    best_loc = (i,j)
    print("fitting alignment execution time:  " + str((time.time()-start)))
    return dp_matrix,best_loc

def get_move_fitting(matrix,idx):
    """
    :param matrix: the matrix of alignment scores
    :param idx: location in matrix
    :return: if the next move is diagonal, up, or left in the matrix
    """
    i,j = idx
    if j == 0:
        return "end"

    up = matrix[i-1][j] + gap_score
    left = matrix[i][j-1] + gap_score
    if i>0 and j>0:
        diagonal = matrix[i-1][j-1]
        if seq1[j-1] == seq2[i-1]:
            diagonal += match_score
        else:
            diagonal += mismatch_score
    else:
        diagonal = -np.inf

    if diagonal == matrix[i][j]:
        return "diagonal"
    elif left == matrix[i][j]:
        return "left"
    elif up == matrix[i][j]:
        return "up"
    else:
        return "error"

def align_seqs_fitting(matrix,idx,s1, s2):
    """
    :param matrix: alignment scores matrix
    :param idx: index of highest score
    :param seq1: first sequence
    :param seq2: second sequence
    :return: the fitting alignment of seq1,seq2
    """
    s1_align = []
    s2_align = []
    move = get_move_fitting(matrix, idx)
    i,j = idx
    while move != "end":
        if move == "diagonal":
            s1_align.append(seq1[j-1])
            s2_align.append(seq2[i-1])
            i += -1
            j += -1
        elif move == "left":
            s2_align.append('-')
            s1_align.append(seq1[j-1])
            j += -1
        else:
            s2_align.append(seq2[i-1])
            s1_align.append('-')
            i += -1
        move = get_move_fitting(matrix,(i,j))

    return ''.join(reversed(s1_align)), ''.join(reversed(s2_align))



if __name__ == "__main__":
    input = sys.argv[1]
    output = sys.argv[2]
    alignment_type = sys.argv[3]
    if (alignment_type != "local") and (alignment_type != "fitting"):
        print("invalid alignment type. specify either 'fitting' or 'local' alignment")
        sys.exit(0)
    else:
        with open(input,'r') as f:
            match_score = int(f.readline().strip())
            mismatch_score = int(f.readline().strip())
            gap_score = int(f.readline().strip())
            seq1 = f.readline().strip()
            seq2 = f.readline().strip()
        if alignment_type == 'local':
            matrix, best_loc = local_align(seq1,seq2)
            seq1_aligned, seq2_aligned = align_seqs_local(matrix, best_loc, seq1, seq2)
            with open(output,'w+') as o:
                o.write(seq1_aligned+'\n')
                o.write(seq2_aligned+'\n')
                o.write("score: " + str(matrix[best_loc[0]][best_loc[1]]))
        if alignment_type == 'fitting':
            matrix, best_loc = fitting_align(seq1, seq2)
            seq1_aligned, seq2_aligned = align_seqs_fitting(matrix, best_loc, seq1, seq2)
            with open(output, 'w+') as o:
                o.write(seq1_aligned + '\n')
                o.write(seq2_aligned + '\n')
                o.write("score: " + str(matrix[best_loc[0]][best_loc[1]]))