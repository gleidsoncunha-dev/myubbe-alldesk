# Validação do servidor MyUbbe AllDesk 1.5.5

14/11/2026, America/Sao_Paulo. Destino `195.182.200.177`.

## Publicação e operação

- Deploy às 18:21 BRT: `PUBLICACAO_VERIFICADA MyUbbeAllDesk 1.5.5`.
- `/opt/myubbe-alldesk/current` → `releases/1.5.5`, COMMIT `d3075efce541a98ef3030a79a2413d83458026bc`.
- RustDesk Server OSS 1.1.16, digest `sha256:8ecdab65deb7c84652a626380e31d11a8f1fbafd97916d57f95c20628f943c00`.
- hbbs/hbbr em execução, zero reinícios; `unless-stopped` e Docker habilitado no boot.
- Limite de 256 MiB por serviço. Uso pontual ocioso: 1,492 MiB hbbs e 756 KiB hbbr; não é ensaio de capacidade/banda.
- Shared/data em 700 e chave privada em 600. Backup local de chaves e SQLite consistente antes do deploy. Nenhuma chave privada exportada.
- Apenas TCP 21115/21116/21117 e UDP 21116 publicados. Sem listeners no host em 21114/21118/21119.

## Sondas externas

Executadas deste Windows pela internet. Formato conferido contra
`rendezvous.proto`, `bytes_codec.rs` e `rustdesk-server/src/relay_server.rs`
da versão oficial 1.1.16.

| Verificação | Resultado |
| --- | --- |
| TCP 21115/21116/21117 | acessíveis |
| RegisterPeer UDP 21116, ID aleatório de teste | RegisterPeerResponse/request_pk recebido |
| TestNatRequest TCP 21115 e 21116 | TestNatResponse recebido nos dois |
| Duas conexões ao relay, UUID exclusivo e chave correta | pareadas |
| Payload sintético A → B e B → A | recebido integralmente |
| RequestRelay com chave incorreta | conexão rejeitada |
| OnlineRequest TCP 21115 para o ID Windows | OnlineResponse com bit online 0x80 |

Identificador transitório próprio; sem registrar chaves de outro computador,
iniciar sessão de desktop ou ler telas. A sonda valida UDP, NAT e relay,
mas não homologa vídeo, teclado ou clipboard.

## Cliente Windows e CRM

Cliente portátil 1.5.4 localizado em execução. Sem TCP estabelecido antes da
reinicialização. Encerrado, configurado com backup e reiniciado usando o mesmo
executável. Alteradas somente as opções host/relay/chave. Identidade, senhas,
permissões e consentimento preservados; acesso desassistido não habilitado.

Servidor registrou sua chave; perfil local confirmou
`keys_confirmed["195.182.200.177:21116"] = true`. Valores de host/relay/chave
coincidem com o perfil público distribuído.

O cliente também tenta `/api/sysinfo` da API Pro na porta 21114; o log registra
recusa porque essa API não integra o Server OSS. Registro nativo e relay foram
comprovados independentemente dessa API.

CRM após ativação: `/api/v1/health` HTTP 200, versão 1.98.31, healthy,
Supabase/Redis/WAHA ok. Sem alteração de serviço, banco, DNS, Caddy ou ambiente.

## Limites de homologação

Controle nativo de janelas Windows: pipe indisponível, erro 2. Conector Mac:
erro interno nas tentativas de listar projetos e consultar o binding. Sessão
visual automatizada no MacBook indisponível. O relatório local posterior
confirmou sessão real e vídeo, conforme a seção abaixo. CI, logs de sessão e
inspeção visual direta são evidências distintas; publicação não comprova vídeo.

## Atualização final

Por volta de 20:14 BRT, consulta externa de presença confirmou simultaneamente
`282548778=true` e `496264126=true`. O novo ID corresponde aos primeiros
dígitos visíveis na captura do Mac e foi depois confirmado pelo aplicativo no
relatório local. O VPS passou a ter dois registros. Serviços continuam
running, zero reinícios, versão de deploy 1.5.5. Windows em execução observado
em 1.5.4+72. CRM 1.98.31 healthy, Supabase/Redis/WAHA ok. TCP 21115/21116/21117
externos acessíveis. Isso comprova presença, não autenticação ou vídeo.

Release de pacotes 1.5.5 publicada às 19:21:43 BRT; CI desktop completa aprovada
às 20:26:20 BRT, com Windows x64/ARM64 e Mac Intel/ARM64. Resultado de build,
testes e metadados separado do teste real nos equipamentos. O titular pediu
instrução para o Codex local do VS Code: [prompt preparado](PROMPT_SUPORTE_MAC.md).

## Sessão real relatada pelo Codex local no Mac

O titular forneceu o relatório local: Monterey 12.7.6 Intel, aplicativo
1.5.4 em `/Applications/MyUbbeAllDesk.app`, ID 282548778 e perfil efetivo
`~/Library/Preferences/com.carriez.MyUbbeAllDesk/`. Host/relay/chave conferem;
API vazia. TCP acessível e respostas de registro UDP confirmadas nos logs,
com latência pontual de 22–27 ms.

Sessão direta e segura ao Windows 496264126, monitor 1920×1080, decodificador
H.265 iniciado e retomada do vídeo após reset de conexão às 20:58:43 BRT,
conforme o relatório recebido em 14/11/2026. Sessão e configurações preservadas;
nenhuma senha, identidade, permissão ou proteção foi alterada pelo agente local.

Avisos da API Pro 21114 permaneceram sem impedir a sessão. Não houve abertura
de porta ou ajuste de infraestrutura para silenciá-los. Acessibilidade bloqueou
a inspeção visual automatizada; mouse/teclado e funcionamento após reboot/logout
não foram explicitamente homologados. Acesso não assistido continua separado,
dependendo de configuração de senha permanente e serviço no Windows.
