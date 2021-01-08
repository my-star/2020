package bcup;
import java.net.*;
public class InetAddressTest {

	public static void main(String[] args)throws UnknownHostException {
		// TODO Auto-generated method stub
		InetAddress address = InetAddress.getLocalHost();
		System.out.println(address);
		InetAddress address2 =InetAddress.getLocalHost();
		System.out.println(address2);
		//address=InetAddress.getByName("baidu.com");
		System.out.println(address);
	}

}
