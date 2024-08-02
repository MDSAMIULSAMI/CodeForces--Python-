def minimum_cost_to_restore_rbs(t, test_cases):
    results = []
    
    for i in range(t):
        n = test_cases[i][0]
        s = test_cases[i][1]
        
        # Create a list to store the final characters
        final_s = list(s)
        
        # Use a stack to keep track of the positions of '('
        stack = []
        
        # Initialize the cost
        cost = 0
        
        # Iterate through the even positions
        for j in range(n):
            if j % 2 == 0:
                # For odd positions (0-indexed), we need to insert a bracket
                if stack and final_s[stack[-1]] == '(' and final_s[j + 1] == ')':
                    # If the top of the stack is an opening bracket and the current is a closing bracket
                    # Then we form a pair and pop from stack
                    final_s[j] = '('
                    cost += (j + 1 - stack[-1])
                    stack.pop()
                else:
                    # Else we insert an opening bracket
                    final_s[j] = '('
                    stack.append(j)
            else:
                # For even positions, we just process according to the character already present
                if final_s[j] == '(':
                    stack.append(j)
                elif final_s[j] == ')':
                    if stack:
                        cost += (j + 1 - stack[-1])
                        stack.pop()
        
        # Append the calculated cost for this test case
        results.append(cost)
    
    return results

# Reading input from user interactively
def main():
    t = int(input())
    test_cases = []
    
    for _ in range(t):
        n = int(input())
        s = input()
        test_cases.append((n, s))
    
    results = minimum_cost_to_restore_rbs(t, test_cases)
    
    for result in results:
        print(result)

# Run the main function
if __name__ == "__main__":
    main()
