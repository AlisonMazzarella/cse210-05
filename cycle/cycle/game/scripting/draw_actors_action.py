from game.scripting.action import Action
import constants


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script, is_game_over):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        #everything changed from snake to cycle and then duplicated to represent two players, two cycles, and two scores
        score1 = cast.get_actors(constants.SCORE_GROUP)[0]
        score2 = cast.get_actors(constants.SCORE_GROUP)[1]
        object = cast.get_first_actor(constants.OBJECT_GROUP)

        cycles = cast.get_actors(constants.CYCLE_GROUP)
        cycle1 = cycles[0]
        cycle2 = cycles[1]
        if not is_game_over:
            cycle1.grow_trail(1)
            cycle2.grow_trail(1)
        cycle1_segments = cycle1.get_segments()
        cycle2_segments = cycle2.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actor(object)
        self._video_service.draw_actors(cycle1_segments)
        self._video_service.draw_actors(cycle2_segments)
        self._video_service.draw_actor(score1)
        self._video_service.draw_actor(score2)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()
