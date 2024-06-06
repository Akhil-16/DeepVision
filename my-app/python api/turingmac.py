class TuringMachine:
    def __init__(self, tape, initial_state, final_state):
        self.tape = tape
        self.head = 0
        self.state = initial_state
        self.final_state = final_state

    def step(self, transition_function):
        if self.state == self.final_state:
            return False  

        print("Current state:", self.state)
        print("Current head position:", self.head)
        print("Tape:", self.tape)

        if self.head < 0 or self.head >= len(self.tape):
            print("Head out of bounds!")
            return False

        current_symbol = self.tape[self.head]
        if (self.state, current_symbol) not in transition_function:
            
            print("Transition not defined for current state and symbol!",self.state,current_symbol)
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

def main():
    tape = list(input("Enter the input tape: "))  # e.g., 'aaabbb'
    initial_state = 'q0'
    final_state = 'q4'
    transition_function = {
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

    tm = TuringMachine(tape, initial_state, final_state)
    tm.run(transition_function)

    if tm.state == final_state:
        print("Accepted")
    else:
        print("Rejected")

if __name__ == "__main__":
    main()
