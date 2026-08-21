% Facts
american(george).
country(iraq).
enemy(iraq, america).
missiles(iraq).
sold_by(iraq, george).
weapon(missiles).

% Rules
hostile(X) :-
    enemy(X, america).

criminal(X) :-
    american(X),
    sold_by(iraq, X),
    hostile(iraq),
    weapon(missiles).