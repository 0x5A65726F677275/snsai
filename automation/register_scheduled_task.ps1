#Requires -Version 5.1
<#
.SYNOPSIS
  Refuses to register the daily publish task while automation is halted.
#>

$TaskName = "SNS-AI-Instagram-Publish"
Write-Error "HALTED 2026-08-15: refusing to register $TaskName. See automation/DISABLED.md"
$existing = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($existing) {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
    Write-Host "Removed existing task: $TaskName"
}
exit 1
