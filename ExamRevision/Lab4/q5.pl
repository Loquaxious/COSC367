/* tear rate related clauses */
normal_tear_rate(RATE) :- RATE >= 5.
low_tear_rate(RATE) :- RATE < 5.

/* age-related clauses */
young(AGE) :- AGE < 45.

diagnosis(Recommned, Age, Astigmatic, Tear_Rate) :- Recommned = no_lenses,
low_tear_rate(Tear_Rate).
diagnosis(Recommned, Age, Astigmatic, Tear_Rate) :- Recommned = hard_lenses,
young(Age), normal_tear_rate(Tear_Rate), Astigmatic = yes.
diagnosis(Recommned, Age, Astigmatic, Tear_Rate) :- Recommned = soft_lenses,
young(Age), normal_tear_rate(Tear_Rate), Astigmatic = no.

test_answer :-
    diagnosis(hard_lenses, 21, yes, 11),
    writeln('OK').

test_answer1 :-
    diagnosis(X, 45, no, 4),
    writeln(X).

test_answer2 :-
    diagnosis(X, 19, no, 5),
    writeln(X).
