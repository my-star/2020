public class stringReverse{
	public static void main(String args[]){
		String str="This is a test string.";
		String strR= reverse(str);
		System.out.println(strR);
	}
	static String reverse(String s){
		int len = s.length();
		StringBuffer buffer = new StringBuffer(len);
		for(int i=len-1;i>=0;i--)
			buffer.append(s.charAt(i));
		return buffer.toString();
	}
}
