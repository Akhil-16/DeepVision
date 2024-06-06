class TuringMachine:
    def __init__(self, states, input_alphabet, tape_alphabet, transitions, start_state, accept_states, reject_state):
        self.states = states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
        self.reject_state = reject_state
        self.current_state = start_state
        self.tape = []
        self.head_position = 0

    def load_input(self, input_str):
        self.tape = list(input_str)
        self.head_position = 0
        self.current_state = self.start_state

    def step(self):
        current_symbol = self.tape[self.head_position]
        if (self.current_state, current_symbol) in self.transitions:
            new_state, new_symbol, move_direction = self.transitions[(self.current_state, current_symbol)]
            self.tape[self.head_position] = new_symbol
            self.current_state = new_state
            if move_direction == 'R':
                self.head_position += 1
            elif move_direction == 'L':
                self.head_position -= 1
            return True
        else:
            self.current_state = self.reject_state
            return False

    def run(self):
        while self.current_state not in [self.accept_states, self.reject_state]:
            if not self.step():
                break
        return self.current_state in self.accept_states


class UniversalTuringMachine:
    def __init__(self, tm):
        self.tm = tm

    def simulate(self, input_str):
        self.tm.load_input(input_str)
        result = self.tm.run()
        if result:
            print(f'TM accepts input {input_str}')
        else:
            print(f'TM rejects input {input_str}')


# Define the components and transitions for a sample Turing Machine (TM)
tm_states = {'q0', 'q1', 'q2', 'q3'}
input_alphabet = {'0', '1'}
tape_alphabet = {'0', '1', 'X', 'Y', '_'}
transitions = {
    ('q0', '0'): ('q1', 'X', 'R'),
    ('q0', '1'): ('q1', 'Y', 'R'),
    ('q1', '0'): ('q1', '0', 'R'),
    ('q1', '1'): ('q1', '1', 'R'),
    ('q1', '_'): ('q2', '_', 'L'),
    ('q2', '0'): ('q3', 'X', 'L'),
    ('q2', '1'): ('q3', 'Y', 'L'),
    ('q3', 'X'): ('q0', 'X', 'R'),
    ('q3', 'Y'): ('q0', 'Y', 'R')
}
start_state = 'q0'
accept_states = {'q0'}
reject_state = 'q3'

tm = TuringMachine(tm_states, input_alphabet, tape_alphabet, transitions, start_state, accept_states, reject_state)

# Create a Universal Turing Machine (UTM) instance and simulate the TM
utm = UniversalTuringMachine(tm)
input_str = '101010'
utm.simulate(input_str)
