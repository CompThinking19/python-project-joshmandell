question_prompts = [
  "Who has scored the most touchdowns in one season?\n(a) Peyton Manning\n(b) Tom Brady\n(c) Joe Montana\n(d) Patrick Mahomes\n\n",
  "What MLB team has never made it to a World Series?\n(a) Seattle Mariners\n(b) Texas Rangers\n(c) LA Angels\n(d) Miami Marlins\n\n",
  "How many NBA championships have the Philadelphia 76ers won?\n(a) 1\n(b) 2\n(c) 3\n(d) 4\n\n",
  "Who had the largest Empire in history?\n(a) Mongol Empire\n(b) Roman Empire\n(c) British Empire\n(d) Persian Empire\n\n",
  "1 president has served as president of the United States for two non-consecutive terms who is he?\n(a) Grover Cleveland\n(b) Theodore Roosevelt\n(c) John Adams\n(d) Dwight D. Eisenhower\n\n",
  "What is the smallest country in the world?\n(a) Vatican City\n(b) Portugal\n(c) Singapore\n(d) Kuwait\n\n",
  "Who has won the most Academy Awards for acting?\n(a) Katherine Hepburn\n(b) Meryl Streep\n(c) Daniel Day-Lewis\n(d) Marlon Brando\n\n",
  "Which film was Brad Pitt not in?\n(a) Fight Club\n(b) Money Ball\n(c) Ocean’s Eleven\n(d) Saving Private Ryan\n\n",
  "What was the first American film to feature a toilet flushing?\n(a) Psycho\n(b) Breakfast Club\n(c) The Godfather\n(d) Taxi Driver\n\n" ]

class Question:
  def__init__(self, prompt, answer):
    self.prompt = prompt
    self.answer = answer

questions = [
  Question(question_prompts[0], "a"),
  Question(question_prompts[1], "a"),
  Question(question_prompts[2], "c"),
  Question(question_prompts[3], "c"),
  Question(question_prompts[4], "a"),
  Question(question_prompts[5], "a"),
  Question(question_prompts[6], "a"),
  Question(question_prompts[7], "d"),
  Question(question_prompts[8], "a")]

  #print welcome statement
  #print first prompt
  #accept user input
  #check input type, raise error if not string
  #check answer is right
  #if correct add one to score
  #repeat
  #print final score
  #randomize the order of questions


  