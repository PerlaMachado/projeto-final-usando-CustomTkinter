# 🚀 Sistema de Automação Desktop

## 📌 Sobre o Projeto

O Sistema de Automação é uma aplicação desenvolvida em Python com interface gráfica moderna utilizando CustomTkinter.

O objetivo do sistema é centralizar pequenas automações em um único ambiente organizado, intuitivo e visualmente moderno.

O sistema possui:

* Tela de login
* Alteração de tema (claro e escuro)
* Calculadora
* Consulta de cotação em tempo real
* Controle de preços com exportação Excel
* Organização automática de arquivos
* Salvamento automático de dados

---

# 🖥️ Como Executar o Sistema

## 1. Abrir a pasta do projeto

Abra a pasta:

```plaintext
Projeto_Final
```

Ela contém todos os arquivos necessários do sistema.

---

## 2. Abrir o terminal

No VS Code:

* Clique em Terminal
* Novo Terminal

---

## 3. Ativar o ambiente virtual

Antes de executar o sistema, é necessário ativar o ambiente virtual.

Após ativar corretamente, aparecerá:

```plaintext
(.venv)
```

no início do terminal.

---

## 4. Executar o sistema

Com o ambiente virtual ativo:

Execute o arquivo principal do sistema.

Após isso, a tela de login será aberta automaticamente.

---

# 🔐 Tela de Login

A primeira tela do sistema é a tela de login.

Ela possui:

* Campo de usuário
* Campo de senha
* Botão de entrada
* Alternância de tema

---

## Funcionamento do Login

O sistema verifica:

* Usuário
* Senha

Caso os dados estejam corretos:

✅ O menu principal será aberto.

Caso estejam incorretos:

❌ Uma mensagem de erro será exibida.

Usuário: admin
Senha: 1234

---

# 🌗 Sistema de Tema

O sistema possui dois modos:

* Tema escuro
* Tema claro

A alteração é feita através do botão localizado no canto superior direito.

---

## Tema Escuro

Características:

* Fundo escuro
* Cards escuros
* Texto branco
* Botões azuis

Ideal para ambientes com pouca iluminação.

---

## Tema Claro

Características:

* Fundo claro
* Cards brancos
* Texto escuro
* Botões azuis

Ideal para ambientes iluminados.

---

## Funcionamento do Tema

Quando o tema é alterado:

✅ Todas as telas acompanham automaticamente.

Isso inclui:

* Menu principal
* Calculadora
* Cotação
* Controle de preços
* E-mail

---

# 🧭 Menu Principal

Após o login, o usuário acessa o menu principal.

O menu possui uma barra lateral com os módulos do sistema.

Os módulos disponíveis são:

* Calculadora
* E-mail
* Cotação
* Excel

---

## Funcionamento das Janelas

O sistema foi desenvolvido para trabalhar em uma única janela.

Ao clicar em um módulo:

✅ O conteúdo aparece dentro da mesma interface.

Isso evita abertura de múltiplas janelas e deixa a experiência mais organizada.

---

# 🧮 Módulo Calculadora

O módulo calculadora permite realizar operações matemáticas básicas.

---

## Funcionalidades

* Soma
* Subtração
* Multiplicação
* Divisão

---

## Como Utilizar

### 1. Digite o primeiro número

Exemplo:

```plaintext
10
```

---

### 2. Digite o segundo número

Exemplo:

```plaintext
5
```

---

### 3. Escolha a operação

Exemplo:

```plaintext
+
```

---

## Resultado

O sistema exibirá automaticamente o resultado.

Exemplo:

```plaintext
Resultado: 15
```

---

## Botão Limpar

O botão limpar:

* Remove os números digitados
* Reinicia o resultado

---

# 💵 Módulo de Cotação

O módulo de cotação consulta informações em tempo real através de API pública.

---

## Informações Exibidas

O sistema mostra:

* Cotação atual do dólar
* Cotação atual do euro
* Horário da consulta

---

## Funcionamento

Ao abrir o módulo:

✅ O sistema consulta automaticamente a internet.

Os valores são exibidos na tela.

---

## Exemplo de Resultado

```plaintext
Dólar: R$ 5,43
Euro: R$ 6,12
Consulta realizada em: 14:35
```

---

## Tratamento de Erros

Caso não exista conexão com a internet:

❌ O sistema exibirá uma mensagem de erro.

Isso evita travamentos e melhora a experiência do usuário.

---

# 📊 Módulo Excel

O módulo Excel funciona como um pequeno sistema de controle de preços.

Ele permite:

* Adicionar produtos
* Atualizar preços
* Remover produtos
* Exportar planilhas
* Salvar dados automaticamente

---

# ➕ Adicionando Produtos

## Passo 1

Digite o nome do produto.

Exemplo:

```plaintext
Mouse Gamer
```

---

## Passo 2

Digite o preço atual.

Exemplo:

```plaintext
150
```

---

## Passo 3

Clique em:

```plaintext
Adicionar Produto
```

---

## Resultado

O produto será exibido automaticamente na tabela.

---

# 🔄 Atualizando Preços

O sistema mantém histórico de alterações.

---

## Como funciona

### 1. Selecione um produto na tabela

### 2. Digite o novo preço

### 3. Clique em:

```plaintext
Atualizar Preço
```

---

## O sistema irá:

✅ Salvar o preço antigo

✅ Atualizar o preço atual

✅ Mostrar status da alteração

---

## Exemplos de Status

### Quando o preço aumenta

```plaintext
▲ Aumentou
```

---

### Quando o preço diminui

```plaintext
▼ Diminuiu
```

---

### Quando o preço permanece igual

```plaintext
▬ Igual
```

---

# ❌ Removendo Produtos

Para remover:

1. Selecione o produto
2. Clique em:

```plaintext
Remover
```

O item será apagado automaticamente.

---

# 💾 Salvamento Automático

O sistema salva os dados automaticamente.

Isso significa que:

✅ Mesmo fechando o sistema

✅ Os produtos continuarão salvos

na próxima execução.

---

# 📁 Pasta de Arquivos

O sistema cria automaticamente a pasta:

```plaintext
arquivos
```

Ela é utilizada para armazenar:

* Planilhas Excel
* Dados salvos
* Arquivos do sistema

---

# 📄 Arquivo JSON

Os produtos são armazenados automaticamente em:

```plaintext
arquivos/produtos.json
```

Esse arquivo guarda:

* Nome do produto
* Preço antigo
* Preço atual
* Status

---

# 📈 Exportação Excel

O sistema permite exportar os dados para Excel.

---

## Como Exportar

Clique em:

```plaintext
Exportar Excel
```

---

## Resultado

O sistema criará automaticamente:

```plaintext
controle_precos.xlsx
```

na pasta:

```plaintext
arquivos
```

---

# 📂 Como Acessar a Planilha

Abra a pasta:

```plaintext
Projeto_Final/arquivos
```

Depois abra:

```plaintext
controle_precos.xlsx
```

---

## Importante

O arquivo Excel deve ser aberto em:

* Microsoft Excel
* LibreOffice Calc
* Google Sheets

---

## Observação

Arquivos `.xlsx` não devem ser abertos no VS Code como texto.

Isso acontece porque arquivos Excel são binários.

---

# 📧 Módulo E-mail

O sistema possui uma área destinada para automação de e-mails.

Ela pode ser expandida futuramente para:

* Envio automático
* Disparo em massa
* Notificações
* Integração com SMTP

---

# 🏗️ Estrutura do Projeto

O projeto é dividido em módulos.

Isso melhora:

* Organização
* Manutenção
* Escalabilidade
* Leitura do código

---

# 📦 Organização dos Arquivos

Estrutura principal:

```plaintext
Projeto_Final/
│
├── arquivos/
├── calculadora.py
├── cambio.py
├── cores.py
├── email_auto.py
├── excel_precos.py
├── login.py
├── menu.py
├── tema.py
```

---

# ✨ Recursos do Sistema

O sistema possui:

✅ Interface moderna

✅ Tema escuro e claro

✅ API pública

✅ Persistência de dados

✅ Exportação Excel

✅ Salvamento automático

✅ Estrutura modular

✅ Navegação em única janela

✅ Organização automática de arquivos

---

# 🎯 Objetivo do Projeto

O projeto foi desenvolvido com foco em:

* Automação
* Interface moderna
* Organização de dados
* Experiência do usuário
* Estrutura profissional

Além disso, o sistema demonstra conceitos importantes de desenvolvimento desktop com Python.

---

# 🚀 Considerações Finais

O Sistema de Automação Desktop foi desenvolvido para reunir diferentes funcionalidades em um único ambiente intuitivo.

A estrutura modular permite expansão futura, tornando possível adicionar novos módulos e automações conforme necessário.

O projeto também demonstra boas práticas de:

* Organização
* Interface gráfica
* Persistência de dados
* Consumo de API
* Exportação de arquivos
* Experiência visual

---

# ✅ Fim da Documentação
#   p r o j e t o - f i n a l - u s a n d o - C u s t o m T k i n t e r  
 