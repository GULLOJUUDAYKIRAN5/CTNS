import javax.swing.*;
public class gui{
    public static void main(String[] args) {
        JFrame j=new JFrame();
        JButton b=new JButton("click");
        b.setBounds(50,50,70,30);
        JTextField t=new JTextField("hello");
        t.setBounds(50,100,100,30);
        j.add(b);
        j.add(t);
        j.setSize(1000,1000);
        j.setVisible(true);
        j.setLayout(null);
    }
}