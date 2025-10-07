package Thread;

public class Main {
    public static void main(String[] args) {
        Thread file1 = new Thread(new FileLoader("video.mp4 "));
        Thread file2 = new Thread(new FileLoader("music.mp3 "));
        Thread file3 = new Thread(new FileLoader("image.png "));
        Thread file4 = new Thread(new FileLoader("ph.mp4 "));


        file1.start();
        file2.start();
        file3.start();
        file4.start();




        /*
        new TimerTheard("Timer A").start();
        new TimerTheard("Timer B").start();*/
/*    new A().start();
    // A TheardA = new A();
    // ThreadA.start();
    new B().start();*/


    }
}