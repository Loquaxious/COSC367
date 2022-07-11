eats(X, Y) :- likes(X, Y).
eats(X, Y) :- hungry(X), edible(Y).

likes(bob, chocolate).
hungry(alice).

test_answer :- eats(bob, chocolate),
               writeln('Bob eats chocolate.').

edible(crisps).
hungry(bob).
likes(bob, sushi).

test_answer1 :- eats(bob, crisps),
              writeln('Bob eats crisps.').

/* This example shows how our incomplete definition of
rules can lead to unexpected (nonsense) answers. */

likes(alice, rock).
likes(alice, jazz).
edible(pizza).
hungry(bob).

test_answer2 :- eats(alice, rock),
               writeln('Alice eats rock!').
