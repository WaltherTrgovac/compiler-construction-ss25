from DFA import DFA
from ProductAutomaton import ProductAutomaton

# DFA for L_1 = {w | w starts with 0}
dfa_l1 = DFA(states={"q0", "q1"},
             alphabet={"0", "1"},
             transitions={
                 ("q0", "0"): "q0",
                 ("q0", "1"): "q1",
                 ("q1", "0"): "q1",
                 ("q1", "1"): "q1",
             },
             initial_state="q0",
             final_states={"q1"})

# DFA for L_2 = {w | w contains 1}
dfa_l2 = DFA(states={"r0", "r1", "r2"},
             alphabet={"0", "1"},
             transitions={
                 ("r0", "0"): "r1",
                 ("r0", "1"): "r2", 
                 ("r1", "0"): "r1",
                 ("r1", "1"): "r1",
                 ("r2", "0"): "r2",
                 ("r2", "1"): "r2"
             },
             initial_state="r0",
             final_states={"r1"})

dfa_l1.simulate("001")
dfa_l1.simulate("101")

# This is union product automaton
product_automaton = ProductAutomaton(dfa_l1, dfa_l2)
print(product_automaton)