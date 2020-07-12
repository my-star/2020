http://www.h3c.com/CN/D_201312/807770_30005_0.htm

# 配置VLAN接口1的IP地址，客户端将通过该地址连接Stelnet服务器。


<Switch> system-view

[Switch] interface vlan-interface 1

[Switch-Vlan-interface1] ip address 20.20.0.105 255.255.255.0

[Switch-Vlan-interface1] quit

# 生成RSA及DSA密钥对。

[Switch] public-key local create rsa

The range of public key size is (512 ~ 2048).

NOTES: If the key modulus is greater than 512,

It will take a few minutes.

Press CTRL+C to abort.

Input the bits of the modulus[default = 1024]:2048

Generating Keys...

+++++++++++++++++++++++++++

++++++++++++++++++++++++

+++++++++++++++++++++++++++++

+++++++++++++++++++++++++++++++

[Switch] public-key local create dsa

The range of public key size is (512 ~ 2048).

NOTES: If the key modulus is greater than 512,

It will take a few minutes.

Press CTRL+C to abort.

Input the bits of the modulus[default = 1024]:2048

Generating Keys...

*

..+.++++*

# 开启SSH服务器功能。

[Switch] ssh server enable

Info: Enable SSH server

# 配置允许SSH用户认证尝试的最大次数为5次。

[Switch] ssh server authentication-retries 5

# 设置Stelnet客户端登录用户界面的认证方式为AAA认证，远程用户登录协议为SSH。

[Switch] user-interface vty 0 15

[Switch-ui-vty0-15] authentication-mode scheme

[Switch-ui-vty0-15] protocol inbound ssh

[Switch-ui-vty0-15] quit

# 创建本地用户client001，密码为aabbcc，服务类型为SSH，并授权用户访问的命令级别为3。

[Switch] local-user client001

New local user added.

[Switch-luser-client001] password simple aabbcc

[Switch-luser-client001] service-type ssh

[Switch-luser-client001] authorization-attribute level 3

[Switch-luser-client001] quit

# 配置SSH用户client001的服务类型为Stelnet，认证方式为password认证。

[Switch] ssh user client001 service-type stelnet authentication-type password


------------------------------------------------------------------------------------


1.4.4  配置思路

使用SSH的publickey认证方式：客户端首先要生成RSA密钥对，并将公钥文件上传到Stelnet服务器；服务器端也要生成RSA密钥对。服务器使用本地保存的客户端公钥，与报文中携带的客户端公钥进行比较，完成客户端持有公钥的正确性的验证。如果公钥验证成功，客户端继续使用自己本地密钥对的私钥部分，对特定报文进行摘要运算，将所得的结果（即数字签名）发送给服务器，向服务器证明自己的身份；服务器使用预先配置的该用户的公钥，对客户端发送过来的数字签名进行验证，验证成功后，建立安全的SSH连接。
2. 配置Switch作为FTP服务器

# 配置VLAN接口1的IP地址。

<Switch> system-view

[Switch] interface vlan-interface 1

[Switch-Vlan-interface1] ip address 20.20.0.105 255.255.255.0

[Switch-Vlan-interface1] quit

# 在Switch上创建一个ftp类型的本地用户。

[Switch] local-user ftp

New local user added.

[Switch-luser-ftp] password simple ftp

[Switch-luser-ftp] authorization-attribute level 3

[Switch-luser-ftp] authorization-attribute work-directory flash:/

[Switch-luser-ftp] service-type ftp

[Switch-luser-ftp] quit

# 开启SwitchB的FTP服务器功能。

[Switch] ftp server enable

[Switch] quit
3. 配置客户端上传公钥文件

# Host通过FTP登录并上传公钥文件key.pub到Switch。

c:\> ftp 20.20.0.105

Connected to 20.20.0.105.

220 FTP service ready.

User(20.20.0.105:(none)):ftp

331 Password required for ftp.

Password:

230 User logged in.

ftp> put key.pub

200 Port command okay.

150 Opening ASCII mode data connection for /key.pub.

226 Transfer complete.

ftp> bye

221 Server closing.

 

c:\
4. 配置Switch作为Stelnet服务器

# 生成RSA密钥对。

[Switch] public-key local create rsa

The range of public key size is (512 ~ 2048).

NOTES: If the key modulus is greater than 512,

It will take a few minutes.

Press CTRL+C to abort.

Input the bits of the modulus[default = 1024]:2048

Generating Keys...

++++++++

++++++++++++++

+++++

++++++++

# 启动SSH服务器。

[Switch] ssh server enable

# 设置客户端登录用户界面的认证方式为AAA，远程用户登录协议为SSH，用户能访问的命令级别为3。

[Switch] user-interface vty 0 15

[Switch-ui-vty0-15] authentication-mode scheme

[Switch-ui-vty0-15] protocol inbound ssh

[Switch-ui-vty0-15] user privilege level 3

[Switch-ui-vty0-15] quit

# 从文件key.pub中导入远端的公钥，并命名为Switch001。

[Switch] public-key peer Switch001 import sshkey key.pub

# 创建本地用户client002，服务类型为SSH，并授权用户访问的命令级别为3。

[Switch] local-user client002

New local user added.

[Switch-luser-client002] service-type ssh

[Switch-luser-client002] authorization-attribute level 3

[Switch-luser-client002] quit

# 设置SSH用户client002的认证方式为publickey，并指定公钥为Switch001。

[Switch] ssh user client002 service-type stelnet authentication-type publickey assign publickey Switch001

[Switch] quit
5. 客户端建立与Stelnet服务器的连接

# 指定私钥文件，并建立与Stelnet服务器的连接。

打开PuTTY.exe程序，出现如图9所示的客户端配置界面。在“Host Name（or IP address）”文本框中输入Stelnet服务器的IP地址为20.20.0.105。

图9 SSH客户端配置界面（1）
1.4.6  验证配置

按提示输入用户名client002，即可进入Switch的配置界面。

Login as: client002

Authenticating with public key “rsa-key-20130316”

 

****************************************************************************** 

* Copyright (c) 2004-2013 Hangzhou H3C Tech. Co., Ltd. All rights reserved.  * 

* Without the owner's prior written consent,                                 * 

* no decompiling or reverse-engineering shall be allowed.                    * 

****************************************************************************** 

                                                                               

<Switch>
1.4.7  配置文件

#

vlan 1

#

 public-key peer Switch001

  public-key-code begin

30819D300D06092A864886F70D010101050003818B0030818702818100A2DBC1FD76A837BEF5D322598442D6753B2E8F7ADD6D6209C80843B206B309078AFE2416CB4FAD496A6627243EAD766D57AEA70B901B4B4566D9A651B133BAE34E9B9F04E542D64D0E9814D7E3CBCDBCAF28FF21EE4EADAE6DF52001944A40414DFF280FF043B14838288BE7F9438DC71ABBC2C28BF78F34ADF3D1C912579A19020125

  public-key-code end

 peer-public-key end

#

local-user client002

 authorization-attribute level 3

 service-type ssh

#

local-user ftp

 password cipher $c$3$sg9WgqO1w8vnAv2FKGTOYgFJm3nn2w==

 authorization-attribute work-directory flash:/

 authorization-attribute level 3

 service-type ftp

#

interface Vlan-interface1

 ip address 20.20.0.105 255.255.255.0

#

 ssh server enable

 ssh user client002 service-type stelnet authentication-type publickey assign publickey Switch001

#

user-interface vty 0 15

 authentication-mode scheme

 user privilege level 3

 protocol inbound ssh

#

-----------------------------------------------------------------------------------------------------------
