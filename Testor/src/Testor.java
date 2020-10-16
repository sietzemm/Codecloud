public class Testor {
    public static void main(String[] args){
        System.out.println("Testor : ");

        Testor testor = new Testor();
        testor.updateTime();

    }

    public void updateTime(){
        String testString = "14:22:02";
        String[] testString2 = testString.split(":");
        String testString3 = testString2[0] + testString2[1] + testString2[2];
        String[] testString4 = testString3.split("");


        int[] currTime = new int[testString4.length];

        for(int i = 0; i < currTime.length; i++){
            currTime[i] = Integer.parseInt(testString4[i]);
            System.out.println("value : " + currTime[i]);
        }


    }
}
