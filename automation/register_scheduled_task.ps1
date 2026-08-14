#Requires -Version 5.1
<#
.SYNOPSIS
  Register Windows Task Scheduler job for daily Instagram auto-publish.

.NOTES
  PC must be ON at publish time for this to run.
  For cloud scheduling without PC, see SETUP.ko.md Option B (Cursor Automation).
#>

param(
    [string]$PublishTime = "09:00",
    [string]$ProjectRoot = "c:\Users\Dae Jin Kim\OneDrive\Pictures\sns_ai"
)

$TaskName = "SNS-AI-Instagram-Publish"
$Python = (Get-Command python -ErrorAction SilentlyContinue).Source
if (-not $Python) {
    $Python = (Get-Command py -ErrorAction SilentlyContinue).Source
    if ($Python) { $Python = "$Python -3" }
}
if (-not $Python) {
    Write-Error "Python not found. Install Python 3.11+ first."
    exit 1
}

$ScriptPath = Join-Path $ProjectRoot "automation\daily_auto.py"
$Action = New-ScheduledTaskAction -Execute $Python -Argument "`"$ScriptPath`"" -WorkingDirectory (Join-Path $ProjectRoot "automation")

$Hour, $Minute = $PublishTime.Split(":")
$Trigger = New-ScheduledTaskTrigger -Daily -At "$Hour`:$Minute"

$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Settings $Settings -Force

Write-Host "Registered: $TaskName daily at $PublishTime"
Write-Host "Test now: cd automation && python publish_due.py"
