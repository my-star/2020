import com.PayrollSystem.handler.PayrollHandler;
import com.PayrollSystem.model.Employee;
import java.util.Scanner;

public class PayrollSystem {
	private static PayrollHandler payrollhandler = new PayrollHandler();

	public static void main(String args[]){
		int opr = -1;
		String n = null;
		double s=0.0d;
		
		Scanner in=new Scanner(System.in);
		
		while (true) {
			System.out.println("Please input 1 or 2 or 3 ,0 to End!:");
			opr=in.nextInt();
			in.nextLine();
			if(0==opr) {
				System.out.println("End.");
				break;
			}
			else if(1==opr){
				System.out.println("Add an Employee!");
				System.out.println("Please input the Employee name:");
				n=in.nextLine();
				System.out.println("Please input the Employee's salary:");
				s=in.nextDouble();
				payrollhandler.AddEmployee(n,s);
				payrollhandler.printStaff();
				System.out.println("**************************************");
				continue;
				}
			else if(2==opr) {
				System.out.println("Delete an Employee!");
				System.out.println("Please input the name of the Employee:");
				n=in.nextLine();
				payrollhandler.delEmployee(n);
				payrollhandler.printStaff();
				System.out.println("**************************************");
				continue;
			}
			if(3==opr) {
				System.out.println("Raise an employye's salary:");
				System.out.println("Please input the Employee's name");
				n=in.nextLine();
				System.out.println("Please intput the salary Raised:");
				s=in.nextDouble();
				payrollhandler.addSalary(n, s);
				payrollhandler.printStaff();
				System.out.println("**************************************");
				continue;
			}
						
			}
		}
}

	/*	Employee e1  = new Employee();
	        Employee e2 = new Employee();

		e1.setName("xiaoming");
		e1.setSalary(2278.0);

		e2.setName("Hxiaowu");
		e2.setSalary(8878.8);

		System.out.print("name = " + e1.getName());
		System.out.println(", salary = " + e1.getSalary());

		System.out.print("name = " +e2.getName());
		System.out.println(",salary = " + e2.getSalary());	
	*/
	
