echo "Please provide the port range to scan."
[int]$start_port = Read-Host -Prompt 'Input first port in range to scan: '
[int]$last_port = Read-Host -Prompt 'Input last port in range to scan: '

for ($i=$start_port; $i -le $last_port; $i++){
	Test-NetConnection localhost -Port $i
}