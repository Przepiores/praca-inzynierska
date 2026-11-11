# Aktualizacja pracy na komputerze: git pull + kopia najnowszego PDF do Downloads.
# Uruchomienie: powershell -ExecutionPolicy Bypass -File W:\VAULT\Inzynierka\latex\synchronizuj.ps1
$repo = $PSScriptRoot
git -C $repo pull --ff-only
$data = (git -C $repo log -1 --format=%cs -- pdf/Praca_inzynierska.pdf)
$cel  = Join-Path $env:USERPROFILE "Downloads\Praca_inzynierska_$data.pdf"
Copy-Item (Join-Path $repo "pdf\Praca_inzynierska.pdf") $cel -Force
Write-Host "Zapisano: $cel"
$prom = Join-Path $repo "pdf\Praca_inzynierska_promotor.pdf"
if (Test-Path $prom) {
  $celP = Join-Path $env:USERPROFILE "Downloads\Praca_inzynierska_promotor_$data.pdf"
  Copy-Item $prom $celP -Force
  Write-Host "Zapisano: $celP"
}
