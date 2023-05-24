# LAN Network System

Este é um projeto que simula um sistema de rede local (LAN) com um servidor e clientes. O servidor é responsável por controlar o acesso dos clientes aos computadores da rede. Cada cliente pode solicitar acesso a um computador disponível por um determinado tempo e, após o término desse tempo, o acesso é liberado novamente.

## Estrutura de Arquivos

O projeto possui a seguinte estrutura de arquivos:

```
.
├── server
│   ├── server.py
│   └── __init__.py
├── client
│   ├── client.py
│   └── __init__.py
└── main.py
```

- A pasta `server` contém o arquivo `server.py`, que implementa a lógica do servidor.
- A pasta `client` contém o arquivo `client.py`, que implementa a lógica do cliente.
- O arquivo `main.py` é o ponto de entrada do programa e é responsável por iniciar o servidor ou o cliente, dependendo da escolha do usuário.

## Funcionalidades

### Servidor

O arquivo `server.py` implementa a classe `Server`, que é responsável por controlar o acesso dos clientes aos computadores da rede. O servidor oferece as seguintes funcionalidades:

- Inicialização do servidor e configuração do socket de escuta.
- Aceitação de novas conexões dos clientes.
- Gerenciamento das solicitações e liberações de acesso aos computadores.
- Fornecimento do status atual dos computadores da rede.

### Cliente

O arquivo `client.py` implementa a classe `Client`, que é responsável por se conectar ao servidor e interagir com ele. O cliente oferece as seguintes funcionalidades:

- Conexão ao servidor através de um endereço IP e porta.
- Solicitação do status atual dos computadores da rede.
- Solicitação de acesso a um computador disponível.
- Liberação do acesso a um computador previamente utilizado.

### Main

O arquivo `main.py` é o ponto de entrada do programa. Ele permite que o usuário escolha se deseja iniciar o servidor ou o cliente. Dependendo da escolha, o programa iniciará o servidor ou solicitará ao usuário o endereço IP e a porta do servidor para iniciar o cliente.

## Execução

Para executar o programa, siga as instruções abaixo:

1. Certifique-se de ter o Python instalado em sua máquina.
2. Abra o terminal e navegue até o diretório raiz do projeto.
3. Para iniciar o servidor, execute o seguinte comando:

   ```
   python main.py server
   ```

4. Para iniciar o cliente, execute o seguinte comando:

   ```
   python main.py client
   ```

5. Siga as instruções fornecidas pelo programa para interagir com o servidor e os computadores da rede.

Certifique-se de que o servidor esteja em execução antes de iniciar o cliente para estabelecer a comunicação corretamente.

## Considerações Finais

Este é um projeto simples que demonstra a comunicação entre um servidor e clientes em uma rede local. Sinta-se à vontade para explorar, modificar e expandir o código de acordo com suas necessidades.

Espero que essa documentação ajude a entender a estrutura do projeto e suas funcionalidades. Se você tiver alg

uma dúvida adicional, por favor, não hesite em entrar em contato.
