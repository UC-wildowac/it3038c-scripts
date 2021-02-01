#$Hello = "Hello, Powershell!"
#Write-Host($Hello)
function getIP{
     (get-NetIPAddress).IPv4Address | Select-String "192"
}

Write-Host(getIP)
$IP = getIP
$Date = Get-Date
$Body = "This machine's IP is $IP. User is $env:username. Hostname is $hostname. PowerShell version $Get-Host. Today's date is $Date"

Send-MailMessage -To "wildowac@mail.uc.edu" -From "wildwildow@gmail.com" -Subject "IT3038c Windows SysInfo" -Body $Body -SmtpServer smtp.google.com -port 587 -UseSSL -Credential (Get-Credential)
