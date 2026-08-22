% Facts
greedy_leader(shyam).
honest_leader(gopal).

% Rules
autocrat(X) :-
    greedy_leader(X).

evil(X) :-
    autocrat(X).