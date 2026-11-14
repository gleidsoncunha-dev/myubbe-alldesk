# MyUbbe AllDesk — handoff

## Escopo e base

- Data: 14/11/2026, America/Sao_Paulo.
- Produto definido pelo titular: **MyUbbe AllDesk**.
- Origem: https://github.com/rustdesk/rustdesk.
- Base exata: `a89a82f911d9e1bfe742e79ccb2aeaaa3c950d20` (RustDesk 1.5.3).
- Fork: https://github.com/gleidsoncunha-dev/myubbe-alldesk.
- Pasta local: `C:\PROJETOS\rustdesk`.
- `upstream` aponta para o RustDesk; `origin` aponta para o fork MyUbbe.
- O `AGENTS.md` original foi lido e permanece aplicável.
- O usuário autorizou reutilizar a imagem da marca existente no CRM.

## Lote inicial — 1.5.4 / Flutter 1.5.4+72

Mantemos o esquema SemVer existente e incrementamos o patch do fork. A versão
1.5.4 identifica esta personalização, não uma versão oficial nova do RustDesk.
Cargo.toml, as entradas do aplicativo e do empacotador no Cargo.lock,
libs/portable/Cargo.toml e seu lockfile, pubspec.yaml, a versão do workflow e
os metadados RPM/Arch/AppImage foram sincronizados. Versões de dependências são
preservadas.

A inicialização do nome Windows usa `MyUbbeAllDesk`. O identificador não contém
espaços porque o projeto também o usa em URI, serviços, arquivos e registros.
Os metadados do produto usam **MyUbbe AllDesk**. O nome padrão é aplicado antes
da leitura da configuração de cliente; uma configuração personalizada existente
continua podendo definir seu próprio nome. Nenhum submódulo foi alterado.

O nome personalizado seleciona os caminhos de cliente personalizado já existentes
no RustDesk: configurações, serviço e instalação próprios e ausência da consulta
automática de atualização do cliente oficial. Não compartilhará automaticamente
a identidade/configuração de uma instalação RustDesk anterior. Um servidor
próprio e um canal próprio de atualização ainda precisam ser definidos.

### Origem das imagens

Fonte: `C:\PROJETOS\myubbe-crm\public\brand`, commit do CRM
`e1d46a3fb47a6b004001baa436eb18e80dac3e46`.

- `logo-myubbe-v2.png`: cópia integral para `res/icon.png` e
  `flutter/assets/icon.png`.
- `wordmark-on-light-myubbe-v2.png`: cópia integral para
  `flutter/assets/logo.png` e `flutter/assets/logo_light.png`.
- `wordmark-on-dark-myubbe-v2.png`: cópia integral para
  `flutter/assets/logo_dark.png`.
- Os ICOs de `res/icon.ico`, `res/tray-icon.ico` e
  `flutter/windows/runner/resources/app_icon.ico` são conversões da imagem
  quadrada original, em 16, 24, 32, 48, 64, 128 e 256 pixels.

Não foi reutilizada a arte com o sufixo CRM. Não há redesenho do símbolo nem
geração de uma nova marca. Os logotipos usam o carregamento claro/escuro já
existente no Flutter, sem modificar o layout ou a escala da interface.

### Superfície de alteração

- `src/common.rs`: um hook de inicialização, somente Windows, no início do
  carregamento de cliente; implementação isolada em `src/branding.rs`.
- `src/lib.rs`: declaração do módulo, somente Windows.
- `flutter/windows/runner/main.cpp`: fallback do título coerente com o nome
  retornado pelo núcleo.
- `flutter/windows/runner/Runner.rc`: nome e descrição do produto e marca
  responsável pela distribuição; copyright original preservado.
- `Cargo.toml` e `libs/portable/Cargo.toml`: metadados de produto Windows
  também no binário Rust e no empacotador portátil, com copyright preservado.
- Imagens: ícones e logotipos usados pelo carregamento existente.
- Demais alterações: versão, rastreamento dos PNGs e documentação.

Nenhuma alteração em captura, permissões, consentimento, autenticação, protocolo,
criptografia ou transferência de arquivos. Nome nativo e empacotamento de
Android, iOS, macOS e Linux ainda não foram personalizados integralmente.

## Validação e publicação

Validação local aprovada: `git diff --check`, leitura de TOML com `tomllib`,
coerência das versões, decodificação dos PNGs e de todas as sete resoluções de
cada ICO. As cópias PNG são idênticas aos arquivos do CRM, verificadas byte a
byte. Imagens originais e logotipo claro foram inspecionados visualmente.
A integridade do clone e do submódulo foi verificada com
`git fsck --connectivity-only`. Compilação e testes Rust/Flutter locais ainda
dependem dos SDKs e das ferramentas C++/LLVM/vcpkg, ausentes no PATH e nos locais
padrão conferidos. Python 3.14 com Pillow 12.2 está disponível fora do PATH.

CI e publicação: pendentes de acompanhamento após o push da branch
`feat/myubbe-branding`. Não foram criadas tags nem releases antes do build.

Não há binário MyUbbe compilado ou homologação visual/autenticada nesta etapa.
Não declarar um instalador publicado antes da conclusão do build e da release.

## Licença e próximos passos

Preservados `LICENCE`, avisos e autoria do RustDesk. A licença do código é
AGPL-3.0; distribuição comercial deve cumprir as obrigações aplicáveis, inclusive
fornecimento do código correspondente. Os ativos MyUbbe são reutilizados por
autorização do titular, sem presumir que tenham a mesma licença do código.

Fontes: https://github.com/rustdesk/rustdesk/blob/master/LICENCE e
https://rustdesk.com/docs/en/dev/build/windows/.

Antes de distribuição a clientes: concluir build Windows, inspecionar telas e
instalação, definir infraestrutura própria, configurar assinatura do instalador
e disponibilizar o código correspondente à versão distribuída. Não há uso nem
inclusão de certificados, credenciais ou configurações de produção do CRM.
