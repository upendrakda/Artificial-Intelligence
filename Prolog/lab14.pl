% Facts
dog(puppy).

% Rules
animal(X) :-
    dog(X).

die(X) :-
    animal(X).