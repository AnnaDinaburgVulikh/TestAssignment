param(
    [string[]]$ServiceNames
)

function Check-ServiceStatus {
    param(
        [string]$ServiceName
    )

    $serviceStatus = Get-Service -Name $ServiceName -ErrorAction SilentlyContinue

    # Check if the service is found
    if ($serviceStatus) {
        # Check if the service is running
        if ($serviceStatus.Status -ne "Running") {
            # Send an alert for critical services
            if ($ServiceName -eq "Dhcp") {
                Write-Host "Alert: Critical service '$($serviceStatus.DisplayName)' is stopped." -ForegroundColor Red
            } else {
                Write-Host "Service '$($serviceStatus.DisplayName)' is stopped."
            }
        } else {
            Write-Host "Service '$($serviceStatus.DisplayName)' is running."
        }
    } else {
        Write-Host "Service '$ServiceName' not found."
    }
}

foreach ($ServiceName in $ServiceNames) {
    Check-ServiceStatus -ServiceName $ServiceName
}