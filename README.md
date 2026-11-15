# AllDesk

Cliente de acesso remoto da MyUbbe para Windows e macOS, com identidade visual
MyUbbe, servidor próprio e interface em vários idiomas.

Versão do cliente: **1.5.6**. [Baixar instaladores](https://github.com/gleidsoncunha-dev/myubbe-alldesk/releases).
Os pacotes são publicados como pré-releases de teste: EXE e MSI para Windows
x64/ARM64 e DMG para Mac Intel/Apple Silicon.

O cliente Intel requer macOS Monterey 12.0 ou posterior; Apple Silicon, 12.3
ou posterior. Windows permanece sem assinatura comercial; Mac usa assinatura
ad hoc, sem notarização.

- [Estado da entrega e validações](docs/HANDOFF.md)
- [Servidor próprio e configuração de rede](deploy/vps/README.md)
- [Teste Mac → Windows](docs/TESTE_MAC_WINDOWS.md)
- [Marca e referências técnicas preservadas](docs/MARCA.md)
- [Informações sobre conexões e privacidade](docs/PRIVACIDADE.md)
- [Suporte e relatos de problemas](https://github.com/gleidsoncunha-dev/myubbe-alldesk/issues)

## Compilação

Os workflows [CI Linux](.github/workflows/ci.yml),
[CI desktop](.github/workflows/flutter-ci.yml) e
[publicação desktop](.github/workflows/myubbe-desktop.yml) registram as
ferramentas, dependências, testes e comandos utilizados nesta distribuição.
Tags `myubbe-v<VERSÃO>` iniciam a publicação desktop em rascunho; a release só
é publicada depois da conclusão dos builds e da conferência dos arquivos.

O build nativo requer Rust, Flutter, ferramentas C/C++ e vcpkg. Instruções
técnicas da base: [Windows](https://rustdesk.com/docs/en/dev/build/windows/)
e [macOS](https://rustdesk.com/docs/en/dev/build/osx/).

## Estrutura

- `src/`: cliente Rust, sessões, serviços e integração com o sistema.
- `flutter/`: interface e projetos nativos.
- `libs/hbb_common/`: submódulo compartilhado com o servidor.
- `libs/base/`: configurações e recursos exclusivos do cliente.
- `libs/scrap/`, `libs/enigo/`, `libs/clipboard/`: captura, entrada e clipboard.
- `deploy/`: perfil público do cliente e operação do servidor próprio.
- `scripts/`: validações e configuração dos clientes.

## Origem e licença

O AllDesk deriva do [RustDesk 1.5.3](https://github.com/rustdesk/rustdesk).
O código permanece sob a [AGPL-3.0](LICENCE), com os avisos de autoria e
copyright originais preservados. Os ativos MyUbbe são usados por autorização
do titular. O nome exibido do produto é AllDesk; nomes técnicos necessários
à compatibilidade estão descritos no guia de marca.
