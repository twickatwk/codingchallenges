
import collections

class Animal:
    def __init__(self, timestamp, animalType, name):
        self.timestamp = timestamp
        self.animalType = animalType
        self.name = name

class AnimalShelter:

    def __init__(self):
        self.dogs = collections.deque([])
        self.cats = collections.deque([])

    def dequeueAny(self):
        if len(self.dogs) == 0:
            return self.cats.popleft()
        if len(self.cats) == 0:
            return self.dogs.popleft()

        cat = self.cats.popleft()
        dog = self.dogs.popleft()
        if cat.timestamp < dog.timestamp:
            self.dogs.appendleft(dog)
            return cat
        else:
            self.cats.appendleft(cat)
            return dog
        
    def enqueue(self, timestamp, animalType, name):
        if animalType == 'dog':
            self.dogs.append(Animal(timestamp, animalType, name))
        else:
            self.cats.append(Animal(timestamp, animalType, name))
    
    def dequeueDog(self):
        if len(self.dogs) == 0:
            return None
        return self.dogs.popleft()
    
    def dequeueCat(self):
        if len(self.cats) == 0:
            return None
        return self.cats.popleft()

    def display(self):
        print("List of Cats")
        a = list(self.cats)
        for cat in a:
            print(cat.name)
        
        b = list(self.dogs)
        print("List of Dogs")
        for dog in b:
            print(dog.name)
    
animalShelter = AnimalShelter()

animalShelter.enqueue(2, "cat", "sally")
animalShelter.enqueue(1, "dog", "mark")
animalShelter.enqueue(3, "dog", "john")

animalShelter.display()
animal = animalShelter.dequeueAny()
print()
print("Animal Dequeued: " + str(animal.name))
print()
animalShelter.display()




    