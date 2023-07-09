import json, sys
# 20213006500 e 20213001488
# Ivia Marques Pereira Costa e Joao Victor Peluci G. de S. Valente

# Verifies input
if len(sys.argv) != 3:
    print("Usar: ./mt [MT] [Word]")
# Reads input
else:
    filename = sys.argv[1]
    entry_word = list(sys.argv[2])

# Opens file
file = open(filename, "r")
file_json = json.load(file)
file.close()

# Storing variables
mt = list(file_json.keys())[0]

num_trails = file_json[mt][0]
states = file_json[mt][1]
alphabet = file_json[mt][2]
symbols = file_json[mt][3]
symbol_start = file_json[mt][4]
symbol_empty = file_json[mt][5]
transitions = file_json[mt][6]
initial_state = file_json[mt][7]
final_states = file_json[mt][8]

# Formatting word
entry_word.append(symbol_empty)
entry_word.insert(0, symbol_start)

# Creating k new trails and filling them with _ (underscore) the same size of our word
trails = list()
trails.append(entry_word)

for i in range(1, num_trails):
    new_trail = list()
    for i in range(len(entry_word)):
        new_trail.append(symbol_empty)
    trails.append(new_trail)

# Initializing state, position, read and variables
current_state = initial_state
index = 1
move = True
result = "Não"

# Turing Machine
while move:
    possible_transitions = list(transitions)
    impossible_transitions = list()

    # To discover next transition
    for t in possible_transitions:
        if t[0] != current_state:
            if t not in impossible_transitions:
                impossible_transitions.append(t)

        # Multiple trails
        for i in range(1, num_trails + 1):
            if t[i] != trails[i - 1][index]:
                if t not in impossible_transitions:
                    impossible_transitions.append(t)

    # To remove impossible transitions from list
    for t in impossible_transitions:
        if t in possible_transitions:
            possible_transitions.remove(t)

    # If no possible transitions, stop
    if len(possible_transitions) == 0:
        move = False
        break

    # Else, move
    else:
        # Temporary variable
        current_transition = list(possible_transitions[0])
        
        # Changes state
        current_state = current_transition[num_trails + 1]

        # Write back in trail
        for i in range(num_trails):
            trails[i][index] = current_transition[i+num_trails+2]

        # Move on trail
        if current_transition[len(current_transition) - 1] == '>':
            index = index + 1
        elif index > 0:
            index = index - 1
        else:
            break

# Decides whether the word was read or not
if current_state in final_states:
    result = "Sim"

print(result)