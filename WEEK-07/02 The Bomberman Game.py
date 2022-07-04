def flipped(g):
    grid = g.copy()
    m = len(grid)
    n = len(grid[0])
    fgrid = []
    for i in range(m):
        raw = ''
        for j in range(n):
            if grid[i][j] == 'O' \
            or grid[i][j] == '*' \
            or (i-1 >=0 and grid[i-1][j] == 'O')    \
            or (i+1 < m and grid[i+1][j] == 'O')    \
            or (j-1 >=0 and grid[i][j-1] == 'O')    \
            or (j+1 < n and grid[i][j+1] == 'O')    :
                raw += '*'
            else:
                raw += '.'
        fgrid.append(raw)
    dgrid = []
    for i in range(m):
        raw = ''
        for j in range(n):
            raw += '.' if fgrid[i][j] == '*' else 'O'
        dgrid.append(raw)
    return dgrid

def plant_all(g):
    grid = g.copy()
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        grid[i] = 'O'*n
    return grid

def bomberMan(n, grid):
    if (n==1) : return grid
    if (n-1) % 4 == 0: return flipped(flipped(grid))
    if n % 2 ==0 : return plant_all(grid)    
    return flipped(grid)

# Kunal Wadhwa
