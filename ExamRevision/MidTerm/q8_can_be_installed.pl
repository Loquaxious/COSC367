can_be_installed(Software) :- requires(Software, SL), software_check(SL).
software_check([]).
software_check([H|T]) :- installed(X), member(H, X), software_check(T).


requires(prolog, [cmake, yaml, ncurses]).

installed([cmake, java]).
installed([yaml, json]).
installed([vim, emacs]).
installed([ncurses]).

test_answer :-
    can_be_installed(prolog),
    writeln("OK").

test_answer :-
    \+ can_be_installed(prolog),
    writeln("Wrong!").



requires(learn, [php, sql]).

installed([php, gcc]).

test_answer1 :-
    \+ can_be_installed(learn),
    writeln("OK").

test_answer1 :-
    can_be_installed(learn),
    writeln("Wrong!").
