import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycle collides
    with the object, or the cycle collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False 
        self._winning_player = 0

    def execute(self, cast, script, is_game_over):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        self._handle_segment_collision(cast) #P: changed this from outside the if statment
        self._handle_game_over(cast)


    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycles collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        #changed snake to cycles and separated cycle and cycles for two different players 
        
        cycles = cast.get_actors(constants.CYCLE_GROUP)
        cycle1 = cycles[0]
        head = cycle1.get_segments()[0]
        segments = cycle1.get_segments()[1:]

        cycle2 = cycles[1]
        head2 = cycle2.get_segments()[0]
        segments2 = cycle2.get_segments()[1:]
        

        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._winning_player = 1
                self._is_game_over = True
        for segment in segments2:
            if head.get_position().equals(segment.get_position()):
                self._winning_player = 1
                self._is_game_over = True
        #duplicated from first to represent second cycle
        for segment in segments2:
            if head2.get_position().equals(segment.get_position()):
                self._winning_player = 0
                self._is_game_over = True
        for segment in segments:
            if head2.get_position().equals(segment.get_position()):
                self._winning_player = 0
                self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycle trail and object white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        scores = cast.get_actors(constants.SCORE_GROUP)

        if self._is_game_over:
            #added information for second player, everything here was not included in snake
            cycles = cast.get_actors(constants.CYCLE_GROUP)
            cycle1 = cycles[0]
            segments = cycle1.get_segments()
            object = cast.get_first_actor(constants.OBJECT_GROUP)

            cycle2 = cycles[1]
            segments2 = cycle2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            scores[self._winning_player].add_points(5)
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)
            for segment in segments2:
                segment.set_color(constants.WHITE)
            object.set_color(constants.WHITE)
    
    def get_is_game_over(self):
        return self._is_game_over
