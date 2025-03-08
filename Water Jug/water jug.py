def waterJugProblem(capacity1, capacity2, goal):
    stack = []
    visited = set()

    stack.append((0, 0))  
    visited.add((0, 0))

    actions = []

    while stack:
        jug1, jug2 = stack.pop()
        actions.append((jug1, jug2))

        # Check if target is achieved
        if jug1 == goal or jug2 == goal:
            print("\nSolution Found:\n")
            for i, action in enumerate(actions):
                print(f"Step {i + 1}: {action}")
            return True

        #Rules
        possible_moves = [
            ((capacity1, jug2), "Fill Jug 1"),  # 1: Fill jug1
            ((jug1, capacity2), "Fill Jug 2"),  # 2: Fill jug2
            ((0, jug2), "Empty Jug 1"),         # 3: Empty jug1
            ((jug1, 0), "Empty Jug 2"),         # 4: Empty jug2
            ((max(0, jug1 - (capacity2 - jug2)), min(capacity2, jug1 + jug2)), "Pour from Jug 1 to Jug 2"),  # 5: Pour jug1 → jug2
            ((min(capacity1, jug1 + jug2), max(0, jug2 - (capacity1 - jug1))), "Pour from Jug 2 to Jug 1"),  # 6: Pour jug2 → jug1
        ]

        for state, move in possible_moves:
            if state not in visited:
                visited.add(state)
                stack.append(state)
                print(f"Action: {move} → New State: {state}")

    print("\nNo Solution Found")
    return False

jug1Capacity = 4
jug2Capacity = 3
target = 2          

waterJugProblem(jug1Capacity, jug2Capacity, target)
