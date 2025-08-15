class person{
     String name;
     int age;
    public person(String x,int a) {
        this.name=x;
        this.age=a;
    }
    void display()
    {
        System.out.println("name is "+name+" "+" "+age);
    }
    
}

public class array_obj{
    public static void main(String[] args) {
        person[] p=new person[10];
        p[0]=new person("uday",5);
        p[1]=new person("kiran",6);
        for(int i=0;i<p.length;i++)
        {
            p[i].display();
        }
    }
}