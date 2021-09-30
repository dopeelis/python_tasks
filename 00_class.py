class Character:
    kind = 'Human'

    def __init__(self, name):
        self._hp = 10
        self.name = name

    def get_hp(self):
        return self._hp if self._hp > 0 else 0

    def set_hp(self, hp):
        if hp > 0:
            self._hp = hp
        else:
            self._hp = 0

    @property
    def hp(self):
        return self.get_hp()

    @hp.setter
    def hp(self, val):
        self.set_hp(val)

    def run(self):
        print(f'{self.name} ({Character.kind}) Running')

    def shoot(self):
        print(f'{self.name} Shooting')

    def take(self):
        print(f'{self.name} Taking')

    @staticmethod
    def say_kind():
        print(f'Character kind: {Character.kind}')


class FlyingCharacter(Character):
    def run(self):
        print(f'{self.name} Running with jumping')

    def fly(self):
        print(f'{self.name} Flying')


class SwimmingCharacter(Character):
    def run(self):
        print(f'{self.name} Running on water')

    def swim(self):
        print(f'{self.name} Swimming')


bob = FlyingCharacter('Bob')
alice = SwimmingCharacter('Alice')
frank = Character('Frank')


def marathon(participants):
    for participant in participants:
        participant.run()


marathon([bob, alice, frank])

bob.fly()
bob.set_hp(100)
print(bob.get_hp())
bob.hp = 110
print(bob.hp)

bob.take()
alice.swim()
alice.run()
