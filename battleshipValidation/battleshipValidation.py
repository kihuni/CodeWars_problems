def validate_battlefield(board):
    visited = [[False] * 10 for _ in range(10)]
    
    # directions for up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Check if a given cell is inside the board and not visited yet.
    def is_valid(x, y):
        return 0 <= x < 10 and 0 <= y < 10 and not visited[x][y] and board[x][y] == 1

    # Depth First Search to count cells of a ship and ensure it's straight.
    def dfs(x, y):
        visited[x][y] = True
        size = 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                size += dfs(nx, ny)
                break   # A ship must be a straight line, so only one direction can be valid
        return size

    ships_count = {1: 0, 2: 0, 3: 0, 4: 0}
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1 and not visited[i][j]:
                ship_size = dfs(i, j)
                # Check for invalid ship size
                if ship_size > 4:
                    return False
                ships_count[ship_size] += 1
    
    # Check if the ships are touching each other
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                # Check the diagonal directions for touching ships
                for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < 10 and 0 <= ny < 10 and board[nx][ny] == 1:
                        return False

    return ships_count == {1: 4, 2: 3, 3: 2, 4: 1}

# Test
board_example = [
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 0, 0, 0, 0]
]

print(validate_battlefield(board_example))  

