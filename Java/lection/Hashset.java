import java.util.HashSet;

public class Hashset {
    public static void main(String[] args) {
        HashSet<String> names = new HashSet<>();
        names.add ("Никита");
        names.add("tyzdyraviy");
        names.add("jopich");
        names.add("bezdar");
        names.add("CHUVAK");
        names.add("Negri");
        for (String name : names){
            System.out.println(name);
            // Отличная сортировка для уникальных значений
            // email id номер телефона номер товара
        }
    }
}