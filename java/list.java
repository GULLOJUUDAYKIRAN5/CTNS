import javax.swing.*;
public  class list{
    public static void main(String[] args) {
        JFrame f=new JFrame();
        f.setSize(400,300);
        f.setLayout(null);
        
        String week[]={
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
        };
        JLabel n=new JLabel("select the day");
        n.setBounds(50, 50, 100, 20);
        JList<String> l=new JList(week);
        l.setBounds(150, 50, 120, 100);
        JScrollPane p=new JScrollPane(l);
        p.setBounds(150, 50, 120, 100);
        l.setSelectedIndex(2);
        f.add(n);
      //  f.add(l);
        f.add(p);
        f.setVisible(true);
    }
}