package bcup;
//import bcup.box;
public class BoxDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		box myBox=new box();
		double vol;
		myBox.height=109;
		myBox.lenth=101;
		myBox.width=102;
		//vol=myBox.height*myBox.lenth*myBox.width;
		//System.out.println("vol is "+(int)vol);
		vol=myBox.volume();
		System.out.println(vol);
	}
	

}
