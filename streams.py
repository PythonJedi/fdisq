""" Attempt to do streams via coroutines, properly

Coroutines are cool and all, but by and large, they get messy. I want dataflow
programming in all its glory, and coroutines are background boilerplate to
that goal.

THEORY: Streams are the greatest fixed point of the functor 1+a*x with respect
to x. That is to say, streams are potentially unending conjunctions of 'a'
whatever type that might be. The three main components of streams are sources,
filters, and sinks. Sources produce streams lazily, and are thus lazily iterated
functions of type N -> N,A. Sinks are the corresponding end point, A,B->B where
B is often 1/Unit/NoneType. Filters are where all the power comes into play,
being lazily iterated A->B functions on elements of the stream.

Also to be considered is how to merge and split streams. Thankfully, the stream
system allows us to overload operators left right and center, to get a full set
of operators for combining sources and sinks"""

import types

class _Source:
    def __init__(self):
        self.targets = {}

    def __rshift__(self, other):
        self.targets[other] = True
        return other

    def __mul__(self, other):
        return _Pump(zip)(self, other)


class

# Source class, with curried init.
def _Lazy(func):
    class Source(_Source):
        _f = func
        def __init__(self, tail):
            self._tail = tail
            super(self)
        def run(self):
            while self._tail is not None:
                self._tail, value = self._f(self._tail)
                for target, pred in self.targets.items():
                    if pred(value):
                        target.send(value)
        def __next__():
            if self._tail is not None:
                self._tail, value = self._f(self._tail)
                return value
            else
                raise StopIteration()
    return Source

def _Pump(func):
    class Pump(_Source):
        def __init__(self, *args, **kwargs):
            self._gen = func(*args, **kwargs)
            self.__next__ = self._gen.__next__
            super(self)
        def run(self):
            for value in self._gen:
                for target, pred in self.targets.items():
                    if pred(value):
                        target.send(value)
    return Pump

# source decorator. if func is a generator, it wraps it with a pump
def source(func):
    if isinstance(func, types.GeneratorType):
        return _Pump(func)
    else:
        return _Lazy(func)


# sink decorator. ignores if func is already a generator.
# DO NOT decorate a producer with sink, it will not work
def sink(func):
    if isinstance(func, types.GeneratorType):
        return func
    else:
        def _Sink(tail):
            while tail is not None:
                tail = func((yield), tail)
        return _Sink

# Filter decorator
def filter(func):
