import constants
from game.casting.actor import Actor
from game.shared.point import Point

#changed snake.py into cycles.py 

class Cycles(Actor): #changed from Snake(Actor)
    """
    A vehicle players move on. #removed long and limbless reptile. 
    
    The responsibility of Cycle is to move itself. #Everywhere snake was referenced has been replaced by cycle

    Attributes:
        _points (int): The number of points the object is worth.
    """
    def __init__(self, x, y):
        super().__init__()
        self._segments = []
        self._x = x
        self._y = y
        self._prepare_body(self._x, self._y)

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_trail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(constants.GREEN)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self, x, y):

        if (super().get_color() == constants.YELLOW):
            x = int(20)
            y = int(constants.MAX_Y / 2)

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else constants.GREEN
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)
