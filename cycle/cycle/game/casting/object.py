import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point

#changed file name from food.py to object.py 

class Object(Actor): #changed from Food(Actor)
    """
    An object in the game to catch. #everywhere you saw food referenced in snake has been changed to object. 
    
    The responsibility of Object is to select a random position and points that it's worth.

    Attributes:
        _points (int): The number of points the object is worth.
    """
    def __init__(self):
        "Constructs a new Object."
        super().__init__()
        self._points = 0
        self.set_text("*") #changed the symbol from @ to *
        self.set_color(constants.RED)
        self.reset()
        
    def reset(self):
        """Selects a random position and points that the object is worth."""
        self._points = random.randint(1, 8)
        x = random.randint(1, constants.COLUMNS - 1)
        y = random.randint(1, constants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)
        
    # def get_points(self):
    #     """Gets the points the food is worth.
        
    #     Returns:
    #         points (int): The points the food is worth.
    #     """
    #     return self._points
