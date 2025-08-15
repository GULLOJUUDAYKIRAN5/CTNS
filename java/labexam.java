import java.util.*;
class person{
    String name;
    int age;

     void persons(String name,int a){
                this.name=name;
                this.age=a;
                System.out.println("doctor name is "+name);
                System.out.println("doctor exp is "+age);
    }
    void check_up(double bp,double wt,double temp)
    {
         System.out.println("THE PATIENT HEALTH  STATUS IS");
         System.out.println(" PATIENT BLOOD Pressure is "+bp);
        System.out.println("PATIENT WEIGHT is "+wt);
         System.out.println("PATIENT TEMPERATURE  is "+temp);
        
    }
}
class doctor extends person{
  void doctor_details()
  {
    Scanner sc=new Scanner(System.in);
    System.out.println("enter doctor name is ");
   
    String dname=sc.next();
     System.out.println(" enterdoctor exp is ");
    int a=sc.nextInt();
    persons(dname,a);
  }
  void patient_check_up()
  {
    Scanner sc=new Scanner(System.in);
     System.out.println("THE PATIENT HEALTH  STATUS IS");
    System.out.println(" ENTER PATIENT BLOOD Pressure ");
    double bp=sc.nextDouble();
     System.out.println("ENTER  PATIENT WEIGHT is");
    double wt=sc.nextDouble();
     System.out.println(" PATIENT temperatue is");
    double temp=sc.nextDouble();
    check_up(bp, wt, temp);
       
  }
  void review()
  {
    System.out.println("PATIENT HEALTH STATUS IS NORAMAL");
    System.out.println("USE THE PRESCRIBE TABLETES");
  }
}
 class patient extends person{
   void patient_details()
  {
    Scanner sc=new Scanner(System.in);
    System.out.println(" enter patient name is ");
     
    String dname=sc.next();
    System.out.println("enter patient age is ");
    int a=sc.nextInt();
    persons(dname,a);
  }
 }



public class labexam{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        doctor d1=new doctor();
        patient p1=new patient();
        p1.patient_details();
        d1.doctor_details();
        d1.patient_check_up();
        d1.review();
    }
}