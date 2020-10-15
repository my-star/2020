package bcup;

public class Average {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//double nums[]= {10.1,11.2,12.3,13.4,14.5};
		//double result =0;
		int nums[] = new int[100];
		int sum=0;
		for(int i=0;i<100;i++)
		{
			//result=result+nums[i];
			nums[i]=(int)(Math.random()*100);
			sum =sum +nums[i];
			System.out.println(i+"++"+nums[i]);
		}
		
		//System.out.println("Average is "+result/5);
		System.out.println("The sum is "+sum);
	}

}
