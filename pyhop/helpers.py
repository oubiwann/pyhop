def is_done(b1,state,goal, done_state):
    if b1 == done_state: return True
    if b1 in goal.pos and goal.pos[b1] != state.pos[b1]:
        return False
    if state.pos[b1] == done_state: return True
    return is_done(state.pos[b1],state,goal,done_state)

def all(state):
    return state.clear.keys()
