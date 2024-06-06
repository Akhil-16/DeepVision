class TuringMachine:
    def __init__(self, tape, initial_state, final_state):
        self.tape = tape
        self.head = 0
        self.state = initial_state
        self.final_state = final_state

    def step(self, transition_function):
        if self.state == self.final_state:
            return False  

        if self.head < 0 or self.head >= len(self.tape):
            return False

        current_symbol = self.tape[self.head]
        if (self.state, current_symbol) not in transition_function:
            return False  # Transition not defined

        next_state, write_symbol, move_direction = transition_function[(self.state, current_symbol)]
        self.tape[self.head] = write_symbol
        if move_direction == 'R':
            self.head += 1
        elif move_direction == 'L':
            self.head -= 1
        self.state = next_state
        
        return True

    def run(self, transition_function):
        while self.step(transition_function):
            pass

class UniversalTuringMachine:
    def __init__(self):
        pass

    def simulate(self, tm, input_string):
        tm_instance = TuringMachine(list(input_string), tm.initial_state, tm.final_state)
        tm_instance.run(tm.transition_function)

        if tm_instance.state == tm.final_state:
            return "Accepted"
        else:
            return "Rejected"

class TMDescription:
    def __init__(self, initial_state, final_state, transition_function):
        self.initial_state = initial_state
        self.final_state = final_state
        self.transition_function = transition_function

def main():
    # Define the Turing Machine description
    initial_state_tm = 'q0'
    final_state_tm = 'q4'
    transition_function_tm = {
        ('q0', 'a'): ('q1', 'X', 'R'),
        ('q0', 'Y'): ('q3', 'Y', 'R'),
        ('q1', 'a'): ('q1', 'a', 'R'),
        ('q1', 'b'): ('q2', 'Y', 'L'),
        ('q1', 'Y'): ('q1', 'Y', 'R'),
        ('q2', 'a'): ('q2', 'a', 'L'),
        ('q2', 'X'): ('q0', 'X', 'R'),
        ('q2', 'Y'): ('q2', 'Y', 'L'),
        ('q3', 'Y'): ('q3', 'Y', 'R'),
        ('q3', 'B'): ('q4', 'B', 'L')
    }
    tm_description = TMDescription(initial_state_tm, final_state_tm, transition_function_tm)

    # Create the Universal Turing Machine
    utm = UniversalTuringMachine()

    # Get input from the user
    input_string = input("Enter the input string: ")

    # Simulate the Turing Machine using the UTM
    result = utm.simulate(tm_description, input_string)
    print("Result:", result)

if __name__ == "__main__":
    main()
