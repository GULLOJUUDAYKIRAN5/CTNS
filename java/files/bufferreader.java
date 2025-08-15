import java.io.*;
public class bufferreader{
    public static void main(String[] args) throws IOException{
        BufferedWriter bw=new BufferedWriter(new FileWriter("hello.txt"));
        bw.write("\n hello,everyone");
         bw.write("\n this,is,uday");
          bw.write("\n this,message");
           bw.write("\n about,everyone");
           bw.close();
           BufferedReader bn=new BufferedReader(new FileReader("hello.txt"));
           String[] x=new String[6];
           int i=0;
           while((x[i]=bn.readLine())!=null)
           {
            System.out.println(x[i]);
            i++;
           }
        int c=0;
        String a="this";
        for(String a: x)
        {
            if(x[i].equals(a))
            {
                    c++;
            }
        }
        System.out.println(c);
    //    for(i=0;i<x.length;i++)
    //    {
    //      System.out.println(x[i]);
    //    }
 bn.close();
    }
}