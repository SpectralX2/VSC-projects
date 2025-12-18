def find_treasure(map) : 
    # >>>>>> START - Your CODE goes below this line >>>>>>>>
    for i, row in enumerate(map):
        if 'X' in row:
            return i
    # <<<<<< END - Your CODE ends above this line <<<<<<<<<

# Test your function here
print(find_treasure(["....", "..X.", "...."]))  # Should print 1
print(find_treasure(["X...", "...."]))          # Should print 0
print(find_treasure(["....", "....", "..X.", "...."]))  # Should print 2