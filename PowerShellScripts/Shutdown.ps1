$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
$headers.Add("Authorization", "Bearer [your_script_here]")
$headers.Add("Content-Type", "application/json")

$body = "{`"state`": `"Shutdown`"}"

#echo $body

$response = Invoke-RestMethod 'http://192.168.68.121:8123/api/states/sensor.teams_raw' -Method 'POST' -Headers $headers -Body $body
