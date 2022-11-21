from game.scripting.handle_collisions_action import HandleCollisionsAction #added, ,not included in snake
import time

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, video_service):
        """Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service
        self._game_is_over = False #added, not included in snake
        
    def start_game(self, cast, script):
        """Starts the game using the given cast and script. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            if self._game_is_over ==  False:
                self._execute_actions("input", cast, script)
                self._execute_actions("update", cast, script)
                self._execute_actions("output", cast, script)
            else:
                time.sleep(3)
                self._video_service.close_window()
                
        self._video_service.close_window()

    def _execute_actions(self, group, cast, script):
        """Calls execute for each action in the given group.
        
        Args:
            group (string): The action group name.
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        actions = script.get_actions(group)    
        for action in actions:
            action.execute(cast, script, self._game_is_over)   #added section self._is_game_over

            if isinstance(action, HandleCollisionsAction): #added collision section, not included in snake
                self._game_is_over = action.get_is_game_over()
