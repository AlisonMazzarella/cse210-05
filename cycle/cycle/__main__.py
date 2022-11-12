import constants

from game.casting.cast import Cast
from game.casting.object import Object 
from game.casting.score import Score
from game.casting.cycles import Cycles
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    #create the cast

    # Create two players, get their position and color
    cycle = (Point(int(constants.MAX_X - 645), int(constants.MAX_Y / 2)))
    cycle1 = (Point(int(constants.MAX_X - 300), int(constants.MAX_Y / 2)))
    cycle.set_color(constants.GREEN)
    cycle1.set_color(constants.RED)


    # player 1 
    cast = Cast()
    score1 = Score()
    score1.add_points(5)
    cast.add_actor("cycle", cycle)
    cast.add_actor("score1", score1)
    score1.set_position(Point(constants.MAX_X+150, 10))

    # player 2 
    score2 = Score()
    score2.add_points(5)
    cast.add_actor("cycle1", cycle1)
    cast.add_actor("score2", score2)
    score2.set_position(Point(constants.MAX_X-200, 10))
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()