import asyncio
from random import choice

from arena import Arena
from frog import FROGS_CLASSES


async def main() -> None:
    fight_tasks = []
    for i in range(100):
        fighter_1, fighter_2 = choice(FROGS_CLASSES), choice(FROGS_CLASSES)
        fight_tasks.append(Arena(fighter_1(), fighter_2(), i).fight())
    fighter_1_wins, fighter_2_wins = 0, 0
    for win_1, win_2 in await asyncio.gather(*fight_tasks):
        fighter_1_wins += int(win_1)
        fighter_2_wins += int(win_2)
    print(f"В 100 боях побед у 1 лягушки: {fighter_1_wins}, у второй: {fighter_2_wins}")


if __name__ == "__main__":
    asyncio.run(main())
