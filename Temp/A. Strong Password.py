def calculate_typing_time(s):
    if not s:
        return 0
    time = 2
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            time += 1
        else:
            time += 2
    return time

def max_typing_time_with_insertion(s):
    max_time = 0
    best_string = ""
    for i in range(len(s) + 1):
        for c in 'abcdefghijklmnopqrstuvwxyz':
            new_s = s[:i] + c + s[i:]
            current_time = calculate_typing_time(new_s)
            if current_time > max_time:
                max_time = current_time
                best_string = new_s
                
    return best_string, max_time
t = int(input())
for i in range(t):
    s = input()
    result = max_typing_time_with_insertion(s)
    print(result[0])
