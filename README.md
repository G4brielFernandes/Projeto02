Resumo do Projeto: Automação de Geração e Envio de Contrato com Python
Este projeto automatiza o processo de geração de contratos personalizados e envio via WhatsApp, utilizando Python e algumas bibliotecas para automação:

Geração do contrato:
Usa a biblioteca python-docx para abrir um modelo .docx e substituir marcadores por informações fornecidas pelo usuário (nome, CPF, endereço, forma de pagamento, entre outros). O contrato é salvo com o nome do contratado.

Automação do envio pelo WhatsApp:
Utiliza a biblioteca pyautogui para controlar o mouse e teclado, abrir o navegador, acessar o WhatsApp Web, buscar o contato do vendedor, anexar o contrato gerado e enviar a mensagem automaticamente.

Interação via input:
O script pede dados ao usuário para preencher o contrato e realizar o envio.
