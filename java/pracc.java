import javax.swing.*;

public class pracc{
    public static void main(String[] args) {
        JFrame j = new JFrame();
        
        // Create and position a button
        JButton b = new JButton("click");
        b.setBounds(180, 50, 70, 20);
        
        // Create and position a text field with appropriate height
        JTextField t = new JTextField("hello");
        t.setBounds(180, 100, 90, 20); // Increased width and height
        JPasswordField p=new JPasswordField("enter the password");
        p.setBounds(180,150,110,20);
        JRadioButton r=new JRadioButton("male");
        r.setBounds(180,200,130,20);
        // Add components to the frame
        j.add(b);
        j.add(t);
        j.add(p);
        j.add(r);
        // Set up the frame
        j.setSize(700, 700);
        j.setLayout(null);
        j.setVisible(true);
        //j.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Close the application when the window is closed
    }
}
