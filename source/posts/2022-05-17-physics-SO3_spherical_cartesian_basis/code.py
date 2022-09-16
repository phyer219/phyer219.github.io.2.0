from sympy import pprint
from sympy import Matrix
from sympy import I
from sympy import sqrt

jx_cartesian = Matrix([[0, 0, 0],
                       [0, 0, I],
                       [0, -I, 0]])
jy_cartesian = Matrix([[0, 0, I],
                       [0, 0, 0],
                       [-I, 0, 0]])
jz_cartesian = Matrix([[0, I, 0],
                       [-I, 0, 0],
                       [0, 0, 0]])

print('==== SO(3) generators in cartesian representation is ===')
print('jx_cartesian:')
pprint(jx_cartesian)
print('jy_cartesian:')
pprint(jy_cartesian)
print('jz_cartesian:')
pprint(jz_cartesian)
print('========================================================')
print('we want to change bisis to a representation which jz are diagonalized.')
print('the eigenvaluses and eigenvectors of jz are:')
pprint(jz_cartesian.eigenvects())
print(('note: we need to choose proper coefficients and order of eigenvectors'
       + ' to ensure the results is the right form which we are familiar'
       + ' with in quantum mechanics.'))

u = Matrix([[-1/sqrt(2), 0, 1/sqrt(2)],
            [I/sqrt(2), 0, I/sqrt(2)],
            [0, 1, 0]])

print('so use transorm u**(-1) j u go to spherical representation:')
pprint(u)
print('the results are:')
pprint('jx_spherical:')
pprint(u**(-1) * jx_cartesian * u)
pprint('jy_spherical:')
pprint(u**(-1) * jy_cartesian * u)
pprint('jz_spherical:')
pprint(u**(-1) * jz_cartesian * u)
print('========================================================')

# p, d = jz_cartesian.diagonalize()
