mirror(leaf(X), leaf(Y)) :- X = Y.
mirror(tree(A,B), tree(X,Y)) :- mirror(A, Y), mirror(B, X).
