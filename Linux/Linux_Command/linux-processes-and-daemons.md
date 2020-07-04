# Understanding what runs on your Linux system (and why)
> https://linux-audit.com/running-processes-and-daemons-on-linux-systems/
## Linux processes and daemons

Each Linux system has a bunch of processes running.Most of these processes might be familiar to you if you regularly use a command like ps or top to display them.Processes may look like  just an item in a list. They are actually complicated pieces of code that are tamed by a memory manager.To truly understand how your system is running,knowledge of process(or memory) management is of great help. So let's make a jump into the internals of Linux by learning the tools at our disposal.

### What is a process?
Each system has a particular goal it wants to achieve.Such a goal could be providing a website to anonymous vistors all over the world.To enable thar ,there should be something listening to ghe individual website requests,process them,and finally send back the related website page.We call this a process and it consists of machine code.These are individual instrucions on what the system should do.These instructions include reading an image from the hard disk,sending data via the netwrok interface,or saving an error message in a log file.
Processes come in different forms.The most common type is the commands you may type into a shell program.A shell is a "wrapper" for your Linux console or virtual terminal screen(when using SSH).Most users use the default Bourne Again Shell(or bash).It allows you to type in text, and it will act upon this input.For example,when you type in a command like ls,it sees this as a known command and executes it.
The real magic happens when you run commands. In this event,the shell will decide to run a built-in action or start a program from the hard disk. We call these programs on disk a 'binary'.This binary itself is stored with a specific format,which is typically ELF,or Executable and Linkable Format.

### What is a Linux daemon?
Some processes have the goal to run for a long time on the system int the background.This could be to fulfill requests like scannning an incoming email or sending back a page of a website.These processes are called daemon.Besides the duration,another big difference is that daemons do not need interaction with the terminal.Typically they won't send any date to it but use log files instead.Daemons are often started directly after the operating system started.Most have a 'd' at the end of the process name,to hint that they are a daemon process.

Good to remember:A daemon is always a process,but not all processes are a deamon.


### What about services?

Typically the term 'service' was used on Windows systems.With the introduction of systemd,this term is now more applicable for Linux as well.A service is a combination of resources to provide some functionalality.For example an SSH service ,that consists of running the related deamon and any dependencies like networking.
