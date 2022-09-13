# get a list of all the ports on the system that are listening.
$system_ports = Get-NetTCPConnection -State Listen

# read a list of ports from the file.
$text_port = Get-Content -Path C:\Users\Administrator\Desktop\ports.txt

# iterate through all the ports in the file to see if the ports are listening.
foreach($port in $text_port){

    if($port -in $system_ports.LocalPort){
        echo $port
     }

}