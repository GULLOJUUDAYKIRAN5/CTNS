class hello extends Thread{ 
    public void run(){
        try{
        for(int i=0;i<100;i++)
        {
            System.out.println(i);
            sleep(1000);
        }
        }
        catch(Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
}

public  class thr{
    public static void main(String[] args) {
        hello h1=new hello();
        Thread t1=new Thread(h1);
        t1.start();
        for(int i=0;i<100;i++)
        {
            System.out.println("ths i s me");
        }
    }
}