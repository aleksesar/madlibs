# words game
title = print("Mad libs words game")
color = input("Please write a color: ")
adjective = input("Please write an adjective: ")
verb = input("Please write a verb: ")
name = input("Please write a name: ")
mad_libs = f"""
         Roses are { color }.
         Your are most {adjective} I have ever seen.
         I {verb} {name}!
         """
print(mad_libs)