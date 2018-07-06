import itertools
import actions

def solve(start, goal, moves, available_actions):
    # generate all possible action sequences of length 'moves'
    action_sequences = itertools.product(available_actions, repeat=moves)

    # test each sequence
    for seq in action_sequences:
        num = start
        
        # apply all actions in sequence
        for a in seq:
            num = actions.ACTIONS[a[0]](a[1], num)

        # return the sequence if the final num matches the goal
        if num == goal:
            return seq


if __name__ == "__main__":
    # get round parameters
    start = input("Start number: ")
    goal = input("Goal number: ")
    moves = input("Number of moves: ")

    # setup input of available actions
    num_actions = input("Number of actions: ")
    available_actions = []
    
    # get available actions
    for i in range(num_actions):
        action = []
        action.append(raw_input("Operation type for action #" + str(i+1) + ": "))
        action.append(input("Value for action #" + str(i+1) + ": "))
        available_actions.append(action)

    # print solution sequence
    print "Solution sequence: " + str(solve(start, goal, moves, available_actions))