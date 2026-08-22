% Facts
pompeian(marcus).
assassinate(marcus, caesar).
ruler(caesar).

% Rules
roman(X) :-
    pompeian(X).

not_loyal(X, Y) :-
    assassinate(X, Y),
    ruler(Y).

hate(X, Y) :-
    roman(X),
    ruler(Y),
    not_loyal(X, Y).