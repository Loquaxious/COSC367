leaves([], []).
leaves(tree([H|T]), [H|LS]) :- atom(H), leaves(T, LS).
leaves(tree([H|T]), LS) :- \+ atom(H), leaves(H, LH), leaves(T, LT), append(LH, LT, LS).
leaves([H|T], LS) :- \+ atom(H), leaves(H, LH), leaves(T, LT), append(LH, LT, LS).
leaves([H|T], [H|LS]) :- atom(H), leaves(T, LS).


test_answer :- leaves(tree([the_only_leaf]), Leaves),
               writeln(Leaves).

test_answer1 :- leaves(tree([a, tree([b,c,d])]), L),
               writeln(L).

test_answer2 :- leaves(tree([tree([e]), b, tree([d, f])]), Leaves),
                writeln(Leaves).
