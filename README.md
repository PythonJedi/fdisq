# Fully Dual Intuitionistic Sequent Calculus

This project is a minimal implementation of FDISQ in prolog. Its purpose is to
explore the logic system and its limits in terms of provability.

# What is FDISQ?

Firstly, FDISQ is a sequent calculus. This is a form of logic proof first
developed by Gentzen. Any step of a proof has a turnstile ( :- ) operator in it.
The terms to the left of the turnstile are the antecedent, the thing(s) assumed
true. The terms to the right of the turnstile are the consequent, the thing(s)
to be proven. There are a set of transformations to turn sequents into simpler
sequents, and eventually any sequent can be reduced to a collection of sequents
with atomic antecedents and consequents. If all of these base forms are valid,
the original sequent being reduced is considered valid.

FDISQ is an Intuitionistic sequent calculus. This means it follows in the
spirit of constructive mathematics and intuitionism. What thsi boils down to is
being open to the idea of statements that are neither true nor false. Or more
precicely, statements that are unprovable. This is accomplished by creating a
structure known as a "lattice" based on the provability of propositions. A
lattice is a partially ordered set, where things can be less than or equal to
other things, but there can exist pairs of things that can't be compared. The
name lattice comes from how these structures are drawn out, with incomparable
elements in the same horizontal row, rows laid out in descending order, and
lines between comparable elements. For a complex enough set, the comparability
lines begin to look like slats in a physical lattice.

Finally, FDISQ is fully dual. This means that every level of connective and
quantifier is present, and both sides of the duality are present. This property
is the main reason for studying FDISQ, as no other logic has all 8 connectives
and quantifiers. The connectives are conjunction, disjunction, implication, and
explication (converse nonimplication).

Explication deserves some explanation, as it is one of the lesser known
connectives. It essentially states that the left operand is not implied by the
right operand. However, it has some extra finesse to it in intuitionistic logic.
There, `B </= A` is the smallest term such that `A :- B </= A ; B` is true. This
"law of exclusive implication" is the parallel to implication's Modus Ponens
(`P , P => Q :- Q`), and states that from A, we can conclude B, or that B is not
implied by A. This is a weaker form of the law of excluded middle in classical
logic: `forall(x| x ; -x)`. In a way, it is weakened just enough to be useful in
intuitionistic logic without closing the world. In fact, we can use explication
to express negation by failure, or more precicely, to create a unary operand
stating unprovability. If we have put in place a set of sequents as
axiomatically valid, we can then ask the question `P </= T`, there exists a
proof of True that cannot be turned into a proof of P. We can name this operator
` ~P `, and use it alongside `-P`.

The quantifiers in FDISQ are universal, existential, inductive, and coinductive.
The universal and existential quantifiers are generally well behaved, though
they can produce an atomic variable that can only be eliminated by self-proof
(`A :- A`) on certain sides of the turnstile. The inductive and coinductive
quantifiers are new kids on the block. FDISQ does not allow unquantified
self-reference, but uses these quantifiers to recapture the self-referential
thought processes necessary to do more complex logic. Inductive quantification
is proven by a generalized principle of induction, where the base case is
proven, and then the inductive step assumes a transition exists, and shows that
it commutes with injection. Coinductive quantification is similar, but
instead works with objects that have infinite proofs. It proves a finite case,
assumes a map exists, and shows the assumed map commutes with the projection
used to define the coinduction. In this way, we can talk about proofs of
finite arbitrary length, or even infinite length.
