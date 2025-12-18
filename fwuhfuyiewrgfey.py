def print_image(height=10):
    # ASCII art of a cat (adjust the size by changing `height`)
    for i in range(1, height+1):
        if i == 3 or i == 7:
            print(' /_/\\ ' + '_' * (i-2) + '\\_' * (i))
        elif i == 5:
            print('| | |' + '|-' * (height - 4) + '| |')
        else: 
            print('_/' + '|' * (i-1) + '\\_' * (i))

print_image()
