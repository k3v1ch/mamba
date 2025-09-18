import java.util.ArrayList;
public class import123 {
    public static void main(String[] args) {
        ArrayList <String> employes = new ArrayList<>();
        employes.add("Никита");
        employes.add("tyzdyraviy");
        employes.add("jopich");
        employes.add("bezdar");
        employes.add("CHUVAK");
        employes.add("Negri");
//    for (int i = 0 ; i<employes.size();i++){
//            System.out.println(employes.get(i));
//        }
        for (String name:employes){
            System.out.println(name);
        }
        ArrayList<Integer> numbers = new ArrayList<>();
        for(int i = 0; i <1001;i++){
            numbers.add(i);
        }
        for (int i :numbers){
            System.out.println(i);
        }
    }
}
