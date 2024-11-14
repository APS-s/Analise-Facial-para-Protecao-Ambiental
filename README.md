# Como configurar o ambiente de desenvolvimento

### Como Instalar

1. Instale a ferramenta GIT, caso não tenha
2. Instale o Python 3.7, caso não tenha
3. Instale o MySQL, caso ainda não tenha
4. Clone o repositório https://github.com/APS-s/Analise-Facial-para-Protecao-Ambiental.git
5. Acesse a pasta criada
6. Execute o comando `pip install -r pip install -r requirements.txt`
7. Importe a tabela `default_table.sql` para o banco de dados. Para saber como importar a tabela, consulte a documentação do MySQL.

### Como Executar

NOTA: Para a execução do aplicativo, é necessário ter uma câmera instalada no computador

- Para executar o aplicativo de cadastro
    1. Navegue para a pasta `source`
    2. Abra um terminal no diretório vigente
    3. Execute o comando `python3 register_app.py` 
    NOTA: Dependendo de como o python foi instalado, podem existir variações do comando `python3`. Estes incluem, mas não estão limitados a: `python` e `py`.
- Para executar o script de acesso
    1. Navegue para a pasta `source`
    2. Abra um terminal no diretório vigente
    3. Execute o comando `python3 main.py` 
    NOTA: Dependendo de como o python foi instalado, podem existir variações do comando `python3`. Estes incluem, mas não estão limitados a: `python` e `py`.

# Recomendações
Para obter melhores resultados, siga estas orientações:
- **Ambiente iluminado e fundo liso**: Posicione-se em um local bem iluminado, de preferência com uma parede lisa e sem muitos detalhes ao fundo. Isso facilita a detecção do rosto pelo sistema.
- **Repetir se necessário**: Se o programa não detectar nenhum rosto, tente novamente. Isso pode ocorrer devido a problemas de iluminação ou pela presença de múltiplos rostos no ambiente. Caso a detecção continue falhando, procure um lugar mais adequado, com menos elementos no fundo.


# Funcionamento do programa
## database_connection.py

Este script utiliza a biblioteca `mysql.connector` para estabelecer uma conexão com um banco de dados MySQL através do método `conexao_a_database()`. Dentro do método, é realizada uma tentativa de conexão com o banco utilizando as credenciais e o nome do banco especificados. Caso a conexão seja bem-sucedida, o objeto `conn` é retornado, permitindo interações com o banco de dados. Se ocorrer algum erro de conexão, o script captura a exceção e exibe uma mensagem informativa com o erro encontrado, retornando `None` para indicar falha na conexão.

## take_and_analyze_a_picture_cascate.py

Este script utiliza as bibliotecas `cv2` e `os` para capturar uma imagem com a webcam e detectar rostos usando o método de detecção em cascata do OpenCV. O script salva a imagem em uma pasta especificada, adicionando um contorno ao redor dos rostos detectados.

**Configuração e Inicialização**

A função `tirar_e_analisar_foto_cascata(save_path, image_name)` configura e executa o processo de captura e análise de imagem. Para detecção facial, o script usa o classificador Haar Cascade, carregado do arquivo XML `haarcascade_frontalface_default.xml`. Este modelo é amplamente utilizado para reconhecimento facial e está incluído no repositório do OpenCV.

**Verificação do Caminho**

O script verifica inicialmente se a pasta especificada (`save_path`) existe. Caso contrário, ele a cria, garantindo que a imagem capturada seja salva no local correto.

**Carregamento do Classificador**

O modelo Haar Cascade é carregado e verificado. Se houver falha ao carregar o arquivo XML, o script emite uma mensagem de erro.

**Captura e Processamento da Imagem**

**Início da Captura com a Webcam**

Ao iniciar a webcam, o usuário deve centralizar o rosto na tela e pressionar a tecla `ESC` para capturar a imagem, assegurando o enquadramento adequado.

**Transformações de Imagem**

- **Escala de Cinza**: A imagem capturada é convertida para escala de cinza para facilitar a detecção de rostos.
- **Equalização de Histograma**: Aplicada à imagem em tons de cinza para melhorar a visibilidade dos detalhes faciais.
- **Desfoque Gaussiano**: Na imagem original colorida, aplica-se um filtro de suavização para reduzir o ruído, auxiliando na detecção de contornos.

**Detecção de Rostos com Haar Cascade**

O classificador Haar Cascade detecta rostos na imagem convertida. Parâmetros cruciais usados na função `detectMultiScale()` incluem:

- **`scaleFactor=1.05`**: Aumenta a sensibilidade à variação de tamanhos de rostos.
- **`minNeighbors=4`**: Reduz a probabilidade de falsos positivos.
- `<i>minSize</i>=(30, 30)`: Especifica o tamanho mínimo do rosto.

Quando um ou mais rostos são detectados:

- **Contornos**: Retângulos são desenhados ao redor dos rostos na imagem original para destacar as áreas detectadas.
- **Visualização e Salvamento**: A imagem com os contornos é exibida e salva no diretório indicado com o nome de arquivo fornecido (`image_name`).

**Resultado**

Após a detecção, o caminho da imagem é retornado e exibido ao usuário. Se nenhum rosto for encontrado, o script exibe uma mensagem informativa e não salva a imagem.

Por fim, a webcam é liberada e todas as janelas de visualização são fechadas automaticamente.

## take_and_analyze_a_picture_neural.py

Este script utiliza as bibliotecas `cv2`, `os`, e `numpy` no método `tirar_e_analisar_foto_rede(save_path, image_name)`. Seu objetivo é capturar uma imagem pela webcam, processá-la com desfoque e escala de cinza, e detectar rostos utilizando uma rede neural convolucional pré-treinada.

**Configuração e Inicialização**

O script carrega um modelo de rede neural para detecção de rostos usando os arquivos `deploy.prototxt` e `res10_300x300_ssd_iter_140000.caffemodel`. Esses arquivos foram obtidos a partir do repositório oficial do OpenCV no GitHub e contêm, respectivamente, a estrutura da rede e os pesos pré-treinados. A função `cv2.dnn.readNetFromCaffe()` é usada para carregar o modelo, preparando-o para identificar rostos nas imagens capturadas.

**Captura e transformações de Imagem**

A webcam é aberta e uma imagem é capturada após o usuário pressionar a tecla `ESC` para confirmar o enquadramento. A imagem é então convertida para escala de cinza e sofre uma equalização de histograma para realçar as características visuais. Um filtro de desfoque gaussiano é aplicado para reduzir ruídos.

**Processamento da Imagem com a Rede Neural**

A imagem é convertida em um “blob” (uma estrutura compatível com a entrada da rede neural) com a dimensão de 400x400 pixels. Esse blob é passado pela rede neural, e as detecções de rostos são processadas com uma confiança mínima de 0.7. Quando rostos são detectados, retângulos são desenhados ao redor deles.

**Resultado**

A imagem com os rostos identificados é exibida e salva na pasta especificada pelo usuário, com o nome indicado nos parâmetros.

Ao final, a webcam é liberada, e todas as janelas abertas pelo `cv2` são fechadas.

## face_comparison.py

Este script utiliza `dlib`, `cv2`, `numpy`, e uma conexão com um banco de dados para comparar o rosto de um indivíduo capturado em uma imagem com rostos autorizados armazenados. Ele visa determinar se o rosto corresponde ao de algum funcionário cadastrado, retornando o cargo correspondente ao rosto encontrado.

**Conexão ao Banco de Dados**

A função `conexao_a_database()` é importada do script `database_connection.py` e estabelece uma conexão com o banco de dados para obter as informações dos rostos autorizados e seus respectivos cargos. Caso não haja conexão, o script encerra o processo com uma mensagem de erro.

**Carregamento da Imagem**

O script carrega a imagem que será analisada a partir do caminho `image_path`. Caso a imagem não seja carregada corretamente, o processo é encerrado com uma mensagem de erro.

**Inicialização de Componentes do `dlib` que são carregados pelo script**:

- Um **detector de rostos** (`get_frontal_face_detector()`) que identifica rostos na imagem.
- Um **predictor de pontos faciais** (`shape_predictor`) para obter pontos específicos do rosto, carregando o modelo de landmarks do arquivo `shape_predictor_68_face_landmarks.dat`.
- Um **modelo de reconhecimento facial** (`face_recognition_model_v1`) que extrai descritores faciais, representando características únicas do rosto, carregado de `dlib_face_recognition_resnet_model_v1.dat`.

**Detecção de Rosto**

O rosto é detectado na imagem analisada. Caso nenhum rosto seja identificado, o script encerra o processo com uma mensagem de erro.

**Descritor de Rosto**

Utilizando os pontos faciais obtidos pelo `shape_predictor`, o script calcula o descritor facial da imagem analisada, criando uma representação única que será usada para comparação.

**Consulta ao Banco de Dados**

O script realiza uma consulta SQL para obter a lista de rostos autorizados (`rosto`) e seus cargos (`cargo`) armazenados no banco de dados `pessoasautorizadas`.

**Iteração e Comparação de Rostos:**

- Para cada registro de rosto no banco de dados:
    - **Verificação do Arquivo**: Verifica se o caminho da imagem existe. Se não, exibe uma mensagem de erro e continua para o próximo registro.
    - **Carregamento e Detecção do Rosto**: Carrega a imagem correspondente ao rosto e aplica o detector de rostos para identificar a região facial.
    - **Cálculo do Descritor de Rosto**: Após detectar o rosto, calcula o descritor facial do rosto armazenado.
    - **Cálculo da Distância**: A distância entre os descritores faciais do rosto analisado e do banco de dados é calculada usando a **distância Euclidiana** (`np.linalg.norm`). Essa distância indica a similaridade entre os rostos: quanto menor a distância, maior a similaridade.
    - **Critério de Correspondência**: Se a distância for menor ou igual ao limite `min_distance = 0.5`, o script considera que houve uma correspondência e armazena o cargo do funcionário correspondente.

**Encerramento da Conexão**

O cursor e a conexão com o banco de dados são fechados após o término da comparação.

**Retorno do Cargo**

O cargo do rosto identificado (se houver uma correspondência) é retornado. Caso nenhum rosto autorizado seja identificado com uma distância suficiente, o script retorna "Nenhum".

## file_opening.py

Este script utiliza a biblioteca `os` para acessar e abrir arquivos específicos armazenados em um diretório local, com base no valor fornecido ao método `abrir_arquivos()`.

**Configuração do Caminho do Arquivo**

Dentro da função `abrir_arquivos(valor)`, é construída uma string `file_path` que representa o caminho absoluto do arquivo. Esse caminho é resolvido dinamicamente usando o valor fornecido para a função (`valor`), o qual é inserido no nome do arquivo (`Doc{valor}.docx`) dentro do diretório `confidencial_documents`.

**Verificação da Existência do Arquivo**

O script verifica se o arquivo especificado existe no caminho construído com `os.path.exists(file_path)`. Caso o arquivo seja encontrado, ele será aberto pelo comando `os.startfile(file_path)`, que utiliza o programa padrão associado ao tipo de arquivo (neste caso, `.docx`) para exibir o documento. Uma mensagem de confirmação “Abrindo Arquivo {valor}” também é exibida no console.

**Mensagem de Erro**

Se o arquivo não existir no caminho especificado, o script exibe uma mensagem informativa no console alertando o usuário de que o arquivo não foi encontrado, com uma sugestão para verificar o caminho e a existência do arquivo.

## main.py

Este script realiza a captura, análise e comparação de rostos para verificar o nível de acesso de uma pessoa e abrir documentos específicos com base no cargo identificado

**Importações de Módulos e Funções**

São importadas três funções principais de outros scripts

- A função `tirar_e_analisar_foto_rede` (renomeada como `tirar_e_analisar_foto`) do módulo `take_and_analyze_a_picture_neural` ou `tirar_e_analisar_foto_cascata` (também renomeada como `tirar_e_analisar_foto`) do módulo `take_and_analyze_a_picture_cascade` captura e processa uma imagem de rosto utilizando uma rede neural ou um modelo de detecção por cascata, respectivamente. A escolha entre `tirar_e_analisar_foto_cascata` e `tirar_e_analisar_foto_rede` depende das necessidades do usuário, pois ambas demonstram desempenho semelhante em testes. No entanto, `tirar_e_analisar_foto_cascata` mostrou maior consistência na quantidade de rostos detectados e analisados. Por ser um projeto baseado em inteligência artificial, o método `tirar_e_analisar_foto_rede` é adotado como padrão, alinhando-se melhor com a temática do projeto.
- `comparar_faces_funcionarios` do módulo `face_comparison`, que compara o rosto capturado com um banco de dados de funcionários, identificando o cargo da pessoa.
- `abrir_arquivos` do módulo `file_opening`, que permite abrir documentos específicos conforme o nível de acesso.

**Captura, Análise e Comparação de Rostos**

A função `tirar_e_analisar_foto` é chamada para capturar uma imagem de rosto e salvá-la no diretório especificado (`faces/analyzing`) com o nome `imagem_capturada.jpg`. Ela retorna o caminho do arquivo salvo.

A imagem capturada é então passada para a função `comparar_faces_funcionarios`, que a compara com as imagens no banco de dados e retorna o cargo identificado.

Em seguida, o cargo da pessoa analisada é exibido no console.

**Definição dos Níveis de Acesso**

São definidos três níveis de acesso (`nivel_acesso1`, `nivel_acesso2` e `nivel_acesso3`), cada um contendo cargos específicos. Estes níveis determinam os documentos que serão abertos para cada cargo.

**Verificação do Cargo e Acesso aos Documentos**

O script verifica se o cargo identificado pertence a algum dos níveis de acesso:

- Se o cargo pertence a `nivel_acesso1`, a função `abrir_arquivos(1)` é chamada para abrir o primeiro documento.
- Se o cargo está em `nivel_acesso2`, `abrir_arquivos(2)` abre o segundo documento.
- Se o cargo está em `nivel_acesso3`, `abrir_arquivos(3)` abre o terceiro documento.

Caso o cargo não corresponda a nenhum dos níveis de acesso definidos, o acesso é negado e uma mensagem informativa é exibida.

## Aplicativo de Cadastro

Este script cria uma interface gráfica para registrar funcionários em um banco de dados, incluindo a captura e análise de fotos. Ele utiliza o Tkinter para a interface gráfica e interage com o banco de dados para salvar o nome, cargo e a foto de cada funcionário.

A interface permite registrar funcionários com nome, cargo e uma foto. A imagem é capturada, analisada e salva em uma pasta específica, enquanto os dados são armazenados em um banco de dados, incluindo o caminho para a foto. O script inclui tratamento de erros para garantir que todas as etapas (preenchimento dos campos e captura da foto) sejam cumpridas antes de salvar os dados.

**Importação de Módulos**

- **tkinter** é utilizado para desenvolver a interface gráfica.
- **messagebox**, um módulo do tkinter, exibe mensagens de erro ou sucesso na interface.
- A função `tirar_e_analisar_foto_rede` (renomeada como `tirar_e_analisar_foto`) do módulo `take_and_analyze_a_picture_neural` ou `tirar_e_analisar_foto_cascata` (também renomeada como `tirar_e_analisar_foto`) do módulo `take_and_analyze_a_picture_cascade` captura e processa uma imagem de rosto. Ambas demonstram desempenho semelhante, mas `tirar_e_analisar_foto_cascata` mostrou maior consistência na detecção de rostos. O método `tirar_e_analisar_foto_rede` é adotado como padrão por se alinhar melhor com a temática de inteligência artificial do projeto.
- A função `conexao_a_database()` do script `database_connection.py` estabelece uma conexão com o banco de dados para inserir o nome, cargo e rosto do funcionário.

**Variável Global**

**global image_path**: armazena o caminho da imagem capturada, permitindo acesso por outras funções dentro do escopo global do script.

### Função `salvar_dados(nome, cargo, image_path_def)`

Salva no banco de dados o nome, cargo e o caminho da foto do funcionário:

**Verificação Inicial**

Garante que todos os dados (nome, cargo e caminho da imagem) estejam preenchidos antes de salvar.

**Bloco Try-Except**:

Tenta estabelecer uma conexão com o banco de dados e executa uma inserção de dados na tabela `pessoasautorizadas`. Em caso de erro, verifica se está relacionado à falta de imagem, exibindo uma mensagem específica, ou se é um erro genérico.

### Função `tirar_foto_wrapper()`

Usada para capturar e processar a foto de um novo funcionário.

**Conexão com o Banco**

Verifica o maior ID existente na tabela `pessoasautorizadas` para definir um ID único, usado no nome da imagem (por exemplo, `face_{id}.jpg`), simplificando a resolução de problemas.

**Caminho da Imagem**

Define onde a imagem será salva localmente (`faces/employees/`).

**Chamada de Função**

Executa `tirar_e_analisar_foto` para capturar e processar a imagem.

### Função `criar_ui()`

Esta função cria a interface gráfica para o registro de novos funcionários.

**Janela Principal**

Cria a janela principal da aplicação.

**Entradas de Dados**

**Nome Completo**: cria um campo de texto para inserção do nome completo do funcionário.

**Cargo**: cria botões de opção para seleção do cargo, incluindo opções como "Ministro" e "Estagiário".

**Funções Auxiliares**:

- **on_tirar_foto()**: chama `tirar_foto_wrapper` e armazena o caminho da imagem capturada na variável global `image_path`.
- **on_salvar_dados()**: coleta os valores de `entry_nome`, `cargo_var` e `image_path`, chamando `salvar_dados` para inserir as informações no banco. Após salvar, redefine `image_path` para `None`, permitindo a inclusão de outro funcionário.

**Botões**:

- **Tirar Foto**: executa `on_tirar_foto` para capturar e analisar a imagem.
- **Salvar**: executa `on_salvar_dados` para salvar os dados no banco de dados.

**Execução da Interface**

`root.mainloop()` exibe e mantém a interface aberta até o usuário fechá-la.

### Execução

Por fim, o script chama a função `criar_ui()` para iniciar a interface gráfica e permitir o registro dos funcionários.