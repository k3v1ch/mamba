package main;
import test.Man;

public class Main {
    public static void main(String[] args) {
        Man man = new Man("Nikita", 18);
        man.age = - 10;
        man.showinfo();
    }
}