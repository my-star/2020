package bcup;
import javax.swing.*;
import java.util.Scanner;
public class nice {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//System.out.println("mat");
		/*Scanner scan =new Scanner(System.in);
		for(int i=1;i<=100;i++)
		{
		int guess=(int) (Math.random()*100+1);
		System.out.println("--"+i+"+++"+guess);
		}
		*/
		/*
		JFrame frame=new JFrame();
		
		frame.setSize(220,300);
		frame.setVisible(true);
		frame.setLocation(200, 100);
		*/
		Scanner scanner = new Scanner(System.in);
		int guess = (int)(Math.random()*100+1);
		int number=0;
		System.out.println ("Please input one intger between 1-100:");
		
		while (guess!=number)
		{
			number =scanner.nextInt();
			if(number<guess)
			{
				System.out.println("smaller,please try again");
				//100return;
			}
			else if (number>guess)
			{
				System.out.println("bigger,please try again");
				//return;
			}
			else {
				System.out.println("Congratulation,happy time!");
			}
		}
	}

}
