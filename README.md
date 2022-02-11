# MyLibrary (Em Desevolvimento)
  MyLibrary tem como objetivo de resolver o problema de quem tem varios livros em suas prateleiras/estantes, afim de facilitar a buscar de se possui ou não um determinado livro. 
# Quick Start
   1 - Faça o download do repositório ou utilize o comando `git clone https://github.com/LucRioss/MyLibrary-Django.git` dentro do diretório desejado.
   
   2 - Configure o [virtual environment do Python](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment), para realizar a instalação das dependecias necessárias.
   
   3 - Para realizar a instalação esteja com a virtual environment ativo e dentro do diretório do requirements.txt e utilize o comando dentro do terminal `py pip install -r requirements.txt`.
   
   4 - Depois utilize o comando `py .\manage.py runserver`, para utilizar esse comando tem que estar no mesmo diretório do `manage.py` caso ocorra erro de Migrate utilize os comando a seguir `py .\manage.py makemigrations` `py .\manage.py migrate` e tente novamento o comando `py .\manage.py runserver`.
   
   5 - Após executar o comando para iniciar o servidor acesse dentro do navegador o seguinte link `http://127.0.0.1:8000` que carregará a seguinte pagina:
   
   ![img1](https://user-images.githubusercontent.com/13575185/153595339-56598351-0edf-44b7-ada3-19f6ae57c878.png)
    
   6 - Para ir aos templates funcionais, ao acessar o seguinte link `http://127.0.0.1:8000/books/` terá acesso a seguintes paginas:
   
   `index`
   
   ![img2](https://user-images.githubusercontent.com/13575185/153597159-0fb4da35-6374-4c96-bc4a-66c390f7a6ad.png)

   `Adição de Livros`
    
   ![img3](https://user-images.githubusercontent.com/13575185/153597484-406154d4-77da-4387-bfac-c0b9c916b1dc.png)
   
   `Visualização dos Livros Adicionados`
   
   ![img4](https://user-images.githubusercontent.com/13575185/153597826-24a607ec-e13a-4c0e-be44-adbe76e42466.png)
    
   Caso clique no nome do livro a pagina com os detalhe do livro será carrega, atualmente ela está incompleta, com dois botões `Att seu Livro` que vai para a pagina de Update de dados do livro que foi selecionado, e o botão `Delete` que tem a função de deletar os dados do livro selecionado.
   
   `Detalhe do Livros`
   
   ![img5](https://user-images.githubusercontent.com/13575185/153598552-14a2422a-2a0f-49e9-8129-2591063d9f33.png)
    
   `Botão "Att seu Livro" `
    
   ![img6](https://user-images.githubusercontent.com/13575185/153598672-c92d0076-7e61-418b-88d6-9d89bd6256af.png)
   
   `Botão "Delete" `
   
   ![img7](https://user-images.githubusercontent.com/13575185/153598850-ab346756-bc01-462e-a43f-ac438b939e97.png)
  
  Caso queira acessar o painel administrador, utilize o seguinte comando após encerrar o servidor `py .\manage.py createsuperuser` após seguir os passos acessar o link `http://127.0.0.1:8000/admin` que será redirecionando a seguir tela para a inserção do dados cadastrados anteriormente:
  
  ![img8](https://user-images.githubusercontent.com/13575185/153599628-1106a5d5-1b17-4904-8deb-eb4d925d6e46.png) 
