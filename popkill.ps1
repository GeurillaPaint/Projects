Write-Host "
Script is now running! Popups will be sacked every 30 minutes.

You can view poplog.txt to see a log of pop up start times.

Please feel free to minimize this window. Closing this window will end the script...


"


Write-Host "

"
$ErrorActionPreference= 'silentlycontinue'
do{

$TitleToKill = "posmon.exe"
	$p = get-process | where-object {$_.MainWindowTitle -eq $TitleToKill}
	Stop-Process -InputObject $p
    Get-Process | Where-Object {$_.HasExited} |select name,starttime| Out-File -FilePath .\poplog.txt -Append
    start-sleep -Seconds 30
}until($infinity)
