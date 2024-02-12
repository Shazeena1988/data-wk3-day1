from superhero import Superhero

superman = Superhero("Superman", "Clark Kent" , "Man of Steel", "Lex Luthor")
spiderman = Superhero ("Spiderman", "Peter Parker", "Spidey Senses", "The Green Goblin")
ironman = Superhero ("Iron Man", "Tony Stark", "Armour", "The Mandarin")
batman = Superhero ("Batman", "Bruce Wayne", "Strong", "The Joker")

print(f"I am {superman.name} my real name is {superman.identity} my superpower is I am the {superman.power} my arch enemy is {superman.enemy}")
print(f"I am {spiderman.name} my real name is {spiderman.identity} my superpower is I have {spiderman.power} my arch enemy is {spiderman.enemy}")
print(f"I am {ironman.name} my real name is {ironman.identity} my superpower is I have {ironman.power} my arch enemy is {ironman.enemy}")
print(f"I am {batman.name} my real name is {batman.identity} my superpower is I am {batman.power} my arch enemy is {batman.enemy}")