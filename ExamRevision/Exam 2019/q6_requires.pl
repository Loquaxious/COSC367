can_be_installed(Software) :- requires(Software, SL), is_installed(SL).
is_installed([]).
is_installed([H|T]) :- installed(IL), member(H, IL), is_installed(T).


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
