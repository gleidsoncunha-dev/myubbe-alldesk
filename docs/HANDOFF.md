# MyUbbe AllDesk — handoff

## Servidor próprio — 14/11/2026 — lote 1.5.5

Autorização nesta conversa: implementar tudo necessário para funcionar no VPS
do CRM. Endereço confirmado `195.182.200.177`; acesso pelo alias SSH existente.
Inventário inicial: 15.993 MiB totais, 11.876 MiB disponíveis, 163 GiB livres;
portas 21115–21119 desocupadas. CRM 1.98.31 saudável no domínio principal.

Nova infraestrutura independente em `/opt/myubbe-alldesk`: RustDesk Server OSS
1.1.16 fixado por digest, dados/chaves privados persistentes, limites e rotação
de logs. Apenas portas nativas publicadas. Chave gerada em contêiner sem rede,
antes da publicação; somente a pública é versionada. O DNS `vps.myubbe.com.br`
não existe publicamente; o cliente usa o IP confirmado. Nenhuma alteração DNS
ou proxy é necessária.

Cliente incrementado para 1.5.5 / Flutter 1.5.5+73, com lockfiles e metadados
sincronizados. Defaults de rede no módulo `branding.rs`, preservando opções
manuais e overrides assinados. Sem alteração em submódulos, protocolo, captura,
autenticação, senhas, permissões ou consentimento. Teste desktop compara o
perfil público de distribuição com as constantes e valida a chave de 32 bytes.
Scripts exportam o perfil no formato herdado, configuram clientes parados com
backup e publicam o servidor versionado. Documentação em `deploy/vps/README.md`.

Validação local aprovada: `git diff --check`, AST Python, YAML/TOML, versões
sincronizadas, formato de importação com ida/volta e chave pública de 32 bytes;
3/3 testes do configurador; parser PowerShell sem erros; actionlint 1.7.12 do
workflow de release; Compose validado pelo Docker real do VPS. Build/testes
nativos permanecem nos runners Windows/Mac. Novo workflow verifica Compose,
sintaxe Bash e testes do configurador em Linux.

Commit, CI, publicação e registro real: **em andamento**, ainda não
declarados concluídos. Controle nativo do Windows indisponível: pipe não
encontrado (erro 2). O conector do Mac falhou com erro interno ao listar
projetos; abertura e teste de tela no Mac não estão comprovados por ferramentas.

CI de configuração do servidor `43642250910`: **success**. Primeira tentativa
de deploy interrompida antes de iniciar serviços: `git archive` com autocrlf
herdado do Windows exportou Bash em CRLF. Wrapper corrigido para exportar com
`core.autocrlf=false` e regra LF explícita para os scripts do deploy. Correção
do mesmo lote ainda não publicado no VPS, mantendo 1.5.5. Tag dos clientes
continua apontando para `eb095db8f`; não houve retag nem alteração dos defaults.

Superfície de regressão: em runtime existente, somente `src/branding.rs` passa
a oferecer defaults de servidor aos clientes Windows/macOS. Workflow desktop
passa a publicar também o perfil importável e notas sobre o servidor; demais
arquivos existentes alterados são versão/metadados e documentação. Serviços e
dados do CRM não são alterados.

**Publicação VPS concluída:** `d3075efce`, às 18:21 BRT, marker
`PUBLICACAO_VERIFICADA MyUbbeAllDesk 1.5.5`. Sondas externas passaram em TCP,
UDP, NAT e relay bidirecional com payload sintético; chave incorreta rejeitada.
Cliente Windows 1.5.4 configurado com backup e reiniciado sem sessão TCP ativa;
registro real confirmado no servidor e no `keys_confirmed` local. Serviços
estáveis, zero reinícios, política de boot e permissões verificadas. CRM
1.98.31 continua healthy. [Evidências e limites](VALIDACAO_VPS_1.5.5.md).

CI servidor final `43642359914`: **success**. CI Linux `43642359812`:
**success**, build e testes workspace (212 testes no aplicativo, além das
outras crates). Release `43642253910`: em andamento. CI desktop `43642359975`
foi cancelada sob a suposição incorreta de duplicação integral e depois
**reativada**: a inspeção dos `if` mostrou que a release omite os testes
Rust/Dart quando `upload-artifact=true`. Aguardar a CI desktop específica para
esses testes; não se declara a tentativa cancelada aprovada. Execuções Linux/desktop
anteriores do commit `eb095db8f` canceladas por terem sido substituídas pelas
do commit de correção; não se declaram aprovadas nem substituem as atuais.
Release de instaladores continua em execução na tag original, sem retag.

O titular apresentou captura do Mac às 18:26 com o destino `496264126` offline.
Consulta externa de presença pelo protocolo `OnlineRequest` na porta 21115
confirmou esse Windows **online** no servidor próprio (bit de estado 0x80).
SQLite do VPS ainda contém somente o registro Windows: o Mac não está
registrado no mesmo servidor. Orientados os três campos de Rede para o Mac;
conexão visual ainda aguarda confirmação. O titular informou que tentaria
reconectar seu `codex-mcp`; listagem e consulta do binding continuaram falhando
com erro interno. Nenhum comando ou alteração foi executado no Mac.

## Escopo autorizado

- Data: 14/11/2026, America/Sao_Paulo.
- Produto: **MyUbbe AllDesk**. Marca nos clientes **Windows e Mac**, conforme confirmação do titular. Cenário inicial: MacBook acessando Windows 11.
- Ambiente confirmado: Windows x64 e MacBook Air Intel com macOS Monterey **12.7.6**. O arquivo do Mac desse ambiente é `x86_64`.
- Base: https://github.com/rustdesk/rustdesk, commit `a89a82f911d9e1bfe742e79ccb2aeaaa3c950d20` (RustDesk 1.5.3).
- Fork: https://github.com/gleidsoncunha-dev/myubbe-alldesk.
- Pasta: `C:\PROJETOS\myubbe-alldesk`. `origin` é o fork; `upstream` é RustDesk.
- O clone inicial em `rustdesk` foi movido, sem duplicar código. Histórico e submódulo foram conferidos novamente com `git fsck --connectivity-only` e `git submodule status`.
- O Windows bloqueou a renomeação direta. A origem ficou só com uma `.git` vazia. A revisão automática de aprovação rejeitou a remoção dessas pastas vazias com `blocked by policy`, sem motivo mais específico; elas foram preservadas.
- O `AGENTS.md` original foi lido e continua aplicável. Não há mudança em submódulos.

## Lote inicial — 1.5.4 / Flutter 1.5.4+72

Mantido SemVer, com incremento de patch do fork. Esta versão não representa uma nova versão oficial do RustDesk. Cargo, lockfiles do aplicativo/empacotador, Flutter, workflow, RPM/Arch/AppImage estão sincronizados; versões de dependências não foram alteradas.

O nome técnico é `MyUbbeAllDesk`, sem espaços porque o projeto o utiliza em serviços, URI, diretórios e arquivos. Nome de exibição e metadados: **MyUbbe AllDesk**. O módulo isolado `src/branding.rs` inicializa o nome padrão no carregamento de cliente Windows/macOS; configurações personalizadas assinadas continuam podendo definir outro nome.

O nome seleciona os caminhos de cliente personalizado existentes: configuração, serviço e instalação próprios e ausência da atualização automática do cliente oficial. Não migra automaticamente configurações/identidade de instalações RustDesk anteriores. Servidor e canal próprio de atualização ainda não foram definidos.

### Marca e imagens

Origem autorizada: `C:\PROJETOS\myubbe-crm\public\brand`, commit `e1d46a3fb47a6b004001baa436eb18e80dac3e46`.

- `logo-myubbe-v2.png`: cópias integrais para `res/icon.png`, `res/mac-icon.png` e `flutter/assets/icon.png`.
- `wordmark-on-light-myubbe-v2.png`: cópias integrais para `flutter/assets/logo.png` e `logo_light.png`.
- `wordmark-on-dark-myubbe-v2.png`: cópia integral para `flutter/assets/logo_dark.png`.
- ICOs de Windows/bandeja: conversão da imagem quadrada original em 16, 24, 32, 48, 64, 128 e 256 pixels.
- `flutter/macos/Runner/AppIcon.icns`: conversão da mesma imagem para o ícone macOS, com oito representações decodificadas na verificação.

Não foi usada a arte com o sufixo CRM nem redesenhado o símbolo. Os logotipos claro/escuro usam o carregador já existente. Layout e escala visual foram preservados.

### Identidade e empacotamento

- Windows Flutter: `MyUbbeAllDesk.exe`; recursos de versão, ícone, nome e descrição atualizados. O payload portátil usa o mesmo nome, separando também o diretório temporário do RustDesk oficial.
- MSI: gerador recebe `--app-name MyUbbeAllDesk --manufacturer MyUbbe`, alinhando produto, serviço e registro. O arquivo de licença original é restaurado byte a byte após o pré-processamento, pois o script herdado substitui autoria ao trocar a marca.
- Mac: `MyUbbeAllDesk.app` / executável `MyUbbeAllDesk`, bundle `com.myubbe.alldesk`, URL `myubbealldesk`. O módulo Swift conserva `RustDesk` para manter as classes declaradas no XIB; isso é um nome interno.
- Os três perfis do target Xcode também usam `com.myubbe.alldesk`, pois sobrescrevem AppInfo.xcconfig. O identificador público de equipe Apple herdado foi removido desses perfis; assinatura de desenvolvimento ad hoc permanece, sem presumir uma conta/certificado da MyUbbe.
- `build.py`, esquema/produto Xcode e workflow usam os caminhos dos novos binários.
- Novo `.github/workflows/myubbe-desktop.yml`: release de teste para Windows x64/ARM64 e Mac Intel/Apple Silicon, acionada por tags `myubbe-v*`. Valida tag/Cargo/Flutter/workflow antes do build. Reutiliza o build com `desktop-only: true`; não publica Android/iOS/Linux nem templates comerciais de personalização.
- Publicação em duas etapas: todos os arquivos são enviados a um rascunho (`draft-release: true`); somente após o sucesso do build completo e a presença dos quatro pacotes Windows, dois DMGs e SBOM, um job final publica a pré-release. A opção de rascunho é desativada por padrão no workflow reutilizado, preservando os demais chamadores.
- CI desktop continua compilando e testando Windows/macOS. CI Linux básico é mantido. Nenhum check obrigatório foi removido nem ignorado para merge.
- Os workflows herdados nightly/tag/F-Droid e o atualizador semanal de certificados ficam restritos a `rustdesk/rustdesk`. No fork, publicação usa somente o fluxo MyUbbe desktop; o atualizador herdado, que contém force-push, não pode executar aqui. Consulta inicial após o merge só listou CI, build reutilizado e release MyUbbe registrados; a restrição também fica explícita no código para futuras ativações.
- Smoke de release: versão e metadados do EXE e versão/nome/bundle ID do aplicativo Mac. Sem certificados, Mac recebe assinatura ad hoc de desenvolvimento e Windows fica sem assinatura Authenticode. Isso não equivale a assinatura comercial/notarização Apple.
- Compatibilidade Monterey: mínimo 12.0 no Intel e 12.3 no Apple Silicon, alinhando Xcode, CocoaPods, Rust, ambiente do job e triplets vcpkg de codecs. A compilação em um runner novo não é, por si, prova de execução em Monterey.
- `scripts/check_macos_compatibility.py` verifica arquitetura e mínimos declarados nos Mach-O do bundle com `lipo`/`vtool`, além do mínimo do Info.plist, contra 12.7.6. Registra binários sem mínimo explícito; não substitui abertura e teste no MacBook real.

### Superfície de regressão

Mudanças existentes estritamente relacionadas à marca: hook e declaração de módulo em `src/common.rs`/`src/lib.rs`; nomes e recursos Windows/CMake; metadados, ícone, produto e esquema Xcode; caminhos Windows/macOS em `build.py`; nomes e comandos de empacotamento no workflow reutilizado; seleção desktop no workflow de CI. Outras alterações são versões, imagens, rastreamento de PNG e documentação.

Captura, protocolo, permissões, consentimento, autenticação, criptografia e transferência de arquivos não foram modificados. Android/iOS/Linux e a interface Sciter de 32 bits não compõem a primeira distribuição MyUbbe.

## Validação e estado

- Local: `git diff --check`; leitura de TOML e versões; PNGs comparados byte a byte com o CRM; PNG/ICO/ICNS decodificados; sintaxe Python, YAML/depends e plist validados. Imagens originais e logotipo claro inspecionados.
- `actionlint 1.7.12`, obtido da release oficial com SHA256 conferido: workflows chamadores desktop/release e os quatro workflows herdados com restrição de repositório sem achados. O workflow reutilizado contém dois achados herdados em Android universal (`matrix.job.arch` sem matriz) e Web (`if: False`); confirmados no upstream e preservados fora do escopo desktop.

### Resultado aprovado — commit 2361f1cc1

- [CI Linux](https://github.com/gleidsoncunha-dev/myubbe-alldesk/actions/runs/43606735765): **success**, build e testes Rust.
- [CI desktop](https://github.com/gleidsoncunha-dev/myubbe-alldesk/actions/runs/43606735893): **success**, Windows x64/ARM64 e Mac Intel/ARM64. Windows x64: 257 testes do aplicativo e 2 de clipboard; Mac ARM64: 259 e 22; testes Dart nas duas arquiteturas Mac. O workflow herdado omite Rust tests em Windows ARM64 e Mac Intel.
- Gate macOS: 22 Mach-O em cada arquitetura, incluindo aplicativo, serviço e frameworks. Intel usa mínimo 12.0; ARM64 usa 12.3; nenhum mínimo declarado excede 12.7.6. Versão, nome e bundle ID também passaram. Isso não homologa execução no MacBook físico.
- [PR 1](https://github.com/gleidsoncunha-dev/myubbe-alldesk/pull/1) integrada em `a4f565a8e53fb9e7f9faa50a8c6e0d4f6736002d`, após todos os checks terminarem. Conferido o head exato no merge, sem override administrativo. Branch sem checks obrigatórios adicionais configurados na consulta; nenhum check foi ignorado.
- `master` local acompanha `origin/master`. Histórico preservado, push e merge sem force.
- Inspeção de logs por navegador indisponível: host do navegador e canal nativo de apps não disponíveis nesta sessão. Acompanhamento por CLI/API; nenhuma homologação visual/autenticada do produto foi realizada.
- Publicação dos instaladores: **concluída**, como pré-release de teste 1.5.4. Evidências e limites abaixo.

### Histórico das rodadas anteriores

- CI Linux do commit `d768cb89c`: **success**, incluindo build e testes Rust: https://github.com/gleidsoncunha-dev/myubbe-alldesk/actions/runs/43559553920. A rodada anterior `568e084a2` também passou.
- Na primeira rodada Flutter, Dart passou em Mac Intel e ARM64; ponte Flutter/Rust e auxiliares de janela Windows também passaram. Essa rodada antecede a inclusão da marca Mac e a renomeação dos binários; não valida o lote final.
- Bloqueio inicial do Flutter CI (`contents: write` requerido pelo workflow reutilizado) foi corrigido no job chamador, preservando o padrão global de permissões somente leitura. Repositório sem proteção de branch/checks obrigatórios configurados na consulta inicial.
- Commit/push iniciais: `d7b8cf608`, `568e084a2` e `d768cb89c`; PR em rascunho: https://github.com/gleidsoncunha-dev/myubbe-alldesk/pull/1.
- A revisão dos overrides Xcode encontrou bundle ID antigo nos três perfis do target; todos foram alinhados antes da publicação. A correção recebe nova rodada de CI, pois AppInfo.xcconfig sozinho não prevalecia sobre essas configurações.
- CI `52934ae83`: Windows x64, Windows ARM64 e Mac Apple Silicon passaram. Mac Intel e Linux perderam comunicação com os runners; foram reexecutados isoladamente. O alvo Monterey foi informado depois dessa rodada e exige validação da configuração explícita de deployment target.
- O conector GitHub retornou 403 no fork novo; a CLI já autenticada foi utilizada. GitHub Actions foi ativado no fork.
- Rodada `916c9b82b`: CI Linux aprovado em https://github.com/gleidsoncunha-dev/myubbe-alldesk/actions/runs/43601983142. Build Windows ARM64 aprovado (os testes Rust dessa arquitetura são omitidos pelo workflow herdado). Mac ARM64 passou build e testes Rust, mas o gate novo falhou pela ordem dos argumentos de `lipo`: o caminho precisa preceder `-verify_arch`, que aceita uma lista de arquiteturas. Chamada corrigida; exige nova execução do gate antes de merge/publicação. Windows x64 e Mac Intel ainda em execução nessa consulta.
- Roteiro de homologação do equipamento: [TESTE_MAC_WINDOWS.md](TESTE_MAC_WINDOWS.md). Naquela consulta ainda não havia pacote MyUbbe publicado; o teste de conexão MacBook → Windows 11 continua pendente.

Compilação/testes nativos locais dependem de SDKs Rust/Flutter e ferramentas C++/LLVM/vcpkg, ausentes do PATH e dos locais padrão conferidos. Python 3.14, Pillow 12.2 e PyYAML 6 estão disponíveis fora do PATH. Build macOS é executado nos runners Mac do GitHub; não foi inspecionado no MacBook do titular.

## Publicação concluída e smoke dos arquivos

- [Release MyUbbe AllDesk 1.5.4](https://github.com/gleidsoncunha-dev/myubbe-alldesk/releases/tag/myubbe-v1.5.4), publicada em **14/11/2026 às 14:14:40, America/Sao_Paulo**. API confirma `draft: false`, `prerelease: true`, seis pacotes desktop e SBOM. Tag `myubbe-v1.5.4` aponta para `9165acdcec5ba9b2483a6657980d5a99f0e90dc9`; não foi retaggeada.
- [Workflow de publicação](https://github.com/gleidsoncunha-dev/myubbe-alldesk/actions/runs/43614754750): **success**. Windows x64/ARM64 passaram verificação de versão/produto e geração de MSI; Mac Intel/ARM64 passaram verificação do bundle, assinatura ad hoc com verificação e geração de DMG. O job final só promoveu o rascunho depois dos sete arquivos esperados.
- CI após o merge também terminou **success**: [Linux](https://github.com/gleidsoncunha-dev/myubbe-alldesk/actions/runs/43614526958) e [desktop](https://github.com/gleidsoncunha-dev/myubbe-alldesk/actions/runs/43614527076). Os ajustes posteriores de automação não alteraram o aplicativo e passaram em actionlint.
- Os quatro workflows herdados foram também desativados via API no próprio fork, com estado `disabled_manually`: nightly, tag, F-Droid e update-webpki-roots. CI, build reutilizado e release MyUbbe permanecem ativos.
- Destino público conferido por página da release e API; links diretos de Mac Intel DMG e Windows x64 EXE responderam HTTP 200 sem autenticação.
- Smoke local somente de leitura dos arquivos Windows baixados: tamanhos e SHA256 coincidem com os digests da API da release; cabeçalho PE x64; produto `MyUbbe AllDesk`, versão `1.5.4`; Authenticode `NotSigned`, conforme o perfil de desenvolvimento. Ícone extraído do EXE publicado inspecionado e confirmado como MyUbbe.
- MSI aberto com Windows Installer em modo 0 (leitura), sem instalar: `ProductName=MyUbbeAllDesk`, `Manufacturer=MyUbbe`, `ProductVersion=1.5.4.29911267`, `UpgradeCode={2D68606F-3A5E-57AB-BFC4-299DE98249AE}`. O sufixo MSI é a revisão automática do gerador herdado; a versão base permanece 1.5.4. O UpgradeCode difere do RustDesk original.

| Arquivo Windows x64 | SHA256 conferido no download |
| --- | --- |
| EXE | `eece2d8c79ab55b4ce4591cc2e516c8e50b213d9b98a2f92a749ec3d444259cb` |
| MSI | `184250d31876abdcadadfda7523d8100b4f75abcee3e4c1b540b197f716e1189` |

Esse smoke não executou o aplicativo nem instalou serviço. Abertura no Monterey físico, inspeção completa da interface e sessão real Mac → Windows continuam **pendentes**; seguir [TESTE_MAC_WINDOWS.md](TESTE_MAC_WINDOWS.md). Windows não tem assinatura comercial; Mac tem assinatura ad hoc, sem notarização. Servidor próprio e canal de atualização seguem fora desta primeira distribuição de teste.

O commit documental de fechamento mantém 1.5.4, pois registra o mesmo lote já versionado/publicado; não muda código nem artefatos da tag.

## Licença e continuação

Preservados `LICENCE`, autoria e copyright do RustDesk. Código sob AGPL-3.0; distribuição comercial deve cumprir as obrigações aplicáveis, inclusive fornecimento do código correspondente. Ativos MyUbbe reutilizados por autorização do titular, sem presumir que tenham a mesma licença do código. Não foram incluídos segredos, certificados ou configurações de produção do CRM.

Fontes: https://github.com/rustdesk/rustdesk/blob/master/LICENCE e https://rustdesk.com/docs/en/dev/build/windows/.

Próxima etapa: abrir os clientes publicados nos equipamentos, conferir a interface Windows, validar abertura/permissões no MacBook e testar uma sessão real Mac → Windows. Infraestrutura própria e assinatura comercial ficam para a preparação de distribuição a clientes.
