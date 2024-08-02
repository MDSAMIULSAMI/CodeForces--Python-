def count_cells_to_form_three_regions(t, test_cases):
    results = []
    
    for case in test_cases:
        n, grid = case
        regions = [[0]*n for _ in range(2)]
        region_id = 0
        
        def dfs(x, y, region_id, grid, regions):
            if x < 0 or x >= 2 or y < 0 or y >= n or grid[x][y] == 'x' or regions[x][y] != 0:
                return
            regions[x][y] = region_id
            stack = [(x, y)]
            while stack:
                cx, cy = stack.pop()
                for nx, ny in [(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)]:
                    if 0 <= nx < 2 and 0 <= ny < n and grid[nx][ny] == '.' and regions[nx][ny] == 0:
                        regions[nx][ny] = region_id
                        stack.append((nx, ny))
        for i in range(2):
            for j in range(n):
                if grid[i][j] == '.' and regions[i][j] == 0:
                    region_id += 1
                    dfs(i, j, region_id, grid, regions)
        count = 0
        for i in range(2):
            for j in range(n):
                if grid[i][j] == '.':
                    regions_after_block = [[0]*n for _ in range(2)]
                    region_id_after_block = 0
                    new_grid = [list(row) for row in grid]
                    new_grid[i][j] = 'x'
                    for x in range(2):
                        for y in range(n):
                            if new_grid[x][y] == '.' and regions_after_block[x][y] == 0:
                                region_id_after_block += 1
                                dfs(x, y, region_id_after_block, new_grid, regions_after_block)
                    
                    if region_id_after_block == 3:
                        count += 1
        
        results.append(count)
    
    return results

if __name__ == "__main__":
    t = int(input())
    test_cases = []
    
    for _ in range(t):
        n = int(input())
        grid = []
        for _ in range(2):
            grid.append(input())
        test_cases.append((n, grid))
    
    results = count_cells_to_form_three_regions(t, test_cases)
    for result in results:
        print(result)
