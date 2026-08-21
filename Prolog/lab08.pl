% 8-Queen Problem

queens(Solution) :-
    permutation([1,2,3,4,5,6,7,8], Solution),
    safe(Solution).

% Check whether all queens are safe
safe([]).

safe([Queen|Others]) :-
    no_attack(Queen, Others, 1),
    safe(Others).

% Check that the queen does not attack any other queen
no_attack(_, [], _).

no_attack(Queen, [Next|Others], Distance) :-
    Queen =\= Next,
    abs(Queen - Next) =\= Distance,
    Distance1 is Distance + 1,
    no_attack(Queen, Others, Distance1).