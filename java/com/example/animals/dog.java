import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;
public  class dog{
    public static void main(String[] args) {
        JFrame f=new JFrame();
        f.setSize(400,300);
        f.setLayout(null);

        JTextField f1=new JTextField();
        f1.setBounds(50, 50, 60,20);

        JTextField f2=new JTextField();
        f2.setBounds(50, 100, 80, 20);

        JLabel result=new JLabel("result");
        result.setBounds(50, 150, 100, 30);

        JButton b=new JButton("ADD");
        b.setBounds(100, 200, 120, 30);

        JButton s=new JButton("SUB");
        s.setBounds(300, 200, 120, 30); 

        b.addActionListener(new ActionListener()
        {
           public void actionPerformed(ActionEvent e)
           {
            double b=Double.parseDouble(f1.getText());
             double d=Double.parseDouble(f2.getText());
             double res=b+d;
              result.setText("result :"+ res);

           }
});

s.addActionListener(new ActionListener(){
    public void actionPerformed(ActionEvent f)
    {
        double c=Double.parseDouble(f1.getText());
        double d1=Double.parseDouble(f2.getText());
        double rees=c/d1;
        result.setText("result :"+rees);
    }

    
    });

f.add(f1);
f.add(f2);
f.add(b);
f.add(result);
f.add(s);
f.setVisible(true);

    }
}