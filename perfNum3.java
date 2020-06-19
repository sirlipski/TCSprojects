import java.math.BigInteger;
import java.util.concurrent.TimeUnit;
import java.util.*; 
import java.text.*; 
import java.time.format.DateTimeFormatter;  
import java.time.LocalDateTime;    

public class perfNum3 {

	public static void main(String[] args) {
		DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm");
		LocalDateTime now = LocalDateTime.now();  
		System.out.println("Starting perfect number sequence..."
				+ "\nThe date and time of the start is "+dtf.format(now)
				+".\nThe program is intended to run for 1 week, but theoretically can work forever"
				+ "\nThis program finds perfect numbers. A perfect number is when a number equals to the sum of its positive divisors,"
				+ "\nFor example, 6 = 1 + 2 + 3 = 1 * 6 = 2 * 3"
				+ ".\nThis program uses the Lucas–Lehmer primality test (you can google it)"
				+ "\n\nLet's Begin!!!\n");
		pressAnyKeyToContinue();
		int n = 2;
		int counter = 1;
		double startTime = System.currentTimeMillis();
		System.out.print("Term\t\t\t\t\tPerfect Number\t\t\t\t\tTime elapsed\n");
		System.out.print(counter + ":\t\t\t\t\t " +(int)(Math.pow(n,2-1)*(Math.pow(n, 2)-1)) + ": \t");
		outputTime(System.currentTimeMillis() - startTime);
		n++;
		counter++;
		NumberFormat formatter = new DecimalFormat("0.###E0", DecimalFormatSymbols.getInstance(Locale.ROOT));
		while(true) {
			BigInteger checker = BigInteger.valueOf(2).pow(n).subtract(BigInteger.valueOf(1));
			if(checker.isProbablePrime(1) && BigInteger.valueOf(n).isProbablePrime(1)){
				BigInteger two = BigInteger.valueOf(2).pow(n-1);
				BigInteger num = checker.multiply(two);
				if (counter < 5) {
					System.out.print(counter + ":\t\t\t\t\t " + num + ": \t");
					outputTime(System.currentTimeMillis() - startTime);
				}else {
					System.out.print(counter + ":\t\t\t\t\t " + formatter.format(num) + "\b: ");
					outputTime(System.currentTimeMillis() - startTime);
				}
				counter++;
			}
			n+=2;
		}
	}

	private static void pressAnyKeyToContinue()
	{ 
		System.out.println("Press Enter key to continue...");
		try
		{
			System.in.read();
		}  
		catch(Exception e)
		{}  
	}
	public static void outputTime(double timeElapsed) {
		double seconds = timeElapsed/1000;
		int days = (int)seconds/(24 * 60 * 60);
		seconds -= days / ( 24 * 60 * 60);
		int hours = (int)seconds / (60 * 60);
		seconds -= hours * 60 * 60;
		int minutes = (int)(seconds / 60);
		seconds -= minutes * 60;
		NumberFormat formatter = new DecimalFormat("0.##", DecimalFormatSymbols.getInstance(Locale.ROOT));

		System.out.printf(
				"\t\t\t\t\t%d days, %d hours, %d minutes, %s seconds%n", 
				days, hours, minutes, formatter.format(seconds));
	}
}
