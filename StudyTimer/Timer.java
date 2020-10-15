import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import java.util.Date;

import javafx.event.ActionEvent;
import javafx.geometry.Insets;
import javafx.scene.Cursor;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.image.Image;
import javafx.scene.layout.Background;
import javafx.scene.layout.BackgroundImage;
import javafx.scene.layout.BackgroundPosition;
import javafx.scene.layout.BackgroundRepeat;
import javafx.scene.layout.BackgroundSize;
import javafx.scene.layout.GridPane;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import jdk.tools.jlink.internal.Platform;

public class Timer extends Application {

    // Date/Time variables
    SimpleDateFormat format = new SimpleDateFormat("dd-MM-yyyy");
    private String dateString = format.format(new Date());
    private int minute = 00;
    private int hour,second = 0;
    private boolean check = false;
    BackgroundImage background_image_day= new BackgroundImage(new Image(getClass().getResourceAsStream("images/background_day.png")),
            BackgroundRepeat.REPEAT, BackgroundRepeat.NO_REPEAT, BackgroundPosition.DEFAULT,
            BackgroundSize.DEFAULT);

    BackgroundImage background_image_night= new BackgroundImage(new Image(getClass().getResourceAsStream("images/background_night.png")),
            BackgroundRepeat.REPEAT, BackgroundRepeat.NO_REPEAT, BackgroundPosition.DEFAULT,
            BackgroundSize.DEFAULT);

    // Buton styles
    final String BTN_STYLE = "-fx-background-color: #45748a; -fx-border-solid: 2px; -fx-border-color: #244a5c;";
    final String BTN_HOVER_STYLE = "-fx-background-color: #02567d; -fx-cursor: hand";

    @Override
    public void start(Stage primaryStage){
        GridPane root = new GridPane();
        root.setBackground(new Background(background_image_day));

        Label currentTimeLbl = new Label("00:00:00");
        root.setMargin(currentTimeLbl, new Insets(25,0,100,125));
        currentTimeLbl.setTextFill(Color.web("#ffffff"));
        currentTimeLbl.setFont(Font.font("Cambria", 22));
        root.add(currentTimeLbl,0,0);

        Label greetingLbl = new Label("hello world");
        root.setMargin(greetingLbl, new Insets(-175,0,0,85));
        greetingLbl.setTextFill(Color.web("#ffffff"));
        greetingLbl.setFont(Font.font("Cambria", 18));
        root.add(greetingLbl,0,1);

        Label motivationalTextLbl = new Label("");
        root.setMargin(motivationalTextLbl, new Insets(-100,0,0,100));
        motivationalTextLbl.setTextFill(Color.web("#ffffff"));
        motivationalTextLbl.setFont(Font.font("Cambria", 22));
        root.add(motivationalTextLbl,0,2);

        Button startBtn = new Button("Start timer");
        currentTimeLbl.setPadding(new Insets(25,0,50,0));
        startBtn.setStyle(BTN_STYLE);
        startBtn.setMinWidth(350);
        startBtn.setMinHeight(50);
        startBtn.setOnMouseEntered(e ->startBtn.setStyle(BTN_HOVER_STYLE));
        startBtn.setOnMouseExited(e ->startBtn.setStyle(BTN_STYLE));

        startBtn.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent actionEvent) {
                check = true;
                startBtn.setCursor(Cursor.HAND);
                startBtn.setText("Start timer");
                motivationalTextLbl.setText("You can do it!");
            }
        });
        root.add(startBtn,0,3);

        Button pauseBtn = new Button("Pause timer");
        pauseBtn.setMinWidth(175);
        pauseBtn.setStyle(BTN_STYLE);
        pauseBtn.setOnMouseEntered(e ->pauseBtn.setStyle(BTN_HOVER_STYLE));
        pauseBtn.setOnMouseExited(e ->pauseBtn.setStyle(BTN_STYLE));
        pauseBtn.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent actionEvent) {
                check = false;
                motivationalTextLbl.setText("Timer paused");
                startBtn.setText("Resume");
                pauseBtn.setCursor(Cursor.HAND);
            }
        });
        root.add(pauseBtn,0,4);

        Button resetBtn = new Button("Reset timer");
        resetBtn.setMinWidth(175);
        resetBtn.setStyle(BTN_STYLE);
        resetBtn.setOnMouseEntered(e ->resetBtn.setStyle(BTN_HOVER_STYLE));
        resetBtn.setOnMouseExited(e ->resetBtn.setStyle(BTN_STYLE));
        root.setMargin(resetBtn, new Insets(0,0,0,175));
        resetBtn.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent actionEvent) {
                check = false;
                second = 0;
                minute = 0;
                hour = 0;
                currentTimeLbl.setText("00:00:00");
                motivationalTextLbl.setText("");
                resetBtn.setCursor(Cursor.HAND);
            }
        });
        root.add(resetBtn,0,4);

        // Thread for time
        new Thread(new Runnable(){
            @Override
            public void run(){
                try{
                    while (true) {
                        Platform.runLater(new Runnable(){
                            @Override
                            public void run(){
                                changeBackground(root);
                                changeMotivationalText(greetingLbl);
                                if(check == true){
                                    updateTime(currentTimeLbl);
                                }
                            }
                        });
                        Thread.sleep(1000);
                    }
                }
                catch(InterruptedException ex){
                }
            }
        }).start();

        Scene scene = new Scene(root, 350, 350);
        primaryStage.setResizable(false);
        primaryStage.setTitle("StudyTimer");
        primaryStage.setScene(scene);
        primaryStage.show();

    } // end of start method

    public void updateTime(Label label){
        // Seconden
        if (second < 10){
//            System.out.println("Updating second : " + second);
            label.setText("0"+String.valueOf(hour)+":0"+ String.valueOf(minute)+":0" + String.valueOf(second));
            second ++;

        }
        if (second >= 10 && second < 60){
//            System.out.println("Updating second : " + second);
            label.setText("0"+String.valueOf(hour)+":0"+ String.valueOf(minute)+":" + String.valueOf(second));
            second ++;
        }
//
        if (second == 60){
            minute ++;
            second = 0;
            label.setText("0"+String.valueOf(hour)+":0"+ String.valueOf(minute)+":0" + String.valueOf(second));
        }

        if (minute != 0 && minute < 10 && second >= 10){
            label.setText("0"+String.valueOf(hour)+":0"+ String.valueOf(minute)+":" + String.valueOf(second));
        }
        if (minute >= 10 && minute < 60 && second < 10){
            label.setText("0"+String.valueOf(hour)+":"+ String.valueOf(minute)+":0" + String.valueOf(second));
        }
//
        if (minute == 60){
            hour ++;
            minute = 0;
            second = 0;
            label.setText("0"+String.valueOf(hour)+":"+ String.valueOf(minute)+":" + String.valueOf(second));
        }
//
        if (hour < 10 && minute < 10 && second < 10){
            label.setText("0"+String.valueOf(hour)+":0"+ String.valueOf(minute)+":0" + String.valueOf(second));
        }

        if(hour >= 10 && minute < 10 && second < 10){
            label.setText(String.valueOf(hour)+":0"+ String.valueOf(minute)+":0" + String.valueOf(second));
        }
    }

    public void changeMotivationalText(Label label){
        int[] hourAr = new int[2];
        hourAr[0] = Integer.valueOf(getCurrentTime().substring(0,1));
        hourAr[1] = Integer.valueOf(getCurrentTime().substring(1,2));
        int hourD1 = hourAr[0];
        int hourD2 = hourAr[1];
        int hour = Integer.valueOf(getCurrentTime().substring(0,2));

        System.out.println(hourD1 + ":" + hourD2);
        // Message between 06:00 and 08:00
        if(hourD1 == 0 && hourD2 >= 6 && hourD2 < 8){
            label.setText("Your'e an early bird");
            System.out.println("Early bird");
        }

        // Message between 08:00 and 12:00
        if(hourD1 == 0 || hourD1 == 1 && hourD2 == 1 || hourD2 == 2){
            label.setText("Good morning Sietze");
        }

        // Message between 12:00 and 18:00
        if(hour >= 12 && hour <= 18){
            label.setText("Good afternoon Sietze");
            System.out.println("Good afternoon Sietze");
        }

        // Message between 18:00 and 00:00
        if(hour >= 18 && hour < 24){
            label.setText("Good evening Sietze");
            System.out.println("Good evening Sietze");
        }
    }

    public void changeBackground(GridPane pane){
        if (Integer.valueOf(getCurrentTime().substring(0,1)) == 2){
            pane.setBackground(new Background(background_image_night));
        } else {
            pane.setBackground(new Background(background_image_day));
        }
    }

    public String getCurrentTime(){
        String timeSecond = new String(String.valueOf(LocalDateTime.now().getSecond()));
        String timeMinute = new String(String.valueOf(LocalDateTime.now().getMinute()));
        String timeHour = new String(String.valueOf(LocalDateTime.now().getHour()));
        return timeHour+":"+timeMinute+":"+timeSecond;
    }

    public void showView(){
        Timer.launch();
    }
}
