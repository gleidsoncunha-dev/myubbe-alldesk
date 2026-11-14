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
erro interno nas duas tentativas de listar projetos. Configuração e sessão
visual no MacBook ainda não comprovadas. Perfil importável e guia preparados.
Não se declara teste real Mac → Windows concluído. CI dos pacotes tem estado
próprio no handoff; publicação do servidor não equivale à publicação dos DMGs.
