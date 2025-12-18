def alien_translator(text) : 
    # >>>>>> START - Your CODE goes below this line >>>>>>>>
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char in vowels:
            result += "*"
        else:
            result += char
    return result
    # <<<<<< END - Your CODE ends above this line <<<<<<<<<

# Test your function here
print(alien_translator("Hello"))           # Should print "H*ll*"
print(alien_translator("I come in peace")) # Should print "* c*m* *n p**c*"
print(alien_translator("Thank You")) # Should print "Th*nk Y**"