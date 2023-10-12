# Define target directory for removal
$geckoDir = "$env:USERPROFILE\twitter-video-downloader\GeckoDriver"

# Function to remove directory
function RemoveDir([string]$dirPath) {
    if (Test-Path $dirPath) {
        Remove-Item -Path $dirPath -Recurse -Force
        Write-Host "Removed directory: $dirPath"
    } else {
        Write-Host "Directory $dirPath does not exist."
    }
}

# Remove GeckoDriver directory
RemoveDir $geckoDir

# Remove the geckodriver directory from PATH
$pathEnv = [Environment]::GetEnvironmentVariable("PATH", [EnvironmentVariableTarget]::User)
$newPath = ($pathEnv -split ";" | Where-Object { $_ -ne $geckoDir }) -join ";"
[Environment]::SetEnvironmentVariable("PATH", $newPath, [EnvironmentVariableTarget]::User)
Write-Host "Removed GeckoDriver directory from PATH."

# Uninstall facebook-downloader Python package
pip uninstall twitter-video-downloader -y

Write-Host "Cleanup complete."