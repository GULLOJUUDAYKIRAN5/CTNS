import java.io.*;
public class file{
    public static void main(String[] args) throws IOException
    {
       FileWriter f1=new FileWriter("new.dat");
       f1.write("hello sru");
       f1.close();
       FileReader f2=new FileReader("new.dat");
       char ch[]=new char[25];
       f2.read(ch);
      // String x=new String(ch);
       System.out.println(ch);
       f2.close();
    }
}