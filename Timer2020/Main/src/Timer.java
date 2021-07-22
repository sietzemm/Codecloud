// Author : Sietze Min
// Last modified : 21-07-2021

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.scene.Cursor;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.Background;
import javafx.scene.layout.BackgroundImage;
import javafx.scene.layout.BackgroundPosition;
import javafx.scene.layout.BackgroundRepeat;
import javafx.scene.layout.BackgroundSize;
import javafx.scene.layout.GridPane;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.stage.Stage;

public class Timer extends Application {

    // Date/Time variables
    SimpleDateFormat format = new SimpleDateFormat("dd-MM-yyyy");
    private String dateString = format.format(new Date());
    private int minute = 0;
    private int hour = 0;
    private int second = 0;
    private boolean check = false;
    public boolean backgroundCheck = false;
    public boolean isDay = true;
    ArrayList<Label> worldObjList = new ArrayList<Label>(); // contains the cloud and stars

    BackgroundImage background_image_day = new BackgroundImage(
            new Image(getClass().getResourceAsStream("images/background_day_clean.png")), BackgroundRepeat.REPEAT,
            BackgroundRepeat.NO_REPEAT, BackgroundPosition.DEFAULT, BackgroundSize.DEFAULT);

    BackgroundImage background_image_night = new BackgroundImage(
            new Image(getClass().getResourceAsStream("images/background_night.png")), BackgroundRepeat.REPEAT,
            BackgroundRepeat.NO_REPEAT, BackgroundPosition.DEFAULT, BackgroundSize.DEFAULT);

    // Buton styles
    final String BTN_STYLE = "-fx-background-color: #45748a; -fx-border-solid: 2px; -fx-border-color: #244a5c;";
    final String BTN_HOVER_STYLE = "-fx-background-color: #02567d; -fx-cursor: hand";


    @Override
    public void start(Stage primaryStage) {
        GridPane root = new GridPane();
        root.setBackground(new Background(background_image_day));
        

        Label currentTimeLbl = new Label("00:00:00");
        root.setMargin(currentTimeLbl, new Insets(25, 0, 100, 125));
        currentTimeLbl.setTextFill(Color.web("#cecece"));
        currentTimeLbl.setFont(Font.font("Cambria", 22));
        currentTimeLbl.toFront();
        root.add(currentTimeLbl, 0, 0);
        currentTimeLbl.toFront();

        Label greetingLbl = new Label("Good morning!");
        root.setMargin(greetingLbl, new Insets(-175, 0, 0, 85));
        greetingLbl.setTextFill(Color.web("#ffffff"));
        greetingLbl.setFont(Font.font("Cambria", 18));
        root.add(greetingLbl, 0, 1);

        Label motivationalTextLbl = new Label("");
        root.setMargin(motivationalTextLbl, new Insets(-100, 0, 0, 100));
        motivationalTextLbl.setTextFill(Color.web("#ffffff"));
        motivationalTextLbl.setFont(Font.font("Cambria", 22));
        root.add(motivationalTextLbl, 0, 2);

        Button startBtn = new Button("Start timer");
        currentTimeLbl.setPadding(new Insets(25, 0, 50, 0));
        startBtn.setStyle(BTN_STYLE);
        startBtn.setMinWidth(350);
        startBtn.setMinHeight(50);
        startBtn.setOnMouseEntered(e -> startBtn.setStyle(BTN_HOVER_STYLE));
        startBtn.setOnMouseExited(e -> startBtn.setStyle(BTN_STYLE));

        startBtn.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent actionEvent) {
                check = true;
                startBtn.setCursor(Cursor.HAND);
                startBtn.setText("Start timer");
                motivationalTextLbl.setText("You can do it!");
            }
        });
        root.add(startBtn, 0, 3);

        Button pauseBtn = new Button("Pause timer");
        pauseBtn.setMinWidth(175);
        pauseBtn.setStyle(BTN_STYLE);
        pauseBtn.setOnMouseEntered(e -> pauseBtn.setStyle(BTN_HOVER_STYLE));
        pauseBtn.setOnMouseExited(e -> pauseBtn.setStyle(BTN_STYLE));
        pauseBtn.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent actionEvent) {
                check = false;
                motivationalTextLbl.setText("Timer paused");
                startBtn.setText("Resume");
                pauseBtn.setCursor(Cursor.HAND);
            }
        });
        root.add(pauseBtn, 0, 4);

        Button resetBtn = new Button("Reset timer");
        resetBtn.setMinWidth(175);
        resetBtn.setStyle(BTN_STYLE);
        resetBtn.setOnMouseEntered(e -> resetBtn.setStyle(BTN_HOVER_STYLE));
        resetBtn.setOnMouseExited(e -> resetBtn.setStyle(BTN_STYLE));
        root.setMargin(resetBtn, new Insets(0, 0, 0, 175));
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
                startBtn.setText("Start timer");
            }
        });
        root.add(resetBtn, 0, 4);

        // Thread for time
        new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    while (true) {
                        Platform.runLater(new Runnable() {
                            @Override
                            public void run() {
                                updateGUI(greetingLbl, root); // this methods calls other methods only when necessary
                                changeBackground(root);

                                // only if start button is pressed
                                if (check == true) {                    
                                    updateTimer(currentTimeLbl); // this is executed each second

                                }
                            }
                        });
                        Thread.sleep(1000);
                    }
                } catch (InterruptedException ex) {
                }
            }
        }).start();

        // Thread for moving stars across the background
        new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    while (true) {
                        Platform.runLater(new Runnable() {
                            @Override
                            public void run() {
                                animateBackground();
                            }
                        });
                        Thread.sleep(100);
                    }
                } catch (InterruptedException ex) {
                }
            }
        }).start();

        Scene scene = new Scene(root, 350, 350);
        primaryStage.setResizable(false);
        primaryStage.setTitle("StudyTimer");
        primaryStage.setScene(scene);
        primaryStage.show();

    } // end of start method

    // should only return current time
    public void updateGUI(Label lbl, GridPane pane){
        String currentTime1 = getCurrentTime();
        String[] currentTime2 = currentTime1.split(":");
        String currentTime3 = currentTime2[0] + currentTime2[1] + currentTime2[2];
        String[] currentTime4 = currentTime3.split("");
        int[] currTime = new int[currentTime4.length];

        for(int i = 0; i < currTime.length; i++){
            currTime[i] = Integer.parseInt(currentTime4[i]);
        }

        // if time hour is between midnight (00:00) and 20:00 
        if (currTime[0] == 0 || currTime[0] == 1){

            // if time hour is btween 00:00 and 06:00
            if (currTime[0] == 0 && currTime[1] < 6){
                lbl.setText("Burning the midnight oil!");
            }
            // if time hour is between 06:00 and 10:00
            if (currTime[0] == 0 && currTime[1] >= 6 && currTime[1] <= 9){
                lbl.setText("You are an early bird Sietze!");
            }

            // if time hour is between 10:00 and 12:00
            if (currTime[0] == 1 && currTime[1] >= 0 && currTime[1] <= 2){
                lbl.setText("Good morning Sietze!");
            }

            // if time hour is between 12:00 and 20:00
            if (currTime[0] == 1 && currTime[1] >= 2 && currTime[1] <= 9){
                lbl.setText("Good afternoon Sietze!");
            }

        }
        // if time hour is 2 (20:00 - 00:00)
        if (currTime[0] == 2){
            lbl.setText("Good evenings Sietze!");

            // set background to night at exactly 20:00 and only 20:00
            if(currTime[1] == 0 && currTime[2] == 0 && currTime[3]== 0 && currTime[4] == 0 && currTime[5] == 0){
                changeBackground(pane);
            }
        }
    }

    public void updateTimer(Label label) {
        // seconden
        if (second < 9){
            label.setText("0" + String.valueOf(hour) + ":0" + String.valueOf(minute) + ":0" + String.valueOf(second));
            second ++;

            if (minute < 10){
                label.setText("0" + String.valueOf(hour) + ":0" + String.valueOf(minute) + ":0" + String.valueOf(second));
            } else {
                label.setText("0" + String.valueOf(hour) + ":" + String.valueOf(minute) + ":0" + String.valueOf(second));
            }

        } else {     
            second ++;     
            label.setText("0" + String.valueOf(hour) + ":0" + String.valueOf(minute) + ":" + String.valueOf(second)); 
  

            if (minute < 10){
                label.setText("0" + String.valueOf(hour) + ":0" + String.valueOf(minute) + ":" + String.valueOf(second));
            } else {
                label.setText("0" + String.valueOf(hour) + ":" + String.valueOf(minute) + ":" + String.valueOf(second));
            }
        
        }
        if (second == 60) {
            
                // hour = 0 ;
                second = 0;
                minute ++;
                }

        if (minute == 60) {
                hour ++;
                // second = 0;
                minute = 0;
        }
    }

    public void setInitialBgObj(GridPane pane, int amount, boolean isDay){
     
        for (int i = 0; i < amount; i++) {
            Label worldObjLbl = new Label();
            Image stars = new Image("images/star.png");
            Image clouds = new Image("images/cloud.png");
            int imageSize = (int) ((Math.random() * 10 + 5)); // Random image size
            int initXcoordinate = (int )(Math.random() * 350 + 1);
            int initYcoordinate = (int )(Math.random() * -250 + 1);
            worldObjLbl.setTranslateX(initXcoordinate);
            worldObjLbl.setTranslateY(initYcoordinate);
            pane.add(worldObjLbl,0,2);
            worldObjList.add(worldObjLbl);
            if (isDay == true){
                ImageView view = new ImageView(clouds);
                imageSize = (int) (Math.random() * 20 + 5); // Random image size recalibrated for clouds
                    
                    // make clouds appear farther away by making them opaque
                    if (imageSize <= 11){
                        worldObjLbl.setOpacity(0.5);
                        System.out.println("Changed opacity!" + Integer.toString(imageSize));
                    }
                
                view.setFitHeight(imageSize);
                view.setPreserveRatio(true);
                worldObjLbl.setGraphic(view);
            } else {
                ImageView view = new ImageView(stars);
                view.setFitHeight(imageSize);
                view.setPreserveRatio(true);
                worldObjLbl.setGraphic(view); 
            }
        }
    }
    
    public void changeBackground(GridPane pane) {
        // if time >= 20:00 
        if (Integer.valueOf(getCurrentTime().substring(0, 1)) == 2) {
            pane.setBackground(new Background(background_image_night));
            if (worldObjList.size() == 0){
                setInitialBgObj(pane, 20, false);
            }

        } else {
            pane.setBackground(new Background(background_image_day));
            if (worldObjList.size() == 0){
                setInitialBgObj(pane, 10, true);
            }
        }
    }
    
    public void animateBackground(){
            for (int i = 0; i < worldObjList.size(); i++){                
                double oldX = worldObjList.get(i).getTranslateX();
                // System.out.println("width of clouds : " + Double.toString(worldObjList.get(i).getWidth()));
                // update coordinates

                if(oldX + 1 >= 350){
                    worldObjList.get(i).setTranslateX(-worldObjList.get(i).getWidth()); // if star x-coordinate is bigger than screenwidth, reset to 0. 
                    worldObjList.get(i).setTranslateY(Math.random() * -250 + 1);

                } else {
                    if (worldObjList.get(i).getOpacity() == 0.5){
                        worldObjList.get(i).setTranslateX(oldX + 0.08);
                    
                    }   else {
                        worldObjList.get(i).setTranslateX(oldX + 0.25);
                    }
                }
            }
    }

    public String getCurrentTime() {
        String timeSecond = new String(String.valueOf(LocalDateTime.now().getSecond()));
        String timeMinute = new String(String.valueOf(LocalDateTime.now().getMinute()));
        String timeHour = new String(String.valueOf(LocalDateTime.now().getHour()));
        return timeHour + ":" + timeMinute + ":" + timeSecond;
    }

    public void showView() {
        Timer.launch();
    }

}
