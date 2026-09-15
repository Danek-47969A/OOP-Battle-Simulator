from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Iron Icosahedron"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero.damage = hero.attack()
        enemy.take_damage(hero.is_alive)
        if enemy.is_alive():
            enemy.damage = enemy.attack()
            hero.take_damage(enemy.damage)

        if hero.is_alive():
            print(f"{enemy.name} attacks {hero.name} for {enemy.damage} damage, bringing the hero to {hero.health} health")

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
    hero = Hero("The One Who Battles")
    print(f"{hero.name} enters the arena with {hero.health} health.")

    battle(hero, goblin)
    



if __name__ == "__main__":
    main()
