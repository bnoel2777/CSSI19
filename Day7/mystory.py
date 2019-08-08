story = """I'm a little {2}
{0} and {1}
Here is my {3} 
Here is my spout


When I get all steamed up
Hear me {4}
Tip me over
and pour me out! """

print story

adjective1 = raw_input("Enter an adjective:")
adjective2= raw_input("Enter an adjective2:")
noun1 = raw_input("Enter a noun:")
noun2 = raw_input("Enter a noun:")
noun3 = raw_input("Enter a noun:")

print story.format(adjective1,adjective2,noun1,noun2,noun3)

