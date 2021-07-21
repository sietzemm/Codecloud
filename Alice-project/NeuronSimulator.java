import java.io.*;
import java.lang.*;
import java.util.*;
/**
* First test in simulating a neuron
*
*@author Sietze Min
*@version 1.0 - 2-04-2017
*@version 2.0 - 8-12-2018 // expanded functionality with simulator class and timer ability
 */

 // Gui implentation ?
 //


 // Initializes the simulator
public class NeuronSimulator {
    // <==== FIELDS =====>

    // Kickstarts the program
    public static void main(String[] args){
        Simulator sim = new Simulator(100); // creates a simulator object
        sim.runSimulation(5000);            // runs the simulation for x amount of time (milliseconds)
        sim.writeData();                    // Writes generated results to a file
    }
} // end of class NeuronSimulator

class Simulator{
    // <==== FIELDS =====>
    // private int neuronAmount = 0;
    private ArrayList<Neuron> neuron_list = new ArrayList<Neuron>();
    private long t = System.currentTimeMillis();
    private ArrayList<String> outputData = new ArrayList<String>(); // used for data output generation

    // Constructor declaration for running the actual simulator
    public Simulator(int amount){
        for(int i=1; i< amount; i++){
            Neuron neuron = new Neuron(1); // creates a new neuron object.
            neuron_list.add(neuron);
        }

        // System.out.println("Number of neurons created  :" + neuron_list.size());
        System.out.println("Finished initial creation of the simulation.");
        System.out.println(amount + " neurons are sucessfully created.");
        System.out.println(neuron_list.size());
    }

    // Runs the simulation for a specified amount of time.
    public void runSimulation(int duration){
        int index = 0;
        long sim_time = t + duration;
        String output_string;

        System.out.println("Running simulation!");
        System.out.println(neuron_list.size());

        while(System.currentTimeMillis() < sim_time){

            while(index < neuron_list.size()){
                for (Neuron n : neuron_list) {
                    // String a;
                    output_string = ("Fseq value of neuron :" + n.toString() + ":" + n.getFseq() + "index : " + index);
                    index++;
                    outputData.add(output_string);
                }
            } // ends inner while loop
        } // ends outer while loop

        System.out.println("Simulation has stopped");
        // Simulation code goes here
    }  // end of runSimulation class

    // Writes the generated output into a text file.
    public void writeData(){
        // final Formatter form;
        // int i = 0;
        try{
            FileWriter fw = new FileWriter("NeuronSimulatorData.txt");
            PrintWriter pw = new PrintWriter(fw);
            outputData.forEach((n) -> pw.append(n + "\n"));
            pw.close();
        
        }
        catch(IOException e) {
            System.out.println("Error output");
        }
    } // end of writeData class 

    // gets all neuron properties 
    public void getProperties(Neuron neuron_name){
        System.out.println("Specific neuron properties....");
    }

} // end of simulator class


// Represents an individual neuron
class Neuron {
    // basic implementation of a neuron.
    // should include a way to fire and receive signals. Calculate upon them to certain threshold.
    // 


    // <==== FIELDS =====>
    private double fseq;
    // private int identifier = 12;
    private boolean isAlive = true;        // dead or alive neuron.
   
    // Constructor method
    public Neuron(int f){
        this.fseq = f;
    };

    // Neuron fires signal
    public int fireSignal(int value){
        // Calculations go here
        return value;
    }

    // Gets the value Fseq.
    public double getFseq(){
        return fseq;
    }

    // sets the value for fseq
    public double setFseq(int value){
        this.fseq = value;
        return value;
    }

    // sets the neuron to dead / alive
    public boolean setAlive(boolean value){
        this.isAlive = value;
        return this.isAlive;
    }

} // end of class neuron
