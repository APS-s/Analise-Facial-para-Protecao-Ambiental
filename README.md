### Funcionamento Base
1. Tira a foto (take_a_picture.py) ✅
2. Analisa a foto (face_recognition.py) ✅
3. Abre conexão com o banco de dados (database_connection.py) ✅
4. Compara a foto com o banco de dados (funcionarios_comparison.py)
5. Libera o acesso aos pdfs (file_opening.py) ✅

### Problemas Conhecidos
[ ] Os metodos na classe 'main.py' não estão funcionando de forma sincrona
[ ] O metodo 'compare_faces' da classe 'funcionarios_comparison.py' não está funcionando 

### A fazer ainda
[ ] Conectar o Banco de Dados a rede do Hugo
[ ] Criar a classe 'perigosos_comparison.py' onde nela serão salvos os rostos de quem ficou com verificação de cargo da classe 'main.py' como *none* (Talve o perigosos_comparison.py se torne apenas um metodo da classe database_comparison e então nela estarão o perigosos e os funcionarios em metodos diferentes)

### Links Importantes
https://trello.com/b/DGHwHJAm/aps
https://www.notion.so/APS-dea6d7900cd24b37b4126c36d505e81d?pvs=4
https://calendar.google.com/calendar/u/0/r