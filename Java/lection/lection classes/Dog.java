public class Dog extends Animal implements CanRun {
    @Override
    public void eat() {
        System.out.println("Meat");
    }
    public void sound(){
        System.out.println("gav gav");
    }

    @Override
    public void Run() {
        System.out.println("Бежит");
    }

    public void run(){
        System.out.println("beghizt");
    }
}
