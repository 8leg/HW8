import keyboard
import os
import time
import animal_data
import random


class ZooWorker:
    def __init__(self):
        self.name='John Animalworker'
        self.occupation='Zookeeper'
        self.finances='Broke'
        self.mood='Also broke'
        self.age='19'


class Animals:
    species='None'
    animal_list = []
    hunger_chance=30
    mood_change=(5,5)
    girth_chance=40
    def __init__(self, hunger=0, mood=5, girth=0, animal_name='John Beast'):
        self.animal_list.append(self)
        self.hunger=hunger
        self.mood=mood
        self.girth=girth
        self.animal_name=animal_name

    def stat_changes(self):
        if self.hunger==10:
            print(f'''Oh god, oh no, {self.animal_name} is DEAD!
It died peacefully in his sleep, but anyways you are fired.

(press enter to exit)''')
            input()
            exit(0)
        elif self.mood==0 and self.girth==10:
            print(f'''God damn it. {self.animal_name} ran away!
There are reports of {self.species} sightings, so its probably still alive, but anyways you are fired

(press enter to exit)''')
            input()
            exit(0)
        chance=random.randint(1, 100)
        if self.hunger>self.mood_change[0] or self.girth>self.mood_change[1]:
            if random.randint(0,100)<50 and self.mood>0:
                self.mood-=1
                print(f"{self.animal_name}'s mood worsened")
        else:
            if random.randint(0,100)<50 and self.mood<10:
                self.mood+=1
                print(f"{self.animal_name}'s mood improved")
        if chance<=self.hunger_chance and self.hunger<10:
            self.hunger+=1
            print(f'Whoops, {self.animal_name} got hungrier')
        elif random.randint(0,100)<=self.girth_chance and self.girth<10:
            self.girth+=1
            print(f'Whoops, {self.animal_name} made a mess')


    def stat_show(self)->dict:
        return {'animal_name':self.animal_name, 'hunger':self.hunger,'mood':self.mood, 'girth':self.girth}


class Elephant(Animals):
    species='elephant'
    hunger_chance = 30
    mood_change = (7, 8)
    girth_chance = 40
    pics=animal_data.Animal_Pics.elephant_pics
    def __init__(self, hunger=0, mood=5, girth=0, animal_name='Bogdan'):
        super().__init__(hunger, mood, girth, animal_name)
        self.sex='male'
    def one_cycle(self):
        self.stat_changes()
        event=random.randint(1,100)
        if event<=5:
            victim=[x for x in Animals.animal_list if x!=self and x.hunger<10]
            if victim:
                victim=random.choice(victim)
                victim.hunger+=1
                print(f"{self.animal_name} stole food from {victim.animal_name} using his long trunk!")
            # this part of code uses list comprehension to get a list of animals that are not dying from
            # hunger and steals food from them. That pesky elephant!!!
        elif event<=40 and self.girth>1:
            self.girth-=2
            print(f"{self.animal_name} cleaned his cage up. Good boy.")
    def clean(self):
        if self.girth>3:
            self.girth-=3
        else:
            self.girth=0
        print(f"You clean up an elephant's cage. He doesn't seem to care but you know he appreciates it")
    def feed(self):
        if self.hunger>3:
            self.hunger-=3
        else:
            self.hunger=0
        if random.randint(0,1)==0:
            self.mood+=1
            print(f"{self.animal_name} enjoyed his dish")
        else:
            self.mood-=1
            print(f"{self.animal_name} didn't like his dish")


class Wolf(Animals):
    species='wolf'
    hunger_chance = 45
    mood_change = (5, 4)
    girth_chance = 15
    pics=animal_data.Animal_Pics.wolf_pics
    def __init__(self, hunger=0, mood=5, girth=0, animal_name='Maria'):
        super().__init__(hunger, mood, girth, animal_name)
        self.sex='female'
    def one_cycle(self):
        self.stat_changes()
        event=random.randint(1,100)
        if self.mood<5:
            m_temp=6-self.mood
        else:
            m_temp=0
        if self.hunger>5:
            h_temp=self.hunger-5
        else:
            h_temp=0
        if event<=m_temp+h_temp:
            print(f'''Oh no, no, no, no, no, no, no, things are bad!!!
Whether due to bad mood or a hunger, {self.animal_name} has killed and ate one of our visitors.
Now court judge will decide your guilt, but you are definitely fired.

(press enter to exit)''')
            input()
            exit(0)
        elif event<=20 and self.hunger>6:
            self.hunger-=1
            if self.mood<10:
                self.mood+=1
            print(f'Somehow, somewhere, {self.animal_name} found some meat and ate it. It seems satisfied. Good for you')
        elif 20<event<=30 and self.girth>0 and self.mood>7:
            self.girth-=1
            print(f'{self.animal_name} seems to be in the mood today and cleans after itself')
    def clean(self):
        if self.girth>3:
            self.girth-=3
        else:
            self.girth=0
        print(f"You clean {self.animal_name}'s cage. She greets you with unfriendly stare")
    def feed(self):
        if self.hunger>6:
            self.hunger-=3
            print(f"Ow! {self.animal_name} almost bit your hand of while you were feeding her")
        elif self.hunger>3:
            self.hunger-=3
            print(f"Wolf simply munches on your meet in apathy")
        else:
            self.hunger=0
            print(f"{self.animal_name} reluctantly feasts on her meat. Bon appetit")
    def play(self):
        self.mood+=1
        event=random.randint(1,5)
        if event==1:
            self.mood+=1
            print(f'You had a great time playing with {self.animal_name}. Just when you think you are getting along she'
                  f' pisses on your shoes')
        elif event==4:
            self.hunger-=1
            print(f'While playing {self.animal_name} found some poor rabbit somewhere and completely forgot about you')
        else:
            print(f'That was a great session of playing ball, you both had fun')


class Parrot(Animals):
    species='parrot'
    hunger_chance = 20
    mood_change = (3, 3)
    girth_chance = 25
    pics=animal_data.Animal_Pics.parrot_pics
    bad_words=['a dumb','a moron','an idiot','a stupid','a shithead','an imbecile','a loser','his bitch','a pussy',
               'a dimwit','a hoe','a son of a bitch','a garbage', 'a dork']
    def __init__(self, hunger=0, mood=5, girth=0, animal_name='Danielo Del Sancho'):
        super().__init__(hunger, mood, girth, animal_name)
        self.sex='male'
        self.stance=['None', 0]
    def one_cycle(self):
        if random.randint(1, 10)==1:
            print(f"Parrot calls you {self.bad_words}. Normal day")
        if random.randint(1,2)==1:
            if self.stance[0]=='None' or self.stance[1]<1:
                victim = random.choice([x for x in Animals.animal_list if x != self and x.mood<10])
                if self.mood == 6 or not victim:
                    print(f'Great and powerful {self.animal_name} is lost in contemplation those days...')
                elif self.mood>6:
                    victim.mood+=1
                    print(f'{self.animal_name} had a pleasant, one sided conversation with {victim.animal_name}')
                elif self.mood<6:
                    print(f"{self.animal_name} called {victim.animal_name} {random.choice(self.bad_words)}."
                          f" {victim.animal_name} didn't understand a word but was offended")
                    victim.mood-=1
            elif self.stance[0]=='me':
                if self.mood<6:
                    self.mood+=1
                    print(f'{self.animal_name} found a new purpose in life while conversing to himself')
                elif self.mood>5:
                    self.mood-=1
                    print(f'{self.animal_name} sinks deeper into depression, struggling to find sense in day to day routine')
            else:
                if self.mood == 6:
                    print(f'Great and powerful {self.animal_name} is lost in contemplation those days...')
                elif self.mood > 6 and self.stance[0].mood<10:
                    self.stance[0].mood+=1
                    print(f'{self.animal_name} had a pleasant, one sided conversation with {self.stance[0].animal_name}')
                elif self.mood < 6 and self.stance[0].mood>0:
                    print(f"{self.animal_name} called {self.stance[0].animal_name} {random.choice(self.bad_words)}."
                          f"{self.stance[0].animal_name} didn't understand a word but was offended")
                    self.stance[0].mood -= 1
            self.stance[1]-=1
        self.stat_changes()
        event=random.randint(1,100)
        if event<=5:
            self.girth+=1
            print('That dumb bird shat too much in the enclosure')
        elif event<=30 and self.girth>5:
            self.mood-=1
            print(f'{self.animal_name} fails to observe a beauty in his dirty enclosure')
        elif 30<event<=40:
            self.hunger-=1
            print(f'{self.animal_name} hunted a mouse! Great success for a great bird')
    def clean(self):
        if self.girth>3:
            self.girth-=3
        else:
            self.girth=0
        if random.randint(1,5)==1:
            self.mood+=1
            print(f'You have a smalltalk with a parrot and he seems to enjoy cleaning')
        else:
            print(f'You clean {self.animal_name} cage while he talks to himself')
    def feed(self):
        if random.randint(1,10)==1:
            print(f'{self.animal_name} seems to depressed today and so he only eats a bit')
            self.hunger-=1
        else:
            print(f'{self.animal_name} eats without enthusiasm')
            self.hunger-=3
        if self.hunger<0:
            self.hunger=0
    def talk(self, target):
        self.stance=(target,3)
        if target==self:
            print(f'You council {self.animal_name}, he seems more inclined to think positively')
        else:
            print(f'You spoke with {self.animal_name} about {target.animal_name}. What will come out of this?')


# function I shamelessly stole from stackoverflow. Clears the console. Thanks popcnt
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    time.sleep(1)
    print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Hello. We have reviewed your application 
and are happy to welcome you in our Zoo
as the new zookeeper. Please take good care
of our vast collection of animals. Work 
starts tomorrow. We at the Zoo are like a
family so there is no reason to ever leave
your workplace. Enjoy your new occupation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It was a letter you received after applying for the new job. You have cybersecurity 
bachelor's degree but nobody wanted to take you in, so you had to sign up for the Zoo.
Tomorrow's the day everything changes.

(press enter to begin)
''')
    keyboard.wait('Enter')
    cls()