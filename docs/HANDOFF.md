# MyUbbe AllDesk — handoff

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
- Smoke de release: versão e metadados do EXE e versão/nome/bundle ID do aplicativo Mac. Sem certificados, Mac recebe assinatura ad hoc de desenvolvimento e Windows fica sem assinatura Authenticode. Isso não equivale a assinatura comercial/notarização Apple.
- Compatibilidade Monterey: mínimo 12.0 no Intel e 12.3 no Apple Silicon, alinhando Xcode, CocoaPods, Rust, ambiente do job e triplets vcpkg de codecs. A compilação em um runner novo não é, por si, prova de execução em Monterey.
- `scripts/check_macos_compatibility.py` verifica arquitetura e mínimos declarados nos Mach-O do bundle com `lipo`/`vtool`, além do mínimo do Info.plist, contra 12.7.6. Registra binários sem mínimo explícito; não substitui abertura e teste no MacBook real.

### Superfície de regressão

Mudanças existentes estritamente relacionadas à marca: hook e declaração de módulo em `src/common.rs`/`src/lib.rs`; nomes e recursos Windows/CMake; metadados, ícone, produto e esquema Xcode; caminhos Windows/macOS em `build.py`; nomes e comandos de empacotamento no workflow reutilizado; seleção desktop no workflow de CI. Outras alterações são versões, imagens, rastreamento de PNG e documentação.

Captura, protocolo, permissões, consentimento, autenticação, criptografia e transferência de arquivos não foram modificados. Android/iOS/Linux e a interface Sciter de 32 bits não compõem a primeira distribuição MyUbbe.

## Validação e estado

- Local: `git diff --check`; leitura de TOML e versões; PNGs comparados byte a byte com o CRM; PNG/ICO/ICNS decodificados; sintaxe Python, YAML/depends e plist validados. Imagens originais e logotipo claro inspecionados.
- `actionlint 1.7.12`, obtido da release oficial com SHA256 conferido: workflows chamadores desktop/release sem achados. O workflow reutilizado contém dois achados herdados em Android universal (`matrix.job.arch` sem matriz) e Web (`if: False`); confirmados no upstream e preservados fora do escopo desktop.
- CI Linux do commit `d768cb89c`: **success**, incluindo build e testes Rust: https://github.com/gleidsoncunha-dev/myubbe-alldesk/actions/runs/43559553920. A rodada anterior `568e084a2` também passou.
- Na primeira rodada Flutter, Dart passou em Mac Intel e ARM64; ponte Flutter/Rust e auxiliares de janela Windows também passaram. Essa rodada antecede a inclusão da marca Mac e a renomeação dos binários; não valida o lote final.
- Bloqueio inicial do Flutter CI (`contents: write` requerido pelo workflow reutilizado) foi corrigido no job chamador, preservando o padrão global de permissões somente leitura. Repositório sem proteção de branch/checks obrigatórios configurados na consulta inicial.
- Commit/push iniciais: `d7b8cf608`, `568e084a2` e `d768cb89c`; PR em rascunho: https://github.com/gleidsoncunha-dev/myubbe-alldesk/pull/1.
- A revisão dos overrides Xcode encontrou bundle ID antigo nos três perfis do target; todos foram alinhados antes da publicação. A correção recebe nova rodada de CI, pois AppInfo.xcconfig sozinho não prevalecia sobre essas configurações.
- CI `52934ae83`: Windows x64, Windows ARM64 e Mac Apple Silicon passaram. Mac Intel e Linux perderam comunicação com os runners; foram reexecutados isoladamente. O alvo Monterey foi informado depois dessa rodada e exige validação da configuração explícita de deployment target.
- O conector GitHub retornou 403 no fork novo; a CLI já autenticada foi utilizada. GitHub Actions foi ativado no fork.
- Rodada `916c9b82b`: CI Linux aprovado em https://github.com/gleidsoncunha-dev/myubbe-alldesk/actions/runs/43601983142. Build Windows ARM64 aprovado (os testes Rust dessa arquitetura são omitidos pelo workflow herdado). Mac ARM64 passou build e testes Rust, mas o gate novo falhou pela ordem dos argumentos de `lipo`: o caminho precisa preceder `-verify_arch`, que aceita uma lista de arquiteturas. Chamada corrigida; exige nova execução do gate antes de merge/publicação. Windows x64 e Mac Intel ainda em execução nessa consulta.
- Roteiro de homologação do equipamento: [TESTE_MAC_WINDOWS.md](TESTE_MAC_WINDOWS.md). Não há pacote MyUbbe publicado nem teste de conexão MacBook → Windows 11 concluído.

Compilação/testes nativos locais dependem de SDKs Rust/Flutter e ferramentas C++/LLVM/vcpkg, ausentes do PATH e dos locais padrão conferidos. Python 3.14, Pillow 12.2 e PyYAML 6 estão disponíveis fora do PATH. Build macOS é executado nos runners Mac do GitHub; não foi inspecionado no MacBook do titular.

## Licença e continuação

Preservados `LICENCE`, autoria e copyright do RustDesk. Código sob AGPL-3.0; distribuição comercial deve cumprir as obrigações aplicáveis, inclusive fornecimento do código correspondente. Ativos MyUbbe reutilizados por autorização do titular, sem presumir que tenham a mesma licença do código. Não foram incluídos segredos, certificados ou configurações de produção do CRM.

Fontes: https://github.com/rustdesk/rustdesk/blob/master/LICENCE e https://rustdesk.com/docs/en/dev/build/windows/.

Depois do build: inspecionar os pacotes e a interface Windows; validar abertura/permissões no MacBook; testar a conexão real Mac → Windows; definir infraestrutura própria e assinatura comercial antes de distribuição a clientes.
