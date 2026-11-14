# MyUbbe AllDesk no VPS

Versão do lote: **1.5.5**. Destino: `195.182.200.177`, o VPS do CRM.
O serviço usa RustDesk Server OSS **1.1.16**, fixado pelo digest em `compose.yaml`.
O endereço IP evita depender de um novo registro DNS. Não existe painel Pro.

Somente TCP 21115/21116/21117 e UDP 21116 são publicados. WebSocket
21118/21119 e API 21114 não são publicados. O Compose usa rede e contêineres
próprios; não usa os volumes, bancos, credenciais ou o proxy dos demais produtos.
Limites por serviço: 256 MiB, uma CPU e 128 processos; logs limitados a 30 MiB.
Os dois serviços exigem a chave pública configurada (`-k _`).

Dados persistentes: `/opt/myubbe-alldesk/shared/data`. A chave privada fica
somente no VPS, com permissão 600 e diretório 700. A chave pública está em
`deploy/client-config.json` e nos novos clientes. Nunca substituir a chave
privada ao atualizar. Os backups locais feitos antes de cada deploy conservam
as chaves e uma cópia consistente do SQLite. Backup externo requer destino
próprio; estas cópias locais permitem reversão, mas não cobrem perda do VPS.

## Publicação e operação

Após validação, commit e push, com checkout limpo:

```powershell
pwsh -NoProfile -File deploy/vps/publicar.ps1
```

O deploy usa `/opt/myubbe-alldesk/releases/1.5.5`, verifica a chave contra o
perfil dos clientes, preserva backup, sobe somente seu próprio Compose e testa
as três portas TCP antes de apontar `current`. Repetir o mesmo commit é seguro;
um commit diferente na mesma versão é recusado. A primeira chave desta
instalação foi gerada previamente em contêiner sem acesso à rede. Instalações
novas devem criar sua própria identidade e atualizar o perfil correspondente.

```bash
cd /opt/myubbe-alldesk/current
docker compose -f deploy/vps/compose.yaml ps
docker compose -f deploy/vps/compose.yaml logs --tail 50
python3 scripts/check_server.py --host 127.0.0.1
```

Reversão: usar o Compose da release anterior com os mesmos dados persistentes,
verificar as portas e reapontar `current` somente após sucesso. Na primeira
instalação, `docker compose stop` nessa pasta interrompe somente o AllDesk.
Não usar `down -v`, não apagar dados e não restaurar o SQLite com serviços ativos.
O `restart: unless-stopped` recupera os serviços após reboot. `running` no
Docker não substitui as sondas de rede e um teste real de sessão.

## Configurar Mac e Windows

Os instaladores **1.5.5** têm endereço e chave como valores padrão; opções
manuais anteriores continuam prevalecendo. Clientes **1.5.4** podem usar este
servidor sem reinstalação: Configurações → Rede → Servidor ID/Relay.

| Campo | Valor |
| --- | --- |
| Servidor ID | `195.182.200.177` |
| Servidor Relay | `195.182.200.177` |
| Chave | `H5N5hffKtcU9fT+oW5I47nk2kS0P2ULAQCHsSaqrryw=` |
| Servidor API | vazio |

Nos dois computadores, também é possível importar o texto gerado por
`python scripts/export_server_config.py` no importador de Rede, ou usar
`myubbe-alldesk-server-config.txt` da release. A chave é pública; ela não é
senha de acesso remoto. As senhas, o consentimento e as permissões dos clientes
continuam necessários. Não habilitar acesso desassistido como parte do setup.

Para configurar o perfil do usuário por arquivo, encerrar o AllDesk e executar
`python scripts/configure_client.py` (Python 3.11+). O script faz backup e
altera apenas as três opções de servidor, preservando a identidade e as demais
configurações. Serviço instalado possui perfil próprio; nesse caso usar a tela
Rede ou o `--config` do aplicativo instalado com privilégios administrativos.

Sonda externa: `python scripts/check_server.py`. Conectividade TCP não comprova
UDP, registro criptográfico ou sessão. Conferir registro real no log do cliente,
depois executar o roteiro `docs/TESTE_MAC_WINDOWS.md`, inclusive reconexão.

Referências oficiais: [Docker](https://rustdesk.com/docs/en/self-host/rustdesk-server-oss/docker/)
e [configuração dos clientes](https://rustdesk.com/docs/en/self-host/client-configuration/).
