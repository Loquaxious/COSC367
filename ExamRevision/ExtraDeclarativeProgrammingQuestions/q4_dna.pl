dna([], []).
dna([L|Ls], [R|Rs]) :- ((L=c, R=g); (L=g, R=c); (L=a, R=t); (L=t, R=a)), dna(Ls, Rs).

test_answer :- dna([a, t, c, g], X),
               writeln(X).

test_answer1 :- dna(X, [t, a, g, c]),
               writeln(X).
