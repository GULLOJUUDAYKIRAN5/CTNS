import java.io.*;
public  class buffer
{
    public static void main(String[] args) throws  IOException{
        BufferedWriter bw=new BufferedWriter(new FileWriter("new.dat"));
    
        BufferedReader bn=new BufferedReader(new FileReader("new.dat"));
        String x;
        while((x=bn.readLine())!=null)
        {
        System.out.println(x);
        }
        bn.close();
    }
}