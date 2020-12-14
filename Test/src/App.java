public class App{

    public static void main(String[] args){
        System.out.println("Hello world!");

    // App.getCount("I am sietze!");
    App application = new App();
    application.getCount("I am Sietze!");        
    }

    public void getCount(String value){
        System.out.println("Here is a value :" + value);
    }
}