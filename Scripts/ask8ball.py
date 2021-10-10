#magic8ball

import random

def _8ball(question):

        responses = [
        'It is certain.', 'It is decidedly so.', 'Without a doubt.',
        'Yes - definitely.', 'You may rely on it.', 'As I see it, yes.',
        'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.',
        'Reply hazy, try again.', 'Ask again later.',
        'Better not tell you now.', 'Cannot predict now.',
        'Concentrate and ask again.', "Don't count on it.", 'My reply is no.',
        'My sources say no.', 'Outlook not so good.', 'Very doubtful.'
        ]


        print(f'Question: {question}\nAnswer: {random.choice(responses)}')

ques= input("Enter the question you want to ask the magic 8ball: ")
_8ball(ques)
