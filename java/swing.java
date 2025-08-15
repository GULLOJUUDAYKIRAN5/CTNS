import javax.swing.*;
public class swing{
    public static void main(String[] args) {
        JFrame j=new JFrame();
        JButton b=new JButton("click me");
        JTextField c=new JTextField();
        JPasswordField p=new JPasswordField();
        JRadioButton r=new JRadioButton("male");
        JRadioButton rr=new JRadioButton("female");
        c.setBounds(10,100,60,30);

         p.setBounds(10,180,60,30);
        // b.setBounds();
        
        // r.setBounds();
        // rr.setBounds();
        j.add(c);
        // j.add(b);
        
        // j.add(rr);
         j.add(p);
        // j.add(r);
        j.setSize(500,500);
        j.setVisible(true);
        j.setLayout(null);
    }
}