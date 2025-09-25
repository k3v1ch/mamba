package test;

public class Man {
    private String name;
    private int age;

    public Man(String name, int age) { //Constructor
        this.name = name;
        this.age = age;
    }
    public void showinfo(){
        System.out.println(name + age);
    }
    public void  setAge(int age){
        if (age > 0){
    this.age = age;
        }else {
            System.out.println("Возраст должен быть больше 0");
        }
    }

    public int getAge() {
        return age;
    }
}