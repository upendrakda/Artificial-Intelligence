% Facts
child(ram, hari).
oversmart(hari).

% Rules
stupid(X) :-
    oversmart(X).

naughty(X) :-
    child(X, Y),
    stupid(Y).