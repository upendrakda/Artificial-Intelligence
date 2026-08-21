% Facts
mammal(horse).
mammal(cow).
mammal(pig).

horse(bluebeard).

parent(bluebeard, charlie).

% Rules

% An offspring of a horse is a horse
horse(X) :-
    offspring(X, Y),
    horse(Y).

% Offspring and parent are inverse relations
offspring(X, Y) :-
    parent(Y, X).

% Every horse is a mammal
mammal(X) :-
    horse(X).

% Every mammal has a parent
has_parent(X) :-
    mammal(X),
    parent(_, X).