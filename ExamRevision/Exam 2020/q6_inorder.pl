inorder(leaf(X), [X]).
inorder(tree(H, L, R), T) :- inorder(L, LT), append(LT, [H], LHT),
inorder(R, RT), append(LHT, RT, T).

test_answer :- inorder(tree(1, leaf(2), leaf(3)), T), writeln(T).

test_answer1 :- inorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T),
               writeln(T).
