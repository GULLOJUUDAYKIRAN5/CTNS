import javax.swing.*;
public class login{
    public static void main(String[] args) {
        JFrame j=new JFrame();
        JLabel l=new JLabel("name");
        l.setBounds(10,50 , 40, 20);
        JTextArea t=new JTextArea();
        JLabel l1=new JLabel("pass");
        l1.setBounds(10, 100, 40,20);
        t.setBounds(180, 50, 70, 20);
        JPasswordField p=new JPasswordField();
        p.setBounds(180,100,90,20);
        JRadioButton r=new JRadioButton("submit");
        r.setBounds(180,150,110,20);
    l1.setText("this is me");
        j.add(l);
        j.add(t);
        j.add(p);
        j.add(r);
        j.add(l1);
        j.setSize(1000,1000);
        j.setLayout(null);
        j.setVisible(true);
        
    }
}