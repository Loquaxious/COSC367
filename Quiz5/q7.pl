preorder(leaf(Label), [Traversal]) :- Traversal = Label.
preorder(tree(Root, LS, RS), [Root|Traversal]) :- preorder(LS, LT), preorder(RS, RT), append(LT, RT, Traversal).

test_answer0 :- preorder(leaf(a), L),
               writeln(L).

test_answer1 :- preorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T),
              writeln(T).
