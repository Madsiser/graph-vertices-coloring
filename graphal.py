import random as rnd
import os.path as path
import numpy as np


def export_matrix(matrix):
    if matrix is None:
        return None
    number = 1
    name = 'graph[' + str(matrix.shape[0]) + '-' + str(matrix.shape[1]) + ']_' + str(number) + '.npy'
    while path.exists(name):
        number += 1
        name = 'graph[' + str(matrix.shape[0]) + '-' + str(matrix.shape[1]) + ']_' + str(number) + '.npy'
    print(name)
    np.save(name, matrix)
    return


def import_matrix(filename=None, size=None, number=1):
    if (size is None or not len(size) == 2) and filename is None:
        return None
    if filename is None:
        filename: str = 'graph[' + str(size[0]) + '-' + str(size[0]) + ']_' + str(number) + '.npy'
    if path.exists(filename):
        return np.load(filename)
    else:
        print("Bad import file name")
    return None


def make(nodeAmount=3, edgeAmount=3):
    incidentMatrix = np.array([0])
    incidentMatrix.resize((nodeAmount, edgeAmount))
    test = 0
    isGood = False
    while not isGood:
        isGood = True
        P = []
        # Error check
        test += 1
        if test > edgeAmount * 2 + 100:
            print("Cannot link nodes. Probably too many edges")
            return None
        # Making graph by definition
        for edge in range(0, edgeAmount):
            localTest = 0
            node1 = None
            node2 = None
            localGood = False
            while not localGood:
                localGood = True
                if edge + 1 < nodeAmount:
                    node1 = edge
                    node2 = rnd.randint(0, edge + 1)
                    while node2 == node1:
                        node2 = rnd.randint(0, edge + 1)
                else:
                    node1 = rnd.randint(0, nodeAmount - 1)
                    node2 = rnd.randint(0, nodeAmount - 1)
                    while node2 == node1:
                        node2 = rnd.randint(0, nodeAmount - 1)
                for p in P:
                    if (p[0] == node1 and p[2] == node2) or (p[0] == node2 and p[2] == node1):
                        localGood = False
                        localTest += 1
                        if localTest > nodeAmount * 2 + 100:
                            print("Cannot link nodes. Probably too many edges")
                            return None
                        break
            P.append([node1, edge, node2])
        # Making matrix
        for p in P:
            incidentMatrix[p[0], p[1]] = 1
            incidentMatrix[p[2], p[1]] = 1
        for line in incidentMatrix:
            localGood = False
            for i in line:
                if i == 1:
                    localGood = True
            if not localGood:
                isGood = False
                break
    return incidentMatrix


def optimal(matrix):
    if matrix is None:
        return None
    input_x = matrix.shape[0]

    def check():
        ii = 0
        for m in matrix:
            jj = 0
            for n in m:
                if n == 1:
                    for a in range(0, input_x):
                        if matrix[a, jj] == 1 and not ii == a:
                            if colours[ii] == colours[a]:
                                return False
                jj += 1
            ii += 1
        return True

    colours = []
    for i in range(0, input_x):
        colours.append(0)
    system = 0
    done = False
    while not check():
        if done:
            done = False
        else:
            system += 1
        for it in range(0, input_x):
            if colours[it] < system:
                colours[it] += 1
                done = True
                break
            else:
                colours[it] = 0
    return colours


def coloring(matrix):
    if matrix is None:
        return None
    input_x = matrix.shape[0]

    def check():
        ii = 0
        for m in matrix:
            if colours[ii] == -1:
                ii += 1
                continue
            jj = 0
            for n in m:

                if n == 1:
                    for a in range(0, input_x):
                        if matrix[a, jj] == 1 and not ii == a:
                            if colours[ii] == colours[a]:
                                return False
                jj += 1
            ii += 1
        return True

    deg = []
    for m in matrix:
        deg.append(sum(m))
    colours = []
    for i in range(0, input_x):
        colours.append(-1)
    for j in range(max(deg), 0, -1):
        color = 0
        for i in range(0, input_x):
            if deg[i] == j:
                colours[i] = color
                while not check():
                    color += 1
                    colours[i] = color
    if check():
        return colours
    return None
