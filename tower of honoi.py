def tower_of_hanoi_iterative(n, source, target, auxiliary):
    if n == 0:  # Base case: No disks to move
        return
    moves = 0  # Initialize moves counter
    stack = [(n, source, target, auxiliary)]  # Initialize stack for iterative approach
    while stack:
        n, source, target, auxiliary = stack.pop()  # Retrieve parameters from the stack
        if n == 1:  # Base case: Move a single disk
            print(f"Move disk 1 from {source} to {target}")
            moves += 1  # Increment moves counter
        else:  # Recursive case
            # Push sub-problems onto the stack
            stack.append((n - 1, auxiliary, target, source))  # Move n-1 disks from source to auxiliary
            stack.append((1, source, target, auxiliary))  # Move the largest disk from source to target
            stack.append((n - 1, source, auxiliary, target))  # Move n-1 disks from auxiliary to target
            moves += 2**n - 1  # Calculate the total number of moves
    return moves  # Return the total number of moves


# Test the implementation with 3 disks
n_disks = 3
total_moves = tower_of_hanoi_iterative(n_disks, 'A', 'C', 'B')
print(f"Total number of moves: {total_moves}")
