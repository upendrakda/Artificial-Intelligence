% HCF using Euclidean Algorithm
hcf(A, 0, A).

hcf(A, B, H) :-
    B > 0,
    R is A mod B,
    hcf(B, R, H).

% LCM using HCF
lcm(A, B, L) :-
    hcf(A, B, H),
    L is (A * B) // H.