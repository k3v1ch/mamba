package Thread;

public class TimerTheard extends Thread {
    private final String name;

    TimerTheard(String name) {
        this.name = name;
    }

    @Override
    public void run() {
        try {


            for (int i = 0; i <= 1000; i++) {
                System.out.println(name + ": " + i + " sec");

                Thread.sleep(1000);
            }


        }catch (Exception _){}
    }
}
