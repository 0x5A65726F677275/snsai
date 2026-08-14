#Requires -Version 5.1
# Daily SNS AI automation — runs even if .env missing (logs skip reason)

$ProjectRoot = "c:\Users\Dae Jin Kim\OneDrive\Pictures\sns_ai"
$ScriptPath = Join-Path $ProjectRoot "automation\daily_auto.py"
$Python = (Get-Command python -ErrorAction SilentlyContinue).Source

if (-not $Python) {
    Write-Error "Python not found"
    exit 1
}

& $Python $ScriptPath
exit $LASTEXITCODE
