class threds extends Thread
{
    public void run()
    {
        try{
        for(int i=0;i<50;i++)
        {
        System.out.println("this is dupi");
        sleep(1000);
        }
        }
        catch(Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
}
public class Main{
    public static void main(String[] args) {
        threds t1=new threds();
        Thread t2=new Thread(t1);
        t2.start();
       /* for(int i=0;i<50;i++)
        {
           System.out.println("this is main"); 
        }
        */
    }
}