$Name = "CanonicalGroupLimited.Ubuntu20.04onWindows"
if(Get-AppxPackage -Name $Name){
Write-Host "INSTALLED"
}
else{
Write-Host "NOT INSTALLED!!!"
}