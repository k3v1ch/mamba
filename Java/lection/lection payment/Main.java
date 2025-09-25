import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Выберете способ оплаты:");
        System.out.println("1 - кредитная крата");
        System.out.println("2 - PayPal");

        int choice = sc.nextInt();

        Payment payment;

        if (choice == 1){
        payment = new CreditCardPayment();
        } else {
            payment = new PayPalPayment();
        }
        System.out.println("Введите сумму: " );
        double amount = sc.nextDouble();
        payment.pay(amount);

        sc.close();
    }
}