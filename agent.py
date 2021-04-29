from bke import MLAgent, RandomAgent, validate, plot_validation, is_winner, opponent, start, load, train, save
 
 
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
    def train(self, iterations):
        train(self, iterations)
        save(self, 'MyAgent')

 
my_agent = MyAgent()
my_agent = load('MyAgent')

my_agent.validate()
