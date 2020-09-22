import re



def main(grammar):

	
	print("Hi! I'm an academic advisor. What is your name?")


	run = True

	while(run):

		userMessage = input("> ")
		



		

def switch(grammar, msg):

	temp = msg.split() # Split msg into list of words

	"""
	This loop will translate each pronoun. 'I' -> 'you'.

	I had trouble using re.sub() as it would continually change pronouns
	that were already changed. I had to resort to this.
	"""

	for i in range(len(temp)):
		if(temp[i] in grammar):
			temp[i] = grammar[temp[i]] 

	
	
	return ' '.join(temp)


if(__name__ == "__main__"):
	

	"""
	This is a dictionary that will hold the pronouns to switch during Eliza's response.
	"""

	grammar = {"you":"I",
				"me":"you",
				"I've":"you have",
				"I":"you",
				"I'll":"you will",
				"my":"your",
				"am":"are",
				"are":"am",
				"yours":"mine",
				"mine":"yours"
				}



	rules = 
	
	main(grammar)
	
