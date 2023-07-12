class Random():

    def psuedo_random(seed, N=1, a=0, b=10, integer = True):
        '''For a some unique value seed, it produces N psuedo-random numbers from a to b'''
        rands =[]
        if integer:
            for i in range(N):
                num = int(a+(b-a)*(abs(hash(str(hash(str(seed)+str(i+1)))))%10**13)/10**13)
                rands.append(num)
        else:
            for i in range(N):
                num = a+(b-a)*(abs(hash(str(hash(str(seed)+str(i+1)))))%10**13)/10**13
                rands.append(num)
        if len(rands) == 1:
            return rands[0]
        
        else:
            return rands
        
class Addition():

    def sigma(list):
        '''This function takes in a list/array and returns the total'''
        total = 0
        for i in list:
            total += i
        return total
    
class Matrices():

    def transposeMatrix(m):
        '''This function takes in array m and transposes it'''
        return list(map(list,zip(*m)))

    def getMatrixMinor(m,i,j):
        '''This function takes in array m, row j, and col c and returns the matrix of minors'''
        return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

    def getMatrixDeternminant(m):
        '''This function takes array m and returns the determinant of that array'''
        #base case for 2x2 matrix
        if len(m) == 2:
            return m[0][0]*m[1][1]-m[0][1]*m[1][0]
        determinant = 0
        for c in range(len(m)):
            determinant += ((-1)**c)*m[0][c]*Matrices.getMatrixDeternminant(Matrices.getMatrixMinor(m,0,c))
        return determinant


    def getMatrixInverse(m):
        '''This function takes in array m and returns the inverse of that array'''
        try:
            determinant = Matrices.getMatrixDeternminant(m)
            #special case for 2x2 matrix:
            if len(m) == 2:
                return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                        [-1*m[1][0]/determinant, m[0][0]/determinant]]

            #find matrix of cofactors
            cofactors = []
            for r in range(len(m)):
                cofactorRow = []
                for c in range(len(m)):
                    minor = Matrices.getMatrixMinor(m,r,c)
                    cofactorRow.append(((-1)**(r+c)) * Matrices.getMatrixDeternminant(minor))
                cofactors.append(cofactorRow)
            cofactors = Matrices.transposeMatrix(cofactors)
            for r in range(len(cofactors)):
                for c in range(len(cofactors)):
                    cofactors[r][c] = cofactors[r][c]/determinant
            return cofactors
    
        except ZeroDivisionError:
            print("The determinant of the array is 0, thus there is no inverse")
