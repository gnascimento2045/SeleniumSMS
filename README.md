**Sistema de Envio Automático de SMS via Google Messages utilizando Python e Selenium
**
Descrição Geral: Este sistema foi desenvolvido para automatizar o envio de mensagens SMS através da plataforma Google Messages. Utilizando Python e a biblioteca Selenium, o sistema interage diretamente com a interface web do Google Messages, proporcionando uma solução eficiente e escalável para enviar mensagens de texto de forma automatizada.

Funcionalidades Principais:
Abertura Automática do Google Messages:

O sistema inicia abrindo o site oficial do Google Messages (https://messages.google.com) no navegador.
Login Automatizado (se necessário):

Se o usuário não estiver logado, o sistema detecta a necessidade de autenticação e realiza o login de forma automatizada, sem a necessidade de interação manual.
Envio de SMS para Contatos ou Números Específicos:

O usuário pode inserir um número de telefone diretamente ou selecionar um contato previamente salvo no Google Messages.
Composição e Envio da Mensagem:

O sistema preenche automaticamente o campo de texto da mensagem com o conteúdo fornecido pelo usuário e realiza o envio com um simples clique no botão "Enviar".
Envio de Mensagens em Massa:

É possível enviar mensagens personalizadas para múltiplos destinatários em sequência, ideal para campanhas de marketing ou notificações em grande escala.
Tecnologias Utilizadas:
Python: Linguagem de programação principal utilizada para desenvolver o sistema e lidar com as lógicas de envio e controle de fluxo.
Selenium: Biblioteca utilizada para automatizar as interações com o navegador, como o preenchimento de campos de texto e o envio de mensagens.
Benefícios do Sistema:
Agilidade e Eficiência:

O processo de envio de SMS é completamente automatizado, reduzindo a necessidade de intervenção manual e permitindo o envio rápido de mensagens.
Facilidade de Uso:

Interface simples e intuitiva, garantindo que qualquer usuário, independentemente de seu nível técnico, possa utilizar o sistema com facilidade.
Escalabilidade:

Ideal para uso em campanhas de marketing, notificações em massa ou comunicação em grande escala, com a capacidade de enviar mensagens para vários destinatários simultaneamente.
Economia de Tempo:

O sistema permite que o envio de mensagens SMS seja realizado em grande volume, sem sobrecarregar os recursos humanos da equipe.
Fluxo de Operação:
Início:

O sistema inicia automaticamente o Google Messages no navegador.
Autenticação:

Caso o usuário não esteja logado, o script automatiza o processo de login.
Composição da Mensagem:

O usuário insere o número de telefone ou escolhe um contato da lista.
Em seguida, insere o conteúdo da mensagem.
Envio:

O sistema preenche automaticamente o campo de mensagem e clica no botão de envio, finalizando o processo.
Mensagens em Massa:

O sistema também pode ser configurado para enviar mensagens para vários números de uma vez.
