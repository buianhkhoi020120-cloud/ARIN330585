import random

N = 3
M = 4
environment = {}
for x in range(N):
    for y in range(M):
        environment[(x, y)] = random.choice([0, 1])  # 0: sạch, 1: bẩn


# ===== INTERPRET INPUT =====
def interpret_input(percept):
    position = percept
    x, y = position
    
    state_value = environment[(x, y)]
    moves = []

    if x > 0:
        moves.append("Up")
    if x < N - 1:
        moves.append("Down")
    if y > 0:
        moves.append("Left")
    if y < M - 1:
        moves.append("Right")

    state = (position, state_value, moves)
    return state

def rule_match(state, rules):
    position, state_value, moves = state
    for rule in rules:
        if rule["condition"](state):
            return rule
    return None

rules = [
    {
        "condition": lambda state: state[1] == 1,  # bẩn
        "action": "SUCK"
    },
    {
        "condition": lambda state: state[1] == 0,  # sạch
        "action": "MOVE"
    }
]


# ===== SIMPLE REFLEX AGENT =====
def simple_reflex_agent(percept):
    state = interpret_input(percept)
    rule = rule_match(state, rules)

    if rule["action"] == "SUCK":
        return "SUCK"
    else:
        _, _, moves = state
        return random.choice(moves)

position = (0, 3)

def main():
    global position

    for step in range(15):
        percept = position
        action = simple_reflex_agent(percept)
        x, y = position
        print(f"Step {step}: Pos={position}, State={environment[(x,y)]}, Action={action}")

        if action == "SUCK":
            environment[(x, y)] = 0
        elif action == "Up":
            position = (x - 1, y)
        elif action == "Down":
            position = (x + 1, y)
        elif action == "Left":
            position = (x, y - 1)
        elif action == "Right":
            position = (x, y + 1)

if __name__ == "__main__":
    main()