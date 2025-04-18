from DFA import DFA

import itertools 

class ProductAutomaton:
    def __init__(self, *dfa: DFA):
        self.dfas = dfa
        self.states: set[tuple] = set(itertools.product(*(d.states for d in dfa)))
        self.alphabet: set[str] = set().union(*(d.alphabet for d in dfa))
        self.transitions: dict[tuple[tuple[str, ...], str], tuple[str, ...]] = self.build_transitions()
        self.initial_state: tuple[str, ...] = tuple({d.initial_state for d in self.dfas})
        self.final_states: set[tuple[str, ...]] = self.build_final_states()

    def build_transitions(self) -> dict[tuple[tuple[str, ...], str], tuple[str, ...]] :
        transitions = {}
        for union_state in self.states:
            for symbol in self.alphabet:
                curr_to = []
                for state in union_state:
                    curr_transition = (state, symbol)
                    for dfa in self.dfas:
                        if curr_transition in dfa.transitions:
                            curr_to.append(dfa.transitions[curr_transition])
                            break
                transitions[(union_state, symbol)] = tuple(sorted(set(curr_to)))
        return transitions
    
    def build_final_states(self) -> set[tuple[str, ...]]:
        final_states = set()
        for d in self.dfas:
            for final_state in d.final_states:
                for state in self.states:
                    if final_state in state:
                        final_states.add(state)
        return final_states

    def __str__(self):
        return (
               f"States: {self.states}\n"
               f"Alphabet: {self.alphabet}\n"
               f"Transitions: {self.transitions}\n"
               f"Initial state: {self.initial_state}\n"
               f"Final states: {self.final_states}"
        )
