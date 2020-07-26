package com.PayrollSystem.handler;

import com.PayrollSystem.model.Employee;

public class PayrollHandler {
	private Employee[] staff = new Employee[100];
	
	public void printStaff() {
		
		for(int i =0;i<staff.length;i++) {
			if(null !=staff[i]) {
				System.out.print("name = " +staff[i].getName());
				System.out.println(",salary = "+staff[i].getSalary());
			}
		}
	}
	public void AddEmployee(String na,double sa) {
		
		for(int i=0;i<staff.length;i++) {
			if(null == staff[i]) {
				staff[i]=new Employee();
				staff[i].setName(na);
				staff[i].setSalary(sa);
				break;
			}
		}
	}

	public void addSalary(String na,double sa) {
		
		for(int i=0;i<staff.length;i++) {
			if(null!= staff[i]) {
				if(staff[i].getName().equals(na)) {
					staff[i].setSalary(staff[i].getSalary()+sa);
					break;
			}
			}
		}
	}
	public void delEmployee(String na) {
		for(int i=0;i<staff.length;i++) {
			if(staff[i].getName().equals(na)) {
				staff[i]=null;
				break;
			}	
		}
	}
	
}
