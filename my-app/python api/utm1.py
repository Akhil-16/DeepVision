class TuringMachine:
    def __init__(self, states, alphabet, transitions, initial_state, accepting_state, rejecting_state):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.accepting_state = accepting_state
        self.rejecting_state = rejecting_state

    def run(self, input_str):
        tape = list(input_str)
        current_state = self.initial_state
        head_position = 0

        while current_state != self.accepting_state and current_state != self.rejecting_state:
            symbol_under_head = tape[head_position]
            if (current_state, symbol_under_head) in self.transitions:
                new_state, new_symbol, direction = self.transitions[(current_state, symbol_under_head)]
                tape[head_position] = new_symbol
                current_state = new_state
                if direction == 'R':
                    head_position += 1
                elif direction == 'L':
                    head_position -= 1
            else:
                current_state = self.rejecting_state

            if head_position < 0 or head_position >= len(tape):
                current_state = self.rejecting_state

        if current_state == self.accepting_state:
            print("TM Accepts")
        else:
            print("TM Rejects")

class UniversalTuringMachine:
    def __init__(self, tm, input_str):
        self.tm = tm
        self.input_str = input_str

    def run(self):
        self.tm.run(self.input_str)

# Define TM transitions for a^nb^n where n >= 1
tm_states = {'q0', 'q1', 'q2', 'q3', 'q4'}
tm_alphabet = {'a', 'b', 'X', 'Y', '_'}
tm_transitions = {
    ('q0', 'a'): ('q1', 'X', 'R'),  # Replace 'a' with 'X'
    ('q0', 'Y'): ('q3', 'Y', 'R'),  # Skip 'Y'
    ('q1', 'a'): ('q1', 'a', 'R'),  # Skip 'a'
    ('q1', 'b'): ('q2', 'Y', 'L'),  # Replace 'b' with 'Y'
    ('q1', 'Y'): ('q1', 'Y', 'R'),  # Skip 'Y'
    ('q2', 'a'): ('q2', 'a', 'L'),  # Skip 'a'
    ('q2', 'X'): ('q0', 'X', 'R'),  # Replace 'X' with 'a'
    ('q2', 'Y'): ('q2', 'Y', 'L'),  # Skip 'Y'
    ('q3', 'Y'): ('q3', 'Y', 'R'),  # Skip 'Y'
    ('q3', '_'): ('q4', '_', 'R')   # Move right until encountering '_'
}
tm_initial_state = 'q0'
tm_accepting_state = 'q4'
tm_rejecting_state = 'q2'

tm = TuringMachine(tm_states, tm_alphabet, tm_transitions, tm_initial_state, tm_accepting_state, tm_rejecting_state)

# Input string to test
input_str = "aabb"
utm = UniversalTuringMachine(tm, input_str)
utm.run()
