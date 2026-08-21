% Fibonacci series
fibonacci(0, 0).
fibonacci(1, 1).

fibonacci(N, F) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fibonacci(N1, F1),
    fibonacci(N2, F2),
    F is F1 + F2.

% Print Fibonacci series
fib_series(N) :-
    fib_series(0, N).

fib_series(I, N) :-
    I < N,
    fibonacci(I, F),
    write(F),
    write(' '),
    I1 is I + 1,
    fib_series(I1, N).

fib_series(N, N).