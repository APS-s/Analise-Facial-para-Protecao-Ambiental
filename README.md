### Problemas Conhecidos
[ ] Melhorar o reconhecimento facial

### A fazer ainda
TODO: Melhorar a detecção facial
    - A detecção utlizando o take_and_analyze_a_picture_rede.py foi consideravelmente maior do que o de take_and_analyze_a_picture.py
        TODO: Realizar mais testes e caso ela realmente se saia melhor, utilizar ela no register_app.py também
TODO: Criar um tratamento de erros no main.py e register_app.py OU no take_and_analyze_a_picture.py para caso ele não consiga detectar o rosto, ele não de erro, apenas uma mensagem dizendo pra tirar outra foto

### Links Importantes
https://trello.com/b/DGHwHJAm/aps
https://www.notion.so/APS-dea6d7900cd24b37b4126c36d505e81d?pvs=4
https://calendar.google.com/calendar/u/0/r

### Documentação 
Na documentação explicar tudo aos minimos detalhes, desde a estrutura de arquivos, funcionamento do programa, bibliotecas analisadas, uso de modelos e etc

Lembrar de explicar sobre (Para o take_and_analyze_a_picture_rede.py):
- confidence
- Dimensões do Blob
- Equalização do Histograma
- Desfoque Gaussiano