# Instrução para o Codex local no Mac

Copie o bloco abaixo para uma conversa do Codex no VS Code do MacBook.
O trabalho usa as ferramentas locais do Mac; o conector remoto não é necessário.

```text
Configure e diagnostique o MyUbbe AllDesk neste MacBook Intel com macOS
Monterey 12.7.6. Confira também a versão real do sistema e a arquitetura.

Estado verificado em 14/11/2026:
- Servidor próprio funcionando em 195.182.200.177.
- Windows de destino, ID 496264126, confirmado ONLINE nesse servidor.
- TCP, UDP, NAT e relay testados externamente com sucesso.
- Inicialmente o Mac não apareceu registrado e informou "destino offline ou não existe".
- Atualização por volta de 20:14: os IDs 282548778 e 496264126 foram confirmados
  ONLINE no VPS ao mesmo tempo. Confira o ID real do Mac e o estado atual antes
  de editar. Se já conectar, preserve a configuração e registre o resultado.

Configuração correta:
Servidor ID: 195.182.200.177
Servidor Relay: 195.182.200.177
Chave pública: H5N5hffKtcU9fT+oW5I47nk2kS0P2ULAQCHsSaqrryw=
Servidor API: vazio

Escopo: diagnóstico e configuração do cliente neste Mac. Preserve identidade,
senhas, permissões e o acesso remoto existente. Preserve as proteções do macOS.

1. Identifique versão, caminho do aplicativo e processos/serviços em execução.
   Confira qual cópia está aberta: instalada ou dentro do DMG.
2. Teste TCP para o VPS nas portas 21115, 21116 e 21117.
3. Localize a configuração efetivamente usada pelo processo e pelo serviço.
   Um caminho provável é:
   ~/Library/Preferences/com.carriez.MyUbbeAllDesk/
   Confira também se o serviço usa outro perfil. Verifique os valores salvos,
   não apenas os campos que aparecem na interface.
4. Faça backup antes de editar. Aplique host, relay e chave no perfil efetivo,
   com API vazia e demais opções preservadas. Encerre somente o AllDesk se
   necessário, preservando qualquer sessão ativa, e reabra o aplicativo correto.
5. Confira os logs e comprove o registro no servidor próprio. Investigue UDP
   21116 por resposta do protocolo ou registro real: TCP sozinho não comprova UDP.
6. Tente conectar ao Windows 496264126. Deixe o usuário fornecer a autenticação;
   preserve as senhas atuais. Confirme a visualização e a reconexão, se possível.
7. Se for necessário atualizar, use o pacote Intel 1.5.5 publicado:
   https://github.com/gleidsoncunha-dev/myubbe-alldesk/releases/download/myubbe-v1.5.5/myubbe-alldesk-1.5.5-x86_64.dmg

Perfil importável na tela Configurações → Rede:
https://github.com/gleidsoncunha-dev/myubbe-alldesk/releases/download/myubbe-v1.5.5/myubbe-alldesk-server-config.txt

Conclua as correções locais possíveis. Caso uma permissão ou privilégio do macOS
exija intervenção do usuário, explique a ação exata necessária.

Relate ao terminar:
- versão e caminho do aplicativo;
- perfil realmente utilizado e servidor efetivo;
- resultado das portas e do registro;
- ID mostrado no Mac;
- resultado da sessão ou mensagem exata do erro restante.

Não exponha senhas, chaves privadas ou arquivos completos de configuração.
```
