class SimpleReflexAgent:
    def __init__(self):
        self.rules = {
            "UP": "Di chuyển ô trống lên trên",
            "DOWN": "Di chuyển ô trống xuống dưới",
            "LEFT": "Di chuyển ô trống sang trái",
            "RIGHT": "Di chuyển ô trống sang phải"
        }
        self.goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    def interpret_input(self, percept):
        return tuple(percept)

    def rule_match(self, state, rules):
        empty_idx = state.index(0)

        goal_val_at_empty = self.goal_state[empty_idx]
        current_val_pos = state.index(goal_val_at_empty)

        r_empty, c_empty = empty_idx // 3, empty_idx % 3
        r_val, c_val = current_val_pos // 3, current_val_pos % 3
        
        if r_val < r_empty: return "UP"
        if r_val > r_empty: return "DOWN"
        if c_val < c_empty: return "LEFT"
        if c_val > c_empty: return "RIGHT"
        
        return "NONE"

    def agent_function(self, percept):
        state = self.interpret_input(percept)
        
        if state == self.goal_state:
            return "DONE"
            
        action_key = self.rule_match(state, self.rules)
        return action_key

def move(state, action):
    new_state = list(state)
    idx = new_state.index(0)
    if action == "UP": new_state[idx], new_state[idx-3] = new_state[idx-3], new_state[idx]
    elif action == "DOWN": new_state[idx], new_state[idx+3] = new_state[idx+3], new_state[idx]
    elif action == "LEFT": new_state[idx], new_state[idx-1] = new_state[idx-1], new_state[idx]
    elif action == "RIGHT": new_state[idx], new_state[idx+1] = new_state[idx+1], new_state[idx]
    return tuple(new_state)

def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print("---")

if __name__ == "__main__":
    initial_percept = (1, 2, 3, 4, 5, 0, 7, 8, 6) 
    
    agent = SimpleReflexAgent()
    current_state = initial_percept
    
    print("Trạng thái bắt đầu:")
    print_board(current_state)
    
    steps = 0
    while steps < 10: 
        action = agent.agent_function(current_state)
        
        if action == "DONE":
            print("Đã đạt đến trạng thái đích!")
            break
        if action == "NONE":
            print("Không tìm thấy bước đi phù hợp.")
            break
            
        print(f"Bước {steps+1}: Action = {action}")
        current_state = move(current_state, action)
        print_board(current_state)
        
        steps += 1