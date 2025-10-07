package Thread;

public class A extends Thread{
    public  void run(){
        for (int i = 0; i<1000; i++){
            System.out.println("A: " + i);
        }
    }
}
