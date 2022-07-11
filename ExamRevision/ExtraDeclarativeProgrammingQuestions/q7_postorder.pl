postorder(leaf(X), [X]).
postorder(tree(X, L, R), T) :-
  postorder(L, LT),
  postorder(R, RT),
  append(LT, RT, LRT),
  append(LRT, [X], T).

# postorder(leaf(X), [X]).  % Complete
# postorder(tree(Root, Left, Right), Traversal) :-
#     postorder(Left, LeftTraversal),  % Complete
#     postorder(Right, RightTraversal),  % Complete
#     append(LeftTraversal, RightTraversal, LeftRightTraversal),
#     append(LeftRightTraversal, [Root], Traversal).  % Complete

test_answer :- postorder(tree(a, leaf(b), leaf(c)), T), writeln(T).

test_answer1:- postorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T),
               writeln(T).
