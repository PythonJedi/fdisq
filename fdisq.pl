% Fully Dual Intuitionistic Sequent Calculus

%% See the readme for more information as to why.

:- module(fdisq [
    prove/2,
    operator(900, xfy, =>),   % -> doesn't have the correct precedence
    operator(900, yfx, <\=),  % explication is new...
    operator(900, fy, ~)]).   % ...as is unprovability

prove((Ant :- Con), Axioms) :-
    Ant = (HypA => ResA) ->
        Con = (HypC => ResC) ->
            prove((HypC :- HypA), AxHyp), % Inner implication
            prove((ResA :- ResC), AxRes),
            axiom_union(AxHyp, AxRes, Axioms)
        ;
            
