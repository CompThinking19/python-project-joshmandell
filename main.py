# -*- coding: utf-8 -*-
print "Welcome to my trivia game. The game features 3 questions for each of the following topics: History, Sports, and Movies"

#below is the questions and answer choices
question_prompts = ["Who has scored the most touchdowns in one season?\n(a) Peyton Manning\n(b) Tom Brady\n(c) Joe Montana\n(d) Patrick Mahomes\n", "What MLB team has never made it to a World Series?\n(a) LA Angels\n(b) Texas Rangers\n(c) Seattle Mariners\n(d) Miami Marlins\n", "How many NBA championships have the Philadelphia 76ers won?\n(a) 1\n(b) 2\n(c) 3\n(d) 4\n", "Who had the largest Empire in history?\n(a) Mongol Empire\n(b) British Empire\n(c) Roman Empire\n(d) Persian Empire\n", "One president has served as president of the United States for two nonconsecutive terms who is he?\n(a) Dwight D. Eisenhower\n(b) Theodore Roosevelt\n(c) John Adams\n(d) Grover Cleveland\n", "What is the smallest country in the world?\n(a) Portugal\n(b) Vatican City\n(c) Singapore\n(d) Kuwait\n", "Who has won the most Academy Awards for acting?\n(a) Katherine Hepburn\n(b) Meryl Streep\n(c) Daniel Day-Lewis\n(d) Marlon Brando\n", "Which film was Brad Pitt not in?\n(a) Fight Club\n(b) Money Ball\n(c) Ocean’s Eleven\n(d) Saving Private Ryan\n", "What was the first American film to feature a toilet flushing?\n(a) Psycho\n(b) Breakfast Club\n(c) The Godfather\n(d) Taxi Driver\n"]

#this class below helps sort through the question prompts and the correct answer choices
class Question:
  def __init__(self, prompt, answer):
    self.prompt = prompt
    self.answer = answer

questions = [
  Question(question_prompts[0], "a"),
  Question(question_prompts[1], "c"),
  Question(question_prompts[2], "c"),
  Question(question_prompts[3], "b"),
  Question(question_prompts[4], "a"),
  Question(question_prompts[5], "d"),
  Question(question_prompts[6], "b"),
  Question(question_prompts[7], "d"),
  Question(question_prompts[8], "a")]

#this function is how the game runs, takes user input and gives the user a score
def run_trivia(questions):
    score = 0
    for question in questions:
        answer = raw_input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You answered " + str(score) + "/" + str(len(questions)) + " correct")

run_trivia(questions)

  #print welcome statement/
  #print first prompt/
  #accept user input/
  #check input type, raise error if not string
  #check answer is right
  #if correct add one to score/
  #repeat
  #print final score/
  #randomize the order of questions
