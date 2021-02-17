import java.text.NumberFormat;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
      final byte Months_In_Year = 12;
      final byte percent = 100;

      Scanner scanner = new Scanner(System.in);

      System.out.print("Principal: ");
      int principal = scanner.nextInt();

      System.out.print("Annual Interst Rate: ");
      float annualInterst = scanner.nextFloat();
      float monthlyInterst = annualInterst / percent / Months_In_Year;

      System.out.print("period (Years: ");
      byte years = scanner.nextByte();
      int numberOfPayments = years * Months_In_Year;

      double mortgage = principal * (monthlyInterst * Math.pow(1 + monthlyInterst, numberOfPayments / (Math.pow(1 + monthlyInterst, numberOfPayments) -1)));
      
      String mortageFormatted = NumberFormat.getCurrencyInstance().format(mortgage);
      System.out.println("Mortgage" + mortageFormatted);

      scanner.close();
            
    }

}
