from abc import ABC, abstractmethod
from asyncio import sleep
from random import randint

from typing_extensions import Type, override


class IFrog(ABC):
    attack_range: int
    health: int
    armor: int

    @abstractmethod
    async def take_damage(self, attack_range: int) -> bool:
        raise NotImplementedError


class Frog(IFrog):

    attack_range = 15
    health = 150
    armor = 5

    def __init__(self) -> None:
        self.attack_range = randint(self.attack_range // 2, self.attack_range)
        self.armor = randint(0, self.armor)

    async def take_damage(self, attack_range: int) -> bool:
        await sleep(randint(0, abs((self.health + self.armor) // 10 - attack_range)))
        if self.armor > 0 and self.armor - attack_range > 0:
            self.armor = self.armor - attack_range
        elif self.armor > 0 and self.armor - attack_range <= 0:
            self.armor = self.armor - attack_range
            self.health = self.health + self.armor if self.health - +self.armor > 0 else 0
            self.armor = 0
        else:
            self.health = self.health - attack_range if self.health - attack_range > 0 else 0
        if self.health == 0:
            return True
        return False


class AssassinFrog(Frog):
    @override
    def __init__(self) -> None:
        super().__init__()
        self.health = int(round(self.health * 1.25, 0))


class AdventurerFrog(Frog):
    @override
    def __init__(self) -> None:
        super().__init__()
        self.attack_range = int(round(self.attack_range * 1.5, 0))


class ArtisanFrog(Frog):
    @override
    def __init__(self) -> None:
        super().__init__()
        self.armor = int(round(self.armor * 2, 0))


FROGS_CLASSES: tuple[Type[IFrog], ...] = tuple([Frog, AssassinFrog, AdventurerFrog, ArtisanFrog])
