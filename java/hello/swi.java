import javax.swing.*;
public  class swi{
    public static void main(String[] args) {
        JFrame j=new JFrame();
        j.setSize(400,300);
        j.setLayout(null);
        JLabel L=new JLabel("login");
        L.setBounds(50, 50, 100, 20);

        JTextField t=new JTextField();
        t.setBounds(200, 50,60,20);

        JLabel L1=new JLabel("password");
        L1.setBounds(50, 100, 60, 20);
   
         JPasswordField P=new JPasswordField();
         P.setBounds(200, 100, 80, 20);

         JButton b=new JButton("submit");
         b.setBounds(150, 150, 100, 30);

         String[] x={
            "monday","hafakjfakfj","kjhfkahfiau","hjakjfjkafa"
         };
         JList r=new JList(x);
         r.setBounds(100, 200, 100, 500);
         JScrollPane sc=new JScrollPane(r);
         sc.setBounds(100, 200, 100, 50);
     JRadioButton rr=new JRadioButton("male");
     rr.setBounds(50, 25,100,30);
     j.add(rr);
         j.add(sc);
         j.add(t);
         j.add(L);
         j.add(L1);
         j.add(P);
         j.add(b);
         j.setVisible(true);
    }
}