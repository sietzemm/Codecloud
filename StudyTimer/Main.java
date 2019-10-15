package StudyTimer;

// Date : 09-10-2019
// Author : Sietze Min
// Desc : A simple timer for multiple purposes

public class Main {
    Timer timer = new Timer();
    public static void main(String[] args){
        System.out.println("Running program");
        Main main = new Main();
        main.Main();
    }
    public void Main(){
        timer.showView();
    }
}