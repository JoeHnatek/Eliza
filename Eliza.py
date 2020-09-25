"""
Written by: Joseph Hnatek
Date: Sept. 21, 2020

== OVERALL ==
The main function acts as the drive of the program.
This is where we take in the User's input and bassed on their message,
Eliza will output a response bassed on its set rules.

== EXAMPLE ==
Eliza: Hi! I'm Eliza, an academic advisor. What is your name?
> My name is Joe.
Eliza: Hi Joe!. What are you majoring in?
> I am majoring in Computer Science.
ELiza: Do you enjoy Computer Science?
...

== ALGORITHM ==
While the user does not say "goodbye",
Take in their input and remove anything to the right of the period in a sentence.
If the user inputs "goodbye", make run = false, now we can quit.
Iterate through the rules list and gather a pattern and its potential responses.
We try to then find a match between the pattern and the user's input.
If match, then choose a random reply from its respective pattern and output the reply as Eliza's response.
Continue until user says "goodby"
If the user said "goodbye", then terminate the program.
"""


import re
import random

def main(rules):

	print("Hi! I'm Eliza, an academic advisor. What is your name?")

	run = True

	while(run):
		
		# Take in user text
		# lower it, split to the right so we only have the first sentence.
		# [0] -> Indicates we access the first index in the list generated from the rstrip method.
		userMessage = input("> ").rsplit(".")[0]

		# User is quiting chatbot
		if(userMessage == 'goodbye'):
			run = False

		# Loop through the rules list to find a match.
		# If a match is found, get Eliza's response randomly from the list.
		for pattern, resp in rules:
			match = re.match(pattern, userMessage, re.IGNORECASE)

			# If there is a match from the rules, generate Eliza's response.
			if match:

				# Choose a 'random' response from the respective regex rule.
				reply = random.choice(resp)

				# *match.groups()
				# * -> Indicates to unpack the tuple into usuable values.
				# print out Eliza's response.
				print(reply.format(*match.groups()))
				
				# We want Eliza to respond only once.
				break


if(__name__ == "__main__"):

	"""
	This is a list that contains a regex with its corresponding possible responses.
	"""

	rules = [[r'\?',["Would that help you?", "Perhaps.", "Why are you asking me?"]],
			[r'(^[a-zA-Z]+ [0-9]{2,4}$)', ["Tell me more about {0}.", "Are you handling {0} well?", "Do you want to drop {0}?", "Do you want to add {0}?", "You should really look more into {0}, it sounds fun."]],
			[r'(\bI\b) (\blove\b|\bhate\b|\blike\b|\bneed(ed)?\b) (.*)',['Why do you {1} {3}?']],
			[r'\b(my)?\b \bname\b \b(is)?\b (.*)',["Hi {2}, what are you majoring in?"]],
			[r'(\bhello\b|\bhi\b|\bhey\b)',["Hello! How is your day?", "Hi! I am an academic advisor. How can I help?"]],
			[r'.* \bmajor(ing)?\b \bin\b (.*)',["Do you enjoy {1}?","Tell me more about {1}", "Do you have a minor?"]],
			[r'\bminor(ing)?\b \bin\b (.*)', ["Do you enjoy {1}?", "Tell me more about {1}.", "Would you consider majoring in {1} instead?"]],
			[r"(\bI\b|\bI'm\b) (am)? in (.*)", ["Do you enjoy {2}?", "How is {2} going?", "Why did you pick {2}?", "Can you tell me more about {2}?", "Why are you in {2}?"]],#2
			[r'\bhelp\b (\bwith\b)? (.*)',["What do you need help with?", "How could I help with that?", "Can't you do it yourself?", "Sure! How could I help."]],
			[r'\bclass(es)?\b',["What class do you need to take? (ABCD 1111)", "Is that a required class?", "Do you need that to graduate?", "Do you enjoy that class?"]],
			[r'\b(good)?bye\b',["Bye!","Thanks for talking!", "See ya! That'll be $10,000 per semester."]],
			[r'\bpassing\b', ["Great! What can I help with?", "Can you do better than just passing?"]],
			[r'(\bfall\b|\bspring\b|\bsummer\b)', ["{0} is pretty close. Will you be ready?", "Are you going to be ready for {0}", "Do you enjoy {0}?"]],
			[r'\byes\b',["Great! Anything else?", "Good! I'll make a note of that.", "Great! Anything else you want to talk about?"]],
			[r'\bno(pe)?\b', ["Why is that?", "Okay. I'll make a note of that. Anything else?"]],
			[r'\bgrade(s)?\b', ["How are your classes going?", "Is your GPA good?"]],
			[r'.* (\bterrible\b|\bhorrible\b)', ["Sorry to hear that it is {0}. How can I help?", "Why is it {0}", "How can I help it not be {0}?"]],
			[r'.* \bhomework\b (.*)', ["Have you been doing well with them?", "You say the homework {1}. How so?", "Are you doing them well?"]],
			[r'.* \bwell\b', ["What is making it go well?", "Can it get any better?", "What could go better for you?", "Well? Would you want them to be better?"]],
			[r'\b(.*)\b (\bsound(s)?\b) (.*)', ["Why does {0} sound {3}", "Would you take it if it only sounded {3}?", "{0} does sound {3}"]], # 0 1
			[r'\b(.*)\b (\bgraduate\b) (.*)?', ["When are you graduating?", "What do you need to graduate?", "You can take your time. Why do you want to {1} {2}?", "Are you close to graduating?", "Are you excited to graduate?", "Are you ready to graduate?"]],
			[r'(\bI\b)? (\bam\b)? \bstudy(ing)?\b (.*)', ["Do you enjoy {3}?", "How is {3} going?", "Is {3} required to graduate?"]],#3
			[r'\bI\b (\bwant\b|\bneed\b) to (\badd\b|\bremove\b) \ba class(es)?\b', ["Why do you {0} to {1} a class?", "Sure what class? [ABCD 1111]"]],
			[r'(\bGood\b|\bbad\b|\bokay\b)', ["Why is it {0}?", "{0}?", "Elaborate why it is {0}."]],
			[r'\bare\b \byou\b (.*)', ["Why do you ask if I am {0}?", "So what if I was {0}?"]],
			[r'\bnot really\b', ["That's okay. Would you consider doing research?", "Why not?", "Sure. You should really think about it."]],
			[r'\binteresting\b', ["Why is it interesting?", "Tell me more about why you think it is.", "Would you enjoy it more?", "Would that help in class?"]],
			[r'.* \bgrade(s)?\b',["Do you think it could be higher?", "Do you want to improve your grades?"]],
			[r'\bcan i ask\b', ["What do you want to ask?"]],
			[r'\bjob(s)?\b', ["I'm sure there are jobs out there for you! I can help you look for them.", "What are you looking for?"]],
			[r'\bsalary\b', ["How much?", "That sounds like a solid plan!"]],
			[r'\bthanks\b', ["You're welcome! Anything else?", "No problem!"]],
			[r'\bmilitary\b', ["Why the military?"]],
			[r'\bdont\b (.*)', ["Okay, I won't {0}", "Hmm. I'll take that into acount."]],
			[r'\bmaybe\b', ["You should commit more.", "Think about it more.", "Please consider it."]],
			[r'\bgrades are\b (\bbad\b|\bgood\b|\bgreat\b|\bokay\b)', ["Do you think you can improve it more?", "{0}? Is that what you expect?"]],
			[r'\bregister\b', ["What are you looking to register?"]],
			[r'\bI\b \bdo\b', ["Good! How are your grades?"]],
			[r'\bI\b \bwill\b', ["Great! How is life going?", "Thanks. Can I do anything else?"]],
			[r'.* \btuition\b', ["Tuition is important. It helps pay for this service.", "Tuition can be costly, how can I help?"]],
			[r"(\bI\b|\bI'm\b) \bnot\b \bsure\b", ["That's okay. You should though. What can I help with that?"]],
			[r'.* \bhold\b', ["Sure I can help with that, what's the hold for?"]],
			[r'.* \bowe money\b', ["First you need to pay it off. Do you need support?"]],
			[r'.* \bneed\b \bsuport\b', ["I can direct you to a few grants and scholarships. Do you want that?"]],
			[r'\brecommend\b', ["Try a few professors in your department!"]],
			[r'\bI\b \breally\b (\benjoy\b|\dislike\b) (.*)', ["Why do you really {0} {1}?"]],
			[r'\bfun\b', ["Thats great you find it fun! Have you thought of your future in it?"]],
			[r'\burop\b', ["UROP is a great way to do research! Do you want some info on that?"]],
			[r'\bdont understand\b', ["It can be difficult. Can I do anything else for you?"]],
			[r'\bits\b \bokay\b', ["Sure it is. What other help do you need?"]],
			[r'.* \bthat\b \bis\b (.*)', ["Why do you say it is {0}?", "{0}? Howcome?"]],
			[r'\bthey\b \bare\b (\bgood\b|\bbad\b)', ["That's {0} to hear.", "What else can I help with."]],
			[r"(\bI\b|\bI'm\b) (\bam\b)? \bhope?(ing)?\b (.*)", ["Why do you hope?", "Are you doing well?", "Can you do something instead?"]],
			[r"(.*)",["Can you elaborate on that?","Interesting. Tell me more.", "How come?", "I'm sorry, I'm not quite sure I understand. Can you explain.", "Have you thought about your future at all?"]]]


	# Start Eliza's conversation!

	main(rules)
