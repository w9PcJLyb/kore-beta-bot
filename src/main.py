# <--->
from .board import Board
from .logger import logger, init_logger
from .offence import capture_shipyards
from .defence import defend_shipyards
from .expantion import expand
from .mining import mine
from .control import spawn, greedy_spawn, adjacent_attack, direct_attack

# <--->


def agent(obs, conf):
    if obs["step"] == 0:
        init_logger(logger)

    board = Board(obs, conf)
    step = board.step
    my_id = obs["player"]
    remaining_time = obs["remainingOverageTime"]
    logger.info(f"<step_{step + 1}>, remaining_time={remaining_time:.1f}")

    try:
        a = board.get_player(my_id)
    except KeyError:
        return {}

    if not a.opponents:
        return {}

    defend_shipyards(a)
    capture_shipyards(a)
    adjacent_attack(a)
    direct_attack(a)
    expand(a)
    greedy_spawn(a)
    mine(a)
    spawn(a)

    return a.actions()
