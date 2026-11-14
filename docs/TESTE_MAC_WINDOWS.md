# Primeiro teste — Mac Intel → Windows 11

Ambiente alvo: MacBook Intel com macOS Monterey 12.7.6 e Windows 11 x64.
Este roteiro descreve uma validação manual; sua execução ainda está pendente.

## Arquivos

Lote atual: **1.5.5**, com servidor próprio e configuração padrão integrada.
Conferir no [handoff](HANDOFF.md) se a publicação dos novos pacotes já terminou;
os links abaixo ficam disponíveis somente após o sucesso do workflow.

| Computador | Arquivo da release MyUbbe |
| --- | --- |
| Windows 11 x64 | [myubbe-alldesk-1.5.5-x86_64.exe](https://github.com/gleidsoncunha-dev/myubbe-alldesk/releases/download/myubbe-v1.5.5/myubbe-alldesk-1.5.5-x86_64.exe), primeiro teste portátil |
| Mac Intel | [myubbe-alldesk-1.5.5-x86_64.dmg](https://github.com/gleidsoncunha-dev/myubbe-alldesk/releases/download/myubbe-v1.5.5/myubbe-alldesk-1.5.5-x86_64.dmg) |

Os arquivos `aarch64` correspondem a outra arquitetura. A release deve estar
publicada, com o build completo aprovado, antes de iniciar este roteiro.

## Verificação

1. Mantenha sua sessão atual de acesso ao Windows aberta durante o teste.
2. Abra o MyUbbe AllDesk portátil no Windows e confira nome, ícone e versão.
3. Abra o cliente Intel no Mac e confira os mesmos elementos no Monterey.
   Os dois devem usar `195.182.200.177` como servidor ID/Relay e a chave do
   [guia de configuração](../deploy/vps/README.md). A versão 1.5.5 fornece
   esses defaults; ajustes manuais anteriores prevalecem. Na 1.5.4, importar
   o perfil ou preencher os campos de Rede antes de conectar. Servidor API vazio.
4. No Mac, informe o ID mostrado pelo **MyUbbe AllDesk do Windows** e use a
   autenticação apresentada pelo aplicativo. Cada instalação tem sua identidade
   e configuração próprias; o ID da instalação RustDesk anterior pode diferir.
5. Confirme a visualização do Windows, movimento do ponteiro e entrada de texto
   em um documento de teste. Encerre a conexão e confirme que consegue reconectar.
6. Registre versão, abertura no Monterey, resultado da conexão e eventual mensagem
   de erro. A instalação do serviço Windows pode ser avaliada depois desse teste.

## Estado dos pacotes

Os primeiros pacotes são de desenvolvimento: Windows sem assinatura comercial e
Mac com assinatura ad hoc, sem notarização Apple. Caso o sistema impeça a
abertura, registre a mensagem antes de alterar configurações de segurança.

O gate de build confere arquitetura e versões mínimas declaradas nos binários.
Somente este teste no MacBook confirma o comportamento no equipamento real.
