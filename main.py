import pygame as pg

import modules

pg.init()

class Game:
    def __init__(self):
        self.display = pg.display.set_mode((800, 800))
        pg.display.set_caption("what was")

        self.running = True
        self.clock = pg.time.Clock()
        self.load_pg_assets()

        self.start = modules.Buttons((195, 500, 200, 100), pg.transform.scale(pg.image.load("assets/start_button.png").convert_alpha(), (200, 100)))
        self.exit = modules.Buttons((405, 500, 200, 100), pg.transform.scale(pg.image.load("assets/exit_button.png").convert_alpha(), (200, 100)))

        self.scene = 'main menu'

        pg.mixer_music.load("assets/titlemusic.mp3")
        pg.mixer_music.set_volume(1)
        pg.mixer_music.play()

    def load_pg_assets(self):
        self.font = pg.font.SysFont("Comic Sans", 50)
        self.title = pg.transform.scale(pg.image.load("assets/title.png").convert(), (800, 400))

        self.title_background = pg.transform.scale(pg.image.load("assets/background.png"), (800, 800)).convert()

    def run(self):
        while self.running:
            self.clock.tick(360) 

            if self.scene == 'main menu':
                self.display.blit(self.title_background)
                self.display.blit(self.title, (0, 0))

                self.start.render(self.display)
                self.exit.render(self.display)

                if self.start.update():
                    self.scene = "play"
                
                if self.exit.update():
                    self.running = False

            elif self.scene == "play":
                self.display.fill((255, 255, 255))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            pg.display.update()

if __name__ == "__main__":
    Game().run()

# this story is about a boy who develops psychological issues.
# slowly, he struggles to do basic things.
# his parents get him some pills
# but maybe they do something else.

# the first day:
# their mom tells them to get ready for school.
# there are minor anomalies in his house. such as strange sounds.

# the seconds day:
# you get a dream of hallucinations surrounding you.
# which then you promptly wake up to the fact that 
# their mom yells at him after he was late to school.

# the third day:
# mom notices changes in behavior, so they go to the hospital and get pills. she tells him to strictly use them only once per day.
# she explains that you have some psychological disorder. she leaves the room
# if you take more pills, hallucinations get worse.

# the fourth day:
# you wake up in the middle of the night. and you cant fall asleep.
# you must find the switch to turn the light on to prevent hallucinations to come after you.
# after the lights turn on, mom comes in sleepy, asking why he isnt sleeping at 3 am.
# you take the pills and then you fall asleep shortly.

# in the morning, you dont get ready to school. because of the rough night they had prior.
# mom asks whats been happening lately. she decides to leave the pills directly on the table.

# in the night of the same day you hear strange sounds at night. 
# if you take the pills, strange sounds will proceed to get worse.
# if you take more than one pill, then hallucinations will start making their way to you.
# if you dont take any pills, the sounds will finish shortly.

# the fifth day:
# mom tells you that you wont be going to school because shes afraid you are in a critical condition.
# your younger brother comes back from school and asks if he wants to play board games together.
# if you agree, then a minigame will start playing, of snakes and ladders.
# if you decline, then he walks away with tears in his eyes.

# at the end of the day
# if you didnt play with him:
# you wake up once again. to the sounds of his sobbing. 
# if you take your pills, then the sobbing goes away and you can peacefully go to bed.

# if you did play with him:
# then you get a dream of you getting sucked into the board game.
# the snakes here are real. right? you must not fall of into the abyss of the snakes and ladders universe.
# if you successfully manage to dodge all snakes, then your brother with a grin says "wake up"

# if you take the pills, then snakes will come to life and get you.
# otherwise, you must do nothing for 30 seconds.

# the sixth day:
# you wake up with mom beside you, she asks how the night went.

# if you say: "it was fine" then she walks away with relief then proceed to SCENE 1

# otherwise if you say: "i had a bad dream" then she asks why.

# if you say "i dont know" she walks away worried and proceed to SCENE 1.
# if you say "i think im going insane" she starts crying, and you get put in a hospital which then proceed to SCENE 2.

# SCENE 1:
# you get an invitation from your friends if they want to go out.

# if you agree, then your mom will drive you to the mall
# but you wont find anybody. people will start disappearing slowly.
# then suddenly copies of your brother will get you.

# if you decline, then nothing will happen.

# at night, you get a dream and hear a dialouge in a deep voice:
# "do you recognise this place?"
# "well if you dont, then just keep in mind that your soul is no longer in the realm of reality"
# "the world has paused for everyone else. actually, you are the only single candidate i chose to tell you this"
# "because you seem gullible. buts that fine, everyone is. you know what you want. but you wont actually go out of your way to escape reality"
# "and i dont blame you. nobody knows that is beyond this filthy world, and every single one of you guys seem miserable. but i want to let you know that i am probably not real either"
# "im just gonna a leave it on a good note: im personally a huge fan. why not you join me. lyanis, you smelly fuck!"

# END OF STORY

# SCENE 2:
# in the hostpital, you wake up in bed with soft relaxing music ringing your ears beside your mother.  
# the seventh day: you are slowly recovering from the trauma and you start seeing stuff they way they are and your friends message you asking how you are doing

# if you write "im doing good" then they reply with relief
# if you write "i had a rough week" they wish the best of luck
# if you write "idk man" then they reply with fear
# if you write "im gonna be back in a couple days" then they will hope for your recovery.

# at night, you hear a dialouge in a deep voice:
# "you seem to have won control of yourself"
# "you desire a life that you own"
# "but i want to ask you a question"
# "deep down. i want you to think about this"
# "in this dimension, this universe with me and you"
# "i want to let you know that we are not in the same page"
# *laughs* "you thought those were pills?"
# "these pills in particular only make me stronger."
# "do you even think youre even real?"
# "i tried to get you to..."
# "end it all."
# "but at last. you win, lyanis, you fat fuck!"

# END OF STORY