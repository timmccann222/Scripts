echo "`n###########################"
echo "# Password Files & Content #"
echo "###########################"

$path = "C:\Users\Administrator\Desktop\emails\*"
$password_files = Get-ChildItem -Path $path -Recurse | Select-String "password"
echo $password_files

echo "`n###########################"
echo "#         HTTPS Link       #"
echo "###########################`n"

$link = Get-ChildItem -Path $path -Recurse | Select-String "https://"
echo $link