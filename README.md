<h1> Crear su entorno virtual para poder añadir las dependencias o librerias utilizadas en el proyecto </h1>

1. Abriremos el terminal con CTRL + SHIFT + Ñ o desde la opcion Terminal "New terminal"
2. pip install virtualenv
3. Ejecutaremos el comando " virtualenv -p python3 env " (Debes tener la ultima version de Python instalada) 
4. Entramos en el entorno virtual con el comando ".\env\Scripts\activate"
5. Usaremos en comando "python.exe -m pip install --upgrade pip " Para tener actualizado
6. Ejecutamos el comando "pip install -r ".\requirements.txt"
7. Para iniciar el localhost usaremos el comando python .\app\app.py

Nota: Si el sistema no esta habilitado la ejecucion de Scripts se debe ejecutar un PowerShell en modo administrador 
 y ejecutar el comando : " Set-ExecutionPolicy RemoteSigned ", al igual que se debe tener instalado: Microsoft C++ Build Tools que se lo puede descargar e instalar desde el siguiete link https://visualstudio.microsoft.com/es/visual-cpp-build-tools/


