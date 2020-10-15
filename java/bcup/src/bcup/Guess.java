package bcup;
import java.util.Scanner;

public class Guess {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		String play_AgainString="";
		do {
			int number = (int)(Math.random()*100+1);
			int guess = 0;
			while(guess!= number)
			{
				System.out.println("Guess a number between 1 and 100:");
				guess = scanner.nextInt();
				if(guess<number)
					System.out.println(guess + " is too low. Try again.");
				else if(guess>number)
					System.out.println(guess + " is too big. Try again.");
				else 
					System.out.println(guess + " is correct. You win!");	
			}
			System.out.println("Would you like to play again (y/n)?");
			play_AgainString = scanner.next();
		}while(play_AgainString.equalsIgnoreCase("y"));
		System.out.println("Thank you for playing! Goodbye.");
		scanner.close();
	}

}
