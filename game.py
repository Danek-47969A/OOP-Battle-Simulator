from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Iron Icosahedron"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Griko")
    goblin2 = Goblin("Scribble")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
    print("But no hero has answered the call... yet.")
    hero = Hero("The One Who Knocks")
    print(f"{hero.name} enters the arena with {hero.health} health.")

    hero_attack_damage = hero.attack()
    goblin.take_damage(hero_attack_damage)
    print(f"{hero.name} attacks {goblin.name} for {hero_attack_damage} damage, bringing the goblin to {goblin.health} health")

    if goblin.is_alive:
        goblin_attack_damage = goblin.attack()
        hero.take_damage(goblin_attack_damage)
        print(f"{goblin.name} attacks {hero.name} for {goblin_attack_damage} damage, bringing the hero to {hero.health} health")


if __name__ == "__main__":
    main()
