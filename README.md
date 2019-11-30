<h1 align="center">Musica para Todos</h1>
<h2 align="center">Site desenvolvido em Django usando Docker</h2>

### Dependências:
  <ul>
  <li>docker</li>
  <li>docker-compose</li>
  </ul>
 
 ### Instalando depêndecias:
 ### Arch Linux:
  <ul>
  <li>sudo pacman -Syu</li>
  <li>sudo pacman -S docker docker-compose</li>
  <li>sudo systemctl start docker</li>
  <li>sudo systemctl enable docker (caso queira que o docker inicie assim que o sistema ligar)</li>
  </ul>
 
### Debian:
  <ul>
    <li>sudo apt install docker.io docker-compose</li>
  </ul>
  
### Rodando a aplicação no Linux:
  <ul>
  <li>Depois de clonar o projeto entre no diretório app_aulaMusica e rode o comando:</li>
     <ul>
       <li>sudo docker-compose up</li>
     </ul>
 
  <li>Abra o navegador e acesse:</li>
    <ul>
      <li>localhost:8000</li>
    </ul>
  </ul>
