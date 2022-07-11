preorder(leaf(X), [X]).
preorder(tree(X, L, R), [X|T]):- preorder(L,LT), preorder(R,RT), append(LT, RT, T).

test_answer :- preorder(leaf(a), L),
               writeln(L).

test_answer1 :- preorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T),
               writeln(T).
