import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
public class GUI extends JFrame implements ActionListener {

    JPanel panelLabelFile, panelFile, panelLabelLength, panelLength, panelVisualisation, panelLabelVisualisation;
    JLabel labelFile, labelLength, labelVisualisation;
    JTextField textFieldFile, textFieldLength;
    JButton buttonFile, buttonLength;

    public static void main(String[] args) {
        // Making a new frame with new title en size
        GUI frame = new GUI();
        frame.setSize(500, 425);
        frame.setTitle("ORF Finder");
        frame.createGUI();
        frame.setVisible(true);
    }

    public void createGUI() {
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        // Append a window to the GUI
        Container window = getContentPane();
        window.setLayout(new FlowLayout());

        // Append 6 panels to the window
        panelLabelFile = new JPanel();
        panelLabelFile.setPreferredSize(new Dimension(100000,30));
        panelLabelFile.setBackground(Color.PINK);
        window.add(panelLabelFile);

        panelFile = new JPanel();
        panelFile.setPreferredSize(new Dimension(100000,50));
        window.add(panelFile);

        panelLabelLength = new JPanel();
        panelLabelLength.setPreferredSize(new Dimension(100000,30));
        panelLabelLength.setBackground(Color.PINK);
        window.add(panelLabelLength);

        panelLength = new JPanel();
        panelLength.setPreferredSize(new Dimension(100000,50));
        window.add(panelLength);

        panelLabelVisualisation = new JPanel();
        panelLabelVisualisation.setPreferredSize(new Dimension(100000,30));
        panelLabelVisualisation.setBackground(Color.PINK);
        window.add(panelLabelVisualisation);

        panelVisualisation = new JPanel();
        panelVisualisation.setPreferredSize(new Dimension(100000,150));
        window.add(panelVisualisation);

        // Adding 3 labels to the panels
        labelFile = new JLabel("Import a file:");
        panelLabelFile.add(labelFile);

        labelLength = new JLabel("Give a minimum length for the ORF's:");
        panelLabelLength.add(labelLength);

        labelVisualisation = new JLabel("Below you can see the ORF's in the input sequence");
        panelLabelVisualisation.add(labelVisualisation);

        // Putting textfield in panels
        textFieldFile = new JTextField();
        textFieldFile.setColumns(25);
        panelFile.add(textFieldFile);

        textFieldLength = new JTextField();
        textFieldLength.setColumns(10);
        panelLength.add(textFieldLength);

        // Adding buttons besides the textfields
        buttonFile = new JButton("Import file");
        panelFile.add(buttonFile);
        buttonFile.addActionListener(this);

        buttonLength = new JButton("Find ORF's");
        panelLength.add(buttonLength);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == buttonFile){
            int reply;
            File selectfile;
            JFileChooser filechooser = new JFileChooser();
            reply = filechooser.showOpenDialog(this);
            if (reply == JFileChooser.APPROVE_OPTION){
                selectfile = filechooser.getSelectedFile();
                textFieldFile.setText(selectfile.getPath());
            }
            if (reply == JFileChooser.CANCEL_OPTION){
                textFieldFile.setText("Geen bestand ingevoerd");
            }

        }
    }
}
