import java.io.*;
public  class ques1
{
    public static void main(String[] args) throws  IOException{
        BufferedReader bn=new BufferedReader(new FileReader("new.dat"));
        String x;
        int male=0,female=0;
        String arr[]=new String[25];
      while((x=bn.readLine())!=null)
        {
           arr=x.split(" ");
           for(String a:arr)
           {
            if(a.equals("male"))
            {
              male+=1;
            }
            else if(a.equals("female"))
              female+=1;
            }
           }
        }
        System.out.println("male is "+male);
        System.out.println("female is "+female);
        bn.close();
    }
