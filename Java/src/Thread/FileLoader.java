package Thread;

public class FileLoader implements Runnable{
    private final String fileName;
    FileLoader(String fileName){
        this.fileName = fileName;
    }
    public void run(){
        System.out.println("DOWNLOAD: " + fileName + "Start....");
        try {
            Thread.sleep((long)(Math.random() * 2000));
        }catch (Exception _){}
        System.out.println(fileName + "successfull complete");
    }
}
