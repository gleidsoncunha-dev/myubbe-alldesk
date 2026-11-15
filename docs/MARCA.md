# Marca AllDesk

Nome exibido: **AllDesk**, produto da MyUbbe. Identidade visual: os ativos
MyUbbe já aprovados para o aplicativo. A versão 1.5.6 aplica a marca aos textos
traduzidos, ao título fixo da janela, ao rodapé e aos links principais.

As chaves de tradução e as tabelas originais são preservadas: a substituição
ocorre depois da tradução, inclusive nas mensagens de servidor e no rodapé.
Isso mantém os idiomas, as variáveis e a compatibilidade das chamadas.
As variantes de grafia encontradas nos textos italiano e tâmil também são
convertidas, preservando os domínios reais dos links de documentação técnica.

Referências técnicas que continuam contendo o nome original:

- Dependências, submódulos, crates, biblioteca nativa e símbolos FFI: correspondem
  a componentes reais utilizados pelo build.
- Protocolos, canais Flutter, variáveis de ambiente e formatos de configuração:
  interfaces compartilhadas que precisam continuar compatíveis.
- Identificadores `MyUbbeAllDesk`, nomes de serviço, executável e bundle do fork:
  preservam os dados, permissões e atualizações das instalações existentes.
- URLs de documentação técnica upstream: apontam para documentos reais; não
  foram substituídas por domínios ou páginas inexistentes.
- Licença, copyright, autoria, documentação histórica e procedência do código:
  preservam a atribuição ao RustDesk e seus autores.

O módulo Swift e suas duas referências XIB agora usam `AllDesk` em conjunto.
O SBOM publicado passa a se chamar `alldesk.sbom.json`. Android, iOS e Linux
recebem apenas ajustes de rótulos em suas fontes; a distribuição configurada
continua publicando somente os pacotes Windows e macOS.
