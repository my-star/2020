public class PayrollSystem{

	public static void main(String args[]){

		Employee e1  = new Employee();
	        Employee e2 = new Employee();

		e1.setName("xiaoming");
		e1.setSalary(2278.0);

		e2.setName("Hxiaowu");
		e2.setSalary(8878.8);

		System.out.print("name = " + e1.getName());
		System.out.println(", salary = " + e1.getSalary());

		System.out.print("name = " +e2.getName());
		System.out.println(",salary = " + e2.getSalary());	
	}
}
