# Hacking with PowerShell
  
Learn the basics of PowerShell and PowerShell Scripting

##  Task 2 - What is PowerShell?

Powershell is the Windows Scripting Language and shell environment that is built using the .NET framework.

This also allows Powershell to execute .NET functions directly from its shell. Most Powershell commands, called *cmdlets*, are written in .NET. Unlike other scripting languages and shell environments, the output of these *cmdlets* are objects - making Powershell somewhat object oriented. This also means that running cmdlets allows you to perform actions on the output object(which makes it convenient to pass output from one *cmdlet* to another). The normal format of a *cmdlet* is represented using **Verb-Noun**; for example the *cmdlet* to list commands is called `Get-Command`.

Common verbs to use include:

* Get
* Start
* Stop 
* Read
* Write
* New
* Out

To get the full list of approved verbs, visit this link: https://docs.microsoft.com/en-us/powershell/scripting/developer/cmdlet/approved-verbs-for-windows-powershell-commands?view=powershell-7

### Questions & Answers

1. **What is the command to get help about a particular cmdlet(without any parameters)?**

```powershell
Get-Help
```

## Task 3 - Basic PowerShell Commands

### Get-Help

Get-Help displays information about a cmdlet. To get help about a particular command, run the following:

```powershell
Get-Help Command-Name
```

You can also understand how exactly to use the command by passing in the `-examples` flag.

```powershell
Get-Help Command-Name -Examples
```

### Get-Command

Get-Command gets all the *cmdlets* installed on the current Computer. The great thing about this *cmdlet* is that it allows for pattern matching like the following:

`Get-Command Verb-*` or `Get-Command *-Noun`

Running `Get-Command New-*` shows all the *cmdlets* for the verb **new**. 

### Object Manipulation

In the previous task, we saw how the output of every *cmdlet* is an object. If we want to actually manipulate the output, we need to figure out a few things:

* passing output to other cmdlets
* using specific object cmdlets to extract information

The **Pipeline(|)** is used to pass output from one *cmdlet* to another. A major difference compared to other shells is that instead of passing text or string to the command after the pipe, powershell passes an object to the next cmdlet. Like every object in object oriented frameworks, an object will contain methods and properties. You can think of methods as functions that can be applied to output from the cmdlet and you can think of properties as variables in the output from a cmdlet. To view these details, pass the output of a cmdlet to the Get-Member cmdlet:

```powershell
Verb-Noun | Get-Member
``` 

An example of running this to view the members for Get-Command is:

```powershell
Get-Command | Get-Member -MemberType Method
```

### Creating Objects From Previous cmdlets

One way of manipulating objects is pulling out the properties from the output of a cmdlet and creating a new object. This is done using the `Select-Object` *cmdlet*. 

Here's an example of listing the directories and just selecting the mode and the name:

```powershell
Get-ChildItem | Select-Object -Property Mode, Name
```

You can also use the following flags to select particular information:

* first - gets the first x object
* last - gets the last x object
* unique - shows the unique objects
* skip - skips x objects

### Filtering Objects

When retrieving output objects, you may want to select objects that match a very specific value. You can do this using the `Where-Object` to filter based on the value of properties. 

The general format of the using this cmdlet is:

```powershell
Verb-Noun | Where-Object -Property PropertyName -operator Value
```

```powershell
Verb-Noun | Where-Object {$_.PropertyName -operator Value}
```

The second version uses the `$_` operator to iterate through every object passed to the Where-Object cmdlet.

**Powershell is quite sensitive so make sure you don't put quotes around the command!**

Where `-operator` is a list of the following operators:

* -Contains: if any item in the property value is an exact match for the specified value
* -EQ: if the property value is the same as the specified value
* -GT: if the property value is greater than the specified value

For a full list of operators, use this link: https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-7.2&viewFallbackFrom=powershell-6

Here's an example of checking the stopped processes:

```powershell
Get-Service | Where-Object -Property Status -eq Stopped
```

### Sort Object

When a cmdlet outputs a lot of information, you may need to sort it to extract the information more efficiently. You do this by pipe lining the output of a cmdlet to the `Sort-Object` cmdlet.

The format of the command would be

```powershell
Verb-Noun | Sort-Object
```

Here's an example of sort the list of directories:

```powershell
Get-ChildItem | Sort-Object
```

### Questions & Answers

1. **What is the location of the file "interesting-file.txt"?**

Check for any files that include *"interesting-file.txt"*.

```powershell
Get-Childitem –Path C:\ -Include *interesting-file.txt* -File -Recurse -ErrorAction SilentlyContinue
```

Output shows that the file is located in `C:\Program Files`

Resource: https://devblogs.microsoft.com/scripting/use-windows-powershell-to-search-for-files/

2. **Specify the contents of this file?**

Show the content of a file:

```powershell
Get-Content .\interesting-file.txt.txt
```

Answer: `notsointerestingcontent`

3. **How many cmdlets are installed on the system(only cmdlets, not functions and aliases)?**

Count the number of cmdlets installed:

```powershell
Get-Command | Where-Object -Property CommandType -eq Cmdlet | measure
```

Answer: `6638`

4. **Get the MD5 hash of interesting-file.txt**

Return MD5 hash of *"interesting-file.txt.txt"*:

```powershell
Get-FileHash "C:\Program Files\interesting-file.txt.txt" -Algorithm MD5 | Format-List
```

Answer: `49A586A2A9456226F8A1B4CEC6FAB329`

5. **What is the command to get the current working directory?**

Answer: `Get-Location`

6. **Does the path "C:\Users\Administrator\Documents\Passwords" Exist(Y/N)?**

Check if directory path exists:

```powershell
Get-Location -Path "C:\Users\Administrator\Documents\Passwords\"
```

Answer: `N`

7. **What command would you use to make a request to a web server?**

Answer: `Invoke-WebRequest`

8. **Base64 decode the file b64.txt on Windows.**

Check for any files that include *"b64.txt"*.

```powershell
Get-Childitem –Path C:\ -Include *b64.txt* -File -Recurse -ErrorAction SilentlyContinue
```

Found the *b64.txt* file located in `C:\Users\Administrator\Desktop`. Decode the file using `certutil` and output it to a file:

```powershell
certutil -decode "C:\Users\Administrator\Desktop\b64.txt" decode.txt
```

Read contents of the file:

```powershell
Get-Content .\decode.txt
```

Answer:

```
this is the flag - ihopeyoudidthisonwindows
the rest is garbage
the rest is garbage
the rest is garbage
the rest is garbage
etc...
```

## Task 4 - Enumeration

1. **How many users are there on the machine?**

The Get-LocalUser PowerShell cmdlet lists all the local users on a device/machine.

```powershell
Get-LocalUser
```

Answer: `5`

2. **Which local user does this SID(S-1-5-21-1394777289-3961777894-1791813945-501) belong to?**

Use Get-LocalUser and check all the parameters available:

```powershell
Get-LocalUser | Select *
```

Use Get-LocalUser and filter for SID:

```powershell
Get-LocalUser | select name, sid
```

Answer: `Guest`

3. **How many users have their password required values set to False?**

Use Get-LocalUser and filter for *passwordrequired*:

```powershell
Get-LocalUser | select name, sid
```

Answer: `4`

4. **How many local groups exist?**

The Get-LocalGroup cmdlet gets local security groups in Security Account Manager.

```powershell
Get-LocalGroup | measure
```

Answer: `24`

5. **What command did you use to get the IP address info?**

The Get-NetIPAddress cmdlet gets the IP address configuration, such as IPv4 addresses, IPv6 addresses and the IP interfaces with which addresses are associated.

```powershell
Get-NetIPAddress
```

6. **How many ports are listed as listening?**

The Get-NetTCPConnection cmdlet gets current TCP connections.

```powershell
Get-NetTCPConnection | Where-Object -Property State -eq Listen | measure
```

Answer: `20`

7. **What is the remote address of the local port listening on port 445?**

Review the output from the cmdlet used in question 6 above.

Answer: `::`

8. **How many patches have been applied?**

The Get-Hotfix cmdlet gets hotfixes, or updates, that are installed on the local computer or specified remote computers.

```powershell
Get-HotFix | measure
```

Answer: `20`

9. **When was the patch with ID KB4023834 installed?**

Used the Get-HotFix cmdlet and filtered for ID KB4023834:

```powershell
Get-HotFix -Id KB4023834
```

Answer: `6/15/2017 12:00:00 AM`

10. **Find the contents of a backup file.**

Search files with extension `.bak`:

```powershell
Get-Childitem –Path C:\ -Include *.bak* -File -Recurse -ErrorAction SilentlyContinue
```

Found a backup file called `passwords.bak.txt` locted in `C:\Program Files (x86)\Internet Explorer`. 

```powershell
Get-Content "C:\Program Files (x86)\Internet Explorer\passwords.bak.txt"
```

Answer: `backpassflag`

11. **Search for all files containing API_KEY**

Give the location of the files that contain the pattern *"API_KEY"*:

```powershell
Get-ChildItem C:\* -Recurse | Select-String "API_KEY" -List | Select Path
```

Identified file location that contains pattern: `C:\Users\Public\Music\config.xml`

```powershell
Get-Content "C:\Users\Public\Music\config.xml"
```

Answer: `API_KEY=fakekey123`

12. **What command do you do to list all the running processes?**

The Get-Process cmdlet gets the processes on a local or remote computer.

Answer: `Get-Process`

13. **What is the path of the scheduled task called new-sched-task?**

The Get-ScheduledTask cmdlet gets the task definition object of a scheduled task that is registered on a computer.

```powershell
Get-ScheduledTask -TaskName new-sched-task
```

Answer: `/`

14. **Who is the owner of the "C:\"?**

The Get-Acl cmdlet gets objects that represent the security descriptor of a file or resource.

```powershell
Get-Acl C:/
```

Answer: `NT SERVICE\TrustedInstaller`

## Task 5 - Basic Scripting Challenge

For this ask, we'll be using **PowerShell ISE** (which is the Powershell Text Editor). To show an example of this script, let's use a particular scenario. Given a list of port numbers, we want to use this list to see if the local port is listening. Open the `listening-ports.ps1` script on the Desktop using Powershell ISE. Powershell scripts usually have the `.ps1` file extension. 

The convention to create variables is used as:

```powershell
$variable_name = value
```

To iterate through the ports in the file, we use the following

```powershell
foreach($new_var in $existing_var){}
```

To run script, just call the script path using Powershell or click the green button on Powershell ISE.

Now that we've seen what a basic script looks like - it's time to write one of your own. The emails folder on the Desktop contains copies of the emails John, Martha and Mary have been sending to each other (and themselves). Answer the following questions with regards to these emails (try not to open the files and use a script to answer the questions). 

PowerShell Scripting Cheatsheet: https://learnxinyminutes.com/docs/powershell/

Solution Script: `emails-script.ps1`

1. **What file contains the password?**

Ans: `Doc3m`

2. **What is the password?**

Ans: `johnisalegend99`

3. **What files contains an HTTPS link?**

Ans: `Doc2Mary`

## Task 6 - Intermediate Scripting

Try writing a simple port scanner using Powershell. Here's the general approach to use: 

* Determine IP ranges to scan(in this case it will be localhost) and you can provide the input in any way you want
* Determine the port ranges to scan
* Determine the type of scan to run(in this case it will be a simple TCP Connect Scan)

Solution Script: `port-scanner.ps1`

Ans: `11`