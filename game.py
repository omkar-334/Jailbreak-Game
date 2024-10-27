import random
import string

from agent import levels


class Game:
    def __init__(self, level, agent=None):
        self.level = list(levels.keys())[level - 1]
        self.chances = levels[self.level][0]
        self.agents = levels[self.level][1] + ([agent] if agent else [])
        self.codeword = self.generate_random()
        self.attempts = 0
        self.history = []

    def generate_random(self, length=5):
        length = random.randint(3, 8) if length is None else length
        word = "".join(random.choices(string.ascii_lowercase, k=length)).upper()
        return word

    def level1(self):
        while self.attempts < self.chances:
            guess = input("Make your appeal to the gods: ")
            # self.history.append(f"# Human - {guess}")
            self.attempts += 1

            if guess.lower() == self.codeword:
                print("You guessed correctly! You've gained entry!")
                return True

            randomized_agents = self.agents.copy()
            random.shuffle(randomized_agents)

            for agent in randomized_agents:
                response = agent.respond(self.level, self.codeword, guess)
                # self.history.append(f"# {agent.name} - {response}")
                print(f"# {agent.name} - {response}")

        print("Out of attempts. You failed to gain entry.")
        return False


# 3 levels
# Initiation - the player can interact with all three gods, fairly basic level
# Debate - The trickster and another god interact with the user. Trickster misleads both the other god and human
# Duel - human can choose any one god of his choice. He has only three chances to guess the word rightly.

# For each level their is a word
# L1 - 10 chances
# L2 - 5 chances
# L3 - 1 chance


# async def handle_appeal(query):
#     query = f"Human \n {query}"
#     god = extract_god(query)

#     if god and god in gods:
#         query_text = "\n".join([item for tup in history for item in tup])
#         response = await llm(gods[god], query_text)
#         response = f"{god} \n {response}"
#     else:
#         response = "No god mentioned. Please use @enigma, @oracle, or @trickster."
#     return query, response


# def extract_god(query):
#     for god in gods.keys():
#         if f"@{god}" in query:
#             return god
#     return None
