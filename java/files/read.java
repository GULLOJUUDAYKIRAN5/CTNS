import java.io.*;
public class read{
    public static void main(String[] args) throws IOException {
        FileWriter f1=new FileWriter("hello.txt");
        f1.write("this is me");
        f1.close();
        FileReader f2=new FileReader("hello.txt");
        char[] ch=new char[25];
        f2.read(ch);
        System.out.println(ch);
        f2.close();
    }
}