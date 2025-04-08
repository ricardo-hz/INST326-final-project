print("Hello, Git!")
# Practicing git add, git commit, and git push
print("This is a change I made!: Nathan C")

print("This is a change that Aviva S. made!")

# Checks if a number is even (This function was used to practice merge conflict)
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
def is_even_but_better(number):
    # from phoenix. this is totally a better way of implementing this.
    if number < 0:
        # all negative numbers are OBVIOUSLY even.
        return True
    elif number == 0:
        return True
    elif number == 1:
        return False
    else:
        return is_even_but_better(number - 2)