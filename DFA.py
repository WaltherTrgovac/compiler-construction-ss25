class DFA:
    def __init__(self, states: set[str],
                alphabet: set[str],
                transitions: dict[tuple[str, str], str],
                initial_state: str, 
                final_states: set[str]):
                self.states = states
                self.alphabet = alphabet
                self.transitions = transitions 
                self.initial_state = initial_state
                self.final_states = final_states


    def __str__(self):
        return (
               f"States: {self.states}\n"
               f"Alphabet: {self.alphabet}\n"
               f"Transitions: {self.transitions}\n"
               f"Initial state: {self.initial_state}\n"
               f"Final states: {self.final_states}"
        )

    def simulate(self, word: str):
        current_state = self.initial_state
        for char in word: 
            if char not in self.alphabet:
                  raise ValueError(f"The following character is not in the alphabet: {char}")

            key = (current_state, char)
            if key not in self.transitions:
                  raise ValueError(f"There is no transition defined for {key}")

            current_state = self.transitions[key]
            print(f"Current char: {char}\n"
                  f"Taking transition from state {key[0]} to {current_state}")

        if current_state in self.final_states:
              print("Your word has been accepted")
        else:
              print("Your word has not been accepted")
              
# DFA for regular expression a*b
# q3 is used as a state that leads to nothing
dfa = DFA(states={"q1", "q2", "q3"},
          alphabet={"a", "b"},
          transitions={("q1", "a"): "q1",
           ("q1", "b"): "q2", 
           ("q2", "a"): "q3",
           ("q2", "b"): "q3", 
           ("q3", "a"): "q3", 
           ("q3", "b"): "q3"}, 
           initial_state="q1", 
           final_states={"q2"})

print(dfa)
dfa.simulate("aaab")