classDeclaration{
	classBosy
}
---
[public][abstract|final] class ClassName [extends SuperClassName]
		
		[implements InterfaceNameList]
{classbody}

---
```java
public class Employee{
	private String name;
	private double salary;

	public void setName(String na){
		name=na;
	}
	public void setSalary(double sa){
		salary=sa;
	}

	public String getName(){
		return name;
	}
	public double getSalary(){
		return salary;
	}

```
```java
class Employee{

	private String name;
	private double salary;

	Employee(String n,double s){

		name=n;
		salary=s;
	}
	String getName(){
		return name;
	}
	double getSalary(){
		return salary;
	}
```	
