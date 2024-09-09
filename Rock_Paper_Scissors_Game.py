import random

class Game:
    def random_choose(self):
        options = ["rock", "paper", "scissors"]
        return random.choice(options)

    def compare_choose(self, user_choice, pc_choice):
        if user_choice == pc_choice:
            return "There is no winner"
        elif (user_choice == "rock" and pc_choice == "scissors") or \
             (user_choice == "scissors" and pc_choice == "paper") or \
             (user_choice == "paper" and pc_choice == "rock"):
            return "User wins"
        else:
            return "Computer wins"

    def main(self):
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        pc_choice = self.random_choose()

        print(f"User's choice: {user_choice}")
        print(f"Computer's choice: {pc_choice}")
        print(self.compare_choose(user_choice, pc_choice))

if __name__ == "__main__":
    game = Game()
    game.main()
