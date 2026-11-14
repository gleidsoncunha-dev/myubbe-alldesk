param([string]$SshHost = 'contabil-finance-vps')
$ErrorActionPreference = 'Stop'
if ($SshHost -notmatch '^[A-Za-z0-9_.-]+$') { throw 'Alias SSH invalido' }
$root = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
if (git -C $root status --porcelain) { throw 'Checkout deve estar limpo e versionado' }
$match = [regex]::Match((Get-Content (Join-Path $root 'Cargo.toml') -Raw), '(?m)^version = "(\d+\.\d+\.\d+)"')
if (!$match.Success) { throw 'Versao invalida' }
$version = $match.Groups[1].Value
$sha = (git -C $root rev-parse HEAD).Trim()
$archive = Join-Path ([IO.Path]::GetTempPath()) "myubbe-alldesk-$version-$sha.tar"
$destination = "/opt/myubbe-alldesk/releases/$version"
try {
    git -c core.autocrlf=false -C $root archive --format=tar --output=$archive HEAD Cargo.toml deploy scripts
    if ($LASTEXITCODE -ne 0) { throw 'Falha ao gerar arquivo versionado' }
    ssh -o BatchMode=yes $SshHost "install -d -m 755 $destination; test ! -f $destination/COMMIT || test `"`$(cat $destination/COMMIT)`" = '$sha'"
    if ($LASTEXITCODE -ne 0) { throw 'Destino ja contem outro commit' }
    scp -q $archive "${SshHost}:$destination/source.tar"
    if ($LASTEXITCODE -ne 0) { throw 'Falha no envio' }
    ssh -o BatchMode=yes $SshHost "set -eu; cd $destination; tar -xf source.tar; printf '%s' '$sha' > COMMIT; bash deploy/vps/publish.sh"
    if ($LASTEXITCODE -ne 0) { throw 'Publicacao nao confirmada' }
} finally {
    if (Test-Path -LiteralPath $archive) { Remove-Item -LiteralPath $archive }
}
