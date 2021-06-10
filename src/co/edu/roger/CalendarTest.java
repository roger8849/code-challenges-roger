package co.edu.roger;

import java.util.Calendar;
import java.util.Date;

public class CalendarTest {

    public static void main(String[] args) {
        Date date = new Date();
        int semanas = 9;
        semanas=semanas*7;
        Calendar calendar = Calendar.getInstance();
        calendar.setTime(date);
        calendar.add(Calendar.DAY_OF_YEAR, semanas);
        System.out.println(calendar.getTime());
    }
}
