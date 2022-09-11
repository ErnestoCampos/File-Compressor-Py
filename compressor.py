from PIL import Image # Para manipular los archivos de imagen
import os # Nos permite acceder a la carpeta de descargas y leer los archivps

download_folder = r"C:/Users/campo/OneDrive/Escritorio/Archivos/" # Declaramos cual es la direccion de nuestra carpeta de desacargas 
pictures_folder = r"C:/Users/campo/OneDrive/Escritorio/Archivos/Fotos/" # Declaramos la carpeta en la que se guardaran los archivos

if __name__ == "__main__": # Sentencia que sirve para verificar si estamos corriendo el script en nuestro equipo
    for filename in os.listdir(download_folder): # Por cada archivo de la carpeta de descargas 
        name, extension = os.path.splitext(download_folder + filename) # separa el nombre del archivo de su extension y guardalo en 2 variables

        if extension in [".jpg",".png",".jpeg"]: # Si el archivo es jpg, png o jpeg
            picture = Image.open(download_folder + filename) #Abre el archivo de la imagen
            picture.save(pictures_folder + "c-" + filename, optimize=True, quality=50) #Y guardalo en la carpeta de pictures como c-nombre del archivo optimizado con una calidad especifica
            os.remove(download_folder + filename) # borra el original

        if extension in [ ".3gpp" ]: # Si el archivo es un video
            video_folder = r"C:/Users/campo/OneDrive/Escritorio/Archivos/Videos/"
            os.rename ( download_folder + filename , video_folder + filename ) # Muevelo a otra carpeta
        
        if extension in [ ".pdf" ]: # Si el archivo es PDF
            pdf_folder = r"C:/Users/campo/OneDrive/Escritorio/Archivos/PDF/"
            os.rename ( download_folder + filename , pdf_folder + filename ) # Muevelo a otra carpeta 
            