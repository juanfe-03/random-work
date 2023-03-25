def is_space(char):
    if ord(" ")==ord(char):
        space=True
    else:
        space=False
    return space

def multiplier(dimension, matrix_1, matrix_2):
    string=""
    for j in range(0,len(matrix_2),dimension):
        for i in range(0,len(matrix_1),dimension):
            m1_chunk=matrix_1[j:dimension+j]
            m2_chunk=matrix_2[i:i+dimension]
            mult=component_mult(dimension, m1_chunk, m2_chunk)
            mult=str(mult)
            string+=(mult+" ")
    return string
def component_mult(dimension, m1_chunk, m2_chunk):
    comp=0
    for i in range (dimension):
        c=int(m1_chunk[i])*int(m2_chunk[i])
        comp+=c
    return str(comp)
def print_matrix(new,dimension):
    space_counter=0
    counter=0
    old_counter=0
    for i in range(dimension):
        while space_counter<dimension:
            char=new[counter]
            if is_space(char):
                space_counter+=1
            counter+=1
            row=new[old_counter:counter]
        print(row)
        old_counter=counter
        space_counter=0


def row_matrix_input(dimension):
    matrix_1=""
    for i in range(dimension):
        char=input("Enter the rows of row (first) matrix in order.")
        matrix_1+=char
    return matrix_1
def column_matrix_input(dimension):
    matrix_2=""
    for i in range(dimension):
        char=input("Enter the columns of column (second) matrix in order")
        matrix_2+=char
    return matrix_2
def main():
    dimension = int(input("Enter the length of one side of the square"))
    matrix_1=row_matrix_input(dimension)
    matrix_2 = column_matrix_input(dimension)
    new=multiplier(dimension, matrix_1, matrix_2)
    print_matrix(new, dimension)

main()




