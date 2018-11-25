# Integración de BCI en ROS

Este es el repositorio de un TFG sobre la integración de distintos cascos BCI con ROS.

## Información del alumno ## 
* **Nombre**: Jesús Pérez Limón
* **Universidad**: UHU ETSI
* **Carrera**: Grado en Ingeniería Informática

## Hardware ##
* Raspberry Pi 3b con Raspbian Strech

## Objetivo ##
El objetivo de este tfg es poder usar la información de los cascos BCI para mover un robot corriendo sobre ROS. Los cascos elegido para ello son [MindWare de Neurosky](https://store.neurosky.com/pages/mindwave) y [Emotiv Insight](https://www.emotiv.com/insight/).

## Distribución de carpetas ## 
Cada casco BCI cuenta con su carpeta para almacenar todo el código, driver y ficheros de configuración.

Cada carpeta sigue la siguiente estructura:
 * Carpeta *drivers* para guardar los drivers necesarios en el uso del BCI
 * Carpeta *src* para almacenar todo el código de la integración.

## Instalación de ROS en Raspbian Stretch ##
Para la instalación de ROS se han usado los siguientes comandos:

``` 
sudo apt-get install dirmngr

sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install -y python-rosdep python-rosinstall-generator python-wstool python-rosinstall build-essential cmake

sudo rosdep init
rosdep update
```

