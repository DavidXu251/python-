
import os
for x in os.environ.items():
    print(x[0], x[1])

print(os.environ['PROVER9'])

import nltk
read_expr=nltk.sem.Expression.fromstring
prover9=nltk.Prover9()

print(prover9.prove(
    read_expr('mortal(socrates)'),
    [
    read_expr('all x.(man(x) -> mortal(x))'),
    read_expr('man(socrates)')
    ]))
