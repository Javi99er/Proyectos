def get_permutations(sequence):
    if len(sequence) <= 1:
        return [sequence]

    lista = []
    for letra in sequence:
        x = get_permutations(sequence.replace(letra, '', 1))
        for i in x:
            y = letra + i
            if lista.count(y) == 0:
                lista.append(letra + i)
    return lista

'''
# Borrar
input1 = 'abcd'
print('Input:', input1)
print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
print('Actual Output:', get_permutations(input1))

# Test repeat character case
input2 = 'aabd'
print('Input:', input2)
print('Expected Output:', ['aab', 'aba', 'baa'])
print('Actual Output:', get_permutations(input2))

input3 = 'aad'
print('Input:', input3)
print('Expected Output:', ['aa'])
print('Actual Output:', get_permutations(input3))

# Test the single character edge case
input4 = ''
print('Input:', input4)
print('Expected Output:', [''])
print('Actual Output:', get_permutations(input4))
'''