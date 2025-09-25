public class CreditCardPayment implements Payment{
    @Override
    public void pay(double amount) {
        System.out.println("Оплата Кредитной Картой" +amount);
    }
}
