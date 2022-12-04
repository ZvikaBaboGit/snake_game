from game_parameters import get_random_apple_data



class Apple:
    """
    This class represented a object called apple which used for the snake game.
    self.color: the color of the apple which is always green.
    self.score: the score which the snake get when he eat the apple.
    self.location: the location of the apple on the board game(according to x and y).
    """
    def __init__(self):
        self.__apple = get_random_apple_data()
        self.__location = [self.__apple[0],self.__apple[1]]
        self.__score = self.__apple[2]
        self.__color = "green"
    def get_color(self):
        return self.__color
    def get_location(self):
        return self.__location
    def get_score(self):
        return self.__score
    def create_new_apple(self):
        self.__apple = get_random_apple_data()

