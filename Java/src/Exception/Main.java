package Exception;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        try {
            System.out.println("Введите первое число для деления");
            double a = sc.nextDouble();
            System.out.println("Введите второе число для деления");
            double b = sc.nextDouble();
            double c = a / b;
            System.out.println(c);
        } catch (ArithmeticException e){
            System.out.println("Ошибка нах");
        }catch (Exception e1){
            System.out.println("Неверный формат");
        }


    }
}