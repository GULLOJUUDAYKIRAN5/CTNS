import java.io.*;
public class bigg{
    public static void main(String[] args)throws IOException{
        FileOutputStream few=new FileOutputStream("old.dat");
        String s="this is old";
        few.write(s.getBytes());
        few.close();
        FileInputStream few1=new FileInputStream("old.dat");
       int b;
       while((b= few1.read())!=-1)
       {
       System.out.print((char)b);
       }


    }
}