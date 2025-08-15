import javax.swing.*;
 public class dad{
    public static void main(String[] args) {
        JFrame j=new JFrame();
        j.setSize(400,300);
        j.setLayout(null);

        JButton b=new JButton("click");
        b.setBounds(50, 50, 60, 20);
        j.add(b);
        
        JTextField t=new JTextField("NEWLLOOO");
        t.setBounds(50, 100, 80, 20);
        j.add(t);

        

        JPasswordField p=new JPasswordField("PASSWOED");
        p.setBounds(150, 150, 100, 20);
        j.add(p);
        
        JLabel L=new  JLabel("pass");
        L.setBounds(50, 150, 80, 20);
        j.add(L);
        j.setVisible(true);

    }
 }