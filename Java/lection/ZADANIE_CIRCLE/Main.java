import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
        System.out.println("Выбирете фигуру:");
        System.out.println("1 - круг");
        System.out.println("2 - прямоугольник");
        int choice = sc.nextInt();
        Shape shape;
        if (choice == 1){
            System.out.println("Введите радиус круга");
            double r = sc.nextDouble();
            shape = new Circle(r);
        } else {
            System.out.println("Введите ширину");
            double w = sc.nextDouble();
            System.out.println("Введите высоту");
            double h = sc.nextDouble();
        }
        System.out.println("Площадб выбранной фигуры:"+ shape.area() );
    }
}
