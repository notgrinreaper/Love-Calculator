print("❤️ Welcome to the Love Calculator! ❤️")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = (name1 + name2).lower()

# Count TRUE
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")
first_digit = t + r + u + e

# Count LOVE
l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e_again = combined_names.count("e")
second_digit = l + o + v + e_again

love_score = int(str(first_digit) + str(second_digit))

# -------------------------------------------------------------
# NEW BULLETPROOF SYSTEM: No complex rules, just raw matchups.
# -------------------------------------------------------------

# 1. First, it prints the basic score line
print(f"\n✨ Calculation Complete! Your score is: {love_score}% ✨")

# 2. This forces Python to look at your score and pick a text message
message = "Hmm, the stars are undecided on this one. 🪙"

if love_score >= 70:
    message = "You go together like coke and mentos! 💥 Absolute explosive chemistry!"
elif love_score >= 40:
    message = "You guys have amazing chemistry! 🔥 High potential here."
elif love_score >= 15:
    message = "You are alright together. 👌 Pretty comfortable vibes."
else:
    message = "Oof... maybe just stick to being friends. 💀"

# 3. This forces Python to print the comment as a completely separate action
print(f"Match Analysis: {message}")
