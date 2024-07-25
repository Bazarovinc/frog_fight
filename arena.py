from random import randint

from frog import IFrog


class Arena:
    def __init__(self, fighter_1: IFrog, fighter_2: IFrog, arena_number: int) -> None:
        self.arena_number = arena_number
        self.fighter_1 = fighter_1
        self.fighter_2 = fighter_2
        print(
            f"На арене "
            f"{self.arena_number} "
            f"бой состоится между {type(self.fighter_1).__name__} и "
            f"{type(self.fighter_2).__name__}"
        )

    async def fight(self) -> tuple[bool, bool]:
        queue: tuple[IFrog, ...]
        while True:
            turn = randint(0, 1)
            if turn:
                queue = tuple([self.fighter_1, self.fighter_2])
            else:
                queue = tuple([self.fighter_2, self.fighter_1])
            print(
                f"На арене {self.arena_number} "
                f"первой наносит {type(queue[0]).__name__} удар {type(queue[1]).__name__}"
            )
            if not (await queue[0].take_damage(queue[1].attack_range)):
                if await queue[1].take_damage(queue[0].attack_range):
                    break
            else:
                break
        print(
            f"На арене "
            f"{self.arena_number} "
            f"бой между {type(self.fighter_1).__name__} и {type(self.fighter_2).__name__} окончен"
        )
        return bool(self.fighter_1.health), bool(self.fighter_2.health)
