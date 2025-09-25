import java.lang.reflect.Array;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog();
        Cat cat = new Cat();
        Fish fish = new Fish();
        Bird bird = new Bird();
        //Теперь заставим наших животных есть
        ArrayList<Animal> animals = new ArrayList<>();

        animals.add(dog);
        animals.add(fish);
        animals.add(cat);
        animals.add(bird);
        for (Animal animal : animals){
            animal.eat();
        }// Это интерфейс
        Dog dog1 = new Dog();
        dog1.sound();
        Animal animal = dog1; //привел к родительскому классу
        dog1.eat();
        dog1.run();
    }
}