from bke import MLAgent, RandomAgent, train_and_plot, validate, plot_validation, is_winner, opponent, start, load, train, save
 
 
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
    def validate(self):
        self.learning = False
        validation_agent = RandomAgent()
        validation_result = validate(agent_x=self, agent_o=validation_agent, iterations=1000)
        plot_validation(validation_result)
    def train_and_plot(self, iterations, trainings, validations):
        random_agent = RandomAgent()
        train_and_plot(agent=self, validation_agent=random_agent, iterations=iterations, trainings=trainings, validations=validations)
        save(self, 'MyAgent')

my_agent = MyAgent(alpha=0.85, epsilon=0.05)
#my_agent = load('MyAgent')

my_agent.train_and_plot(100, 200, 2000)
