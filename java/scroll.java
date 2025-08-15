import javax.swing.*;

public class scroll {
    public static void main(String[] args) {
        // Create JFrame instance
        JFrame f = new JFrame("Day Selector");
        f.setSize(400, 300);
        f.setLayout(null);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Days of the week
        String week[] = {
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
        };

        // Label for instructions
        JLabel n = new JLabel("Select the day:");
        n.setBounds(50, 50, 100, 20);

        // Create JList
        JList<String> l = new JList<>(week);
        l.setBounds(150, 50, 120, 100); // Increase height for better display

        // Add JScrollPane for the list
        JScrollPane scrollPane = new JScrollPane(l);
        scrollPane.setBounds(150, 50, 120, 100);

        // Set a default selection
        l.setSelectedIndex(1);

        // Add components to the frame
        f.add(n);
        f.add(scrollPane);

        // Make frame visible
        f.setVisible(true);
    }
}
