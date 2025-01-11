# EB SURVIVAL

## Intruduccion
Bienvenidos a mi proyecto, a continuacion, se realizara una descripcion del proyecto asi como de su funcionalidad.


## Sobre el Proyecto
Este proyecto, es un videojuego creado con python y la libreria Pygame, en el cual consta de un personaje, un inventario, una barra de acceso rapido, enemigos entre otras.


### Inventario
El inventario, puede ser abierto precionando la tecla ( i ), en donde se podran observar los diferentes items que se vayan opteniendo durante el tiempo de juego

### Enemigos
El videojuego constra de 3 enemigos, primeramente tenemos un Esqueleto, luego un Slime verde y por ultimo un Slime morado, el cual cada uno tiene su vida y daño

## Funcionalidades
-**Exploracion**: El jugador podra explorar el mundo, el cual puede hacerlo presionando las teclas de UP, DOWN, LEFT, RIGTH, lo cual hara que el personaje empiece a moverse

-**Combate**: El jugador podra entrar en combate con los diferentes enemigos que cuenta el juego, visualizar como la barra de vida disminuye tanto la propia como la del enemigo

Para hacerlo, debe acercarse a un enemigo y precionar click sobre el enemigo el cual desea atacar

## Instalacion
Para intalar el juego

```bash 
# Clona el repositorio 
git https://github.com/ld-ebrat/EB_Survival_Kodland.git
cd EB_Survival_Kodland
# Instalar virtualenv
pip install virtualenv
# Crear el entorno virtual 
virtualenv venv
# Activar el entorno virtual
.\venv\Scripts\actívate
#Instala las dependencias 
pip install -r requirements.txt
```

## Arranque
Para poder arrancar el juego, solamente debe irse a la carpeta donde se clono el proyecto, y ejectura 
```cmd
python main.py
```