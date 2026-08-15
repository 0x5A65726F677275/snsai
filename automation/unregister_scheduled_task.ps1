#Requires -Version 5.1
# Remove the local Windows daily publish task if it exists.

$TaskName = "SNS-AI-Instagram-Publish"
$existing = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($existing) {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
    Write-Host "Removed: $TaskName"
} else {
    Write-Host "No task named $TaskName (already off)."
}
