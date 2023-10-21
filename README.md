# Magic 8-Ball Project

A Python program that can answer any "Yes" or "No" question with a different fortune each time it executes. 

The following 15 possible answers were used for the Magic 8-Ball:
  - Yes, definitely.
  - It is decidedly so.
  - Without a doubt.
  - It is certain.
  - Signs point to yes.
  - Reply hazy, try again.
  - Better not tell you now.
  - Cannot predict now.
  - Ask again later.
  - Don't count on it.
  - My sources say no.
  - Very doubtful.
  - My reply is no.
  - Outlook not so good.
  - Lol no.

The program will randomly output a different answer each time it's run, utilising randomly generated values from 1 (inclusive) to 15 (inclusive). 

The program will first require an input in the following format:
>>> Enter your name: [Name]
>>> Ask Magic 8-Ball a question: [Question]

Once input, the program will generate an output:
>>> Magic 8-Ball's answer: [Answer]

If no name is input, but a question is still asked, an output will generate as normal. 
However, if a question is not asked, regardless if a name is provided, the output will print
>>> Error
