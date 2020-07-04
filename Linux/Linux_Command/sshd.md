sshd -OpenSSH SSH daemon

sshd (OpenSSH Daemon)is the daemon program for ssh.Together these programs repleace rlogin and rsh,and provide secure encrypted communications between two untrusted hosts over an insecure network.
sshd listens for connections from clients.It is normally started at boot from /etc/init.d/ssh.It forks a new daemon for each incoming connection. The forked daemons handle key exchange,encryption,authentication,command execution,and data exchange.
sshd can be configured using command-line options or a configuration file (by default sshd_config);command-line options override values specified in the configuration file.sshd rereads its configuration file when it receives a hangup signal,SIGHUP,by executing itself with the name and options it was started with,e.g./usr/sbin/sshd.

AUTHENTICATION
The OpenSSH SSH daemon supports SSH protocol 2 only.Each host has a host -specific key,used to identify the host .Whenever a client connects,the daemon responds with its public host key.The client compares the host key againt its own database to verify that it has not changed.Forward security is provided through a Diffie-Hellman key agreement.
This key agreement results in a shared session key. The rest of the session is encrypted using a symmetric cipher,currently 128-bit AES,Blow-fish,3DES,CAST128,Arcfour,192-bigAES, or 256-bit AES.The clientselects the encryption algorithm to use from those offered by the server.Additionally ,session integrity is provided through a cryptographhic message authentication code (hmc-md5,hmac-sha1,umac-64,umac-128,hmac-sha2-256 or hmac-sha2-512).
