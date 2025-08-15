import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

public class add{
    public static void main(String[] args) {
        // Create a frame
        JFrame frame = new JFrame("Add Two Numbers");
        frame.setSize(400, 300);
        frame.setLayout(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Create labels
        JLabel label1 = new JLabel("Number 1:");
        label1.setBounds(50, 50, 100, 30);
        JLabel label2 = new JLabel("Number 2:");
        label2.setBounds(50, 100, 100, 30);
        JLabel resultLabel = new JLabel("Result:");
        resultLabel.setBounds(50, 200, 300, 30);

        // Create text fields for input
        JTextField num1Field = new JTextField();
        num1Field.setBounds(150, 50, 150, 30);
        JTextField num2Field = new JTextField();
        num2Field.setBounds(150, 100, 150, 30);

        // Create a button to perform addition
        JButton addButton = new JButton("Add");
        addButton.setBounds(150, 150, 80, 30);
        JButton sb = new JButton("sub");
        sb.setBounds(250, 150, 80, 30);
        frame.add(sb);
        // Add action listener to the button
        addButton.addActionListener(new ActionListener() {
            //@Override
            public void actionPerformed(ActionEvent e) {
                try {
                    // Get numbers from text fields
                    double num1 = Double.parseDouble(num1Field.getText());
                    double num2 = Double.parseDouble(num2Field.getText());

                    // Perform addition
                    double result = num1 + num2;

                    // Display the result
                    resultLabel.setText("Result: " + result);
                } catch (NumberFormatException ex) {
                    // Handle invalid input
                    resultLabel.setText("Please enter valid numbers.");
                }
            }
        });
        sb.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent b) {
                double num1 = Double.parseDouble(num1Field.getText());
                    double num2 = Double.parseDouble(num2Field.getText());

                    // Perform addition
                    double result = num1 - num2;
                resultLabel.setText("subbed : "+ result);
            }
        });

        // Add components to the frame
        frame.add(label1);
        frame.add(num1Field);
        frame.add(label2);
        frame.add(num2Field);
        frame.add(addButton);
        frame.add(resultLabel);

        // Make the frame visible
        frame.setVisible(true);
    }
}
