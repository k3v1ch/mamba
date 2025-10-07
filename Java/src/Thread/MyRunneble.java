package Thread;

public class MyRunneble implements Runnable{
    @Override
    public void run(){
        for (int i = 0; i<5;i++){
            System.out.println("Поток Runnble:" + i);
        }

    }
}
