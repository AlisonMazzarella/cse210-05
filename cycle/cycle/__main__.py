import constants

from game.casting.cast import Cast
# changed from game.casting.food import food
from game.casting.object import Object
from game.casting.score import Score
# changed from game.casting.snake import snake
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
    # create the cast

    # Create two players, get their position and color
    # Added code to create another player, get their position, and manipulate their cycle colors, all this is not included in snake
    cycle1 = Cycles(int(constants.MAX_X - 645), int(constants.MAX_Y / 2))
    cycle2 = Cycles(int(constants.MAX_X - 300), int(constants.MAX_Y / 2))

    cycle1.set_color(constants.GREEN)
    cycle2.set_color(constants.RED)
    object = Object()

    # I think the problem with the score might be here, because it already adds 5 points.
    # player 1
    cast = Cast()
    score1 = Score() # Added this, not in snake
    # changed from foods to cycle
    cast.add_actor(constants.CYCLE_GROUP, cycle1)
    # changed from scores to score1
    cast.add_actor(constants.SCORE_GROUP, score1)
    score1.set_position(Point(constants.MAX_X+150, 10))  # added location points

    # added all of this for second cycle, not included in snake
    # player 2
    score2 = Score()
    cast.add_actor(constants.CYCLE_GROUP, cycle2)
    cast.add_actor(constants.SCORE_GROUP, score2)
    score2.set_position(Point(constants.MAX_X-200, 10))

    cast.add_actor(constants.OBJECT_GROUP, Object())

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
