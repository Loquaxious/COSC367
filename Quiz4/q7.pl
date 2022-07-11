solution(V1,V2,V3,H1,H2,H3):-
word(V1,_,H1V1,_,H2V1,_,H3V1,_),
word(H1,_,H1V1,_,H1V2,_,H1V3,_),
word(V2,_,H1V2,_,H2V2,_,H3V2,_),
word(H2,_,H2V1,_,H2V2,_,H2V3,_),
word(V3,_,H1V3,_,H2V3,_,H3V3,_),
word(H3,_,H3V1,_,H3V2,_,H3V3,_).

word(abalone,a,b,a,l,o,n,e).
word(abandon,a,b,a,n,d,o,n).
word(enhance,e,n,h,a,n,c,e).
word(anagram,a,n,a,g,r,a,m).
word(connect,c,o,n,n,e,c,t).
word(elegant,e,l,e,g,a,n,t).

test_answer :-
    findall((V1,V2,V3,H1,H2,H3), solution(V1,V2,V3,H1,H2,H3), L),
    sort(L,S),
    foreach(member(X,S), (write(X), nl)).

test_answer :- write('Wrong answer!'),
    halt.
