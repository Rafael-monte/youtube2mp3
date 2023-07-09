# Dependencias
## youtube_dl:
Por algum motivo está dando problema na maneira habitual de instalação, por via das dúvidas usar:
```bash
pip install --upgrade --force-reinstall "git+https://github.com/ytdl-org/youtube-dl.git"
```
## FFMPEG
Para **Windows**: https://ffmpeg.org/download.html

Para linux:
```bash
sudo apt-get install ffmpeg
```

# Modo de usar
```bash
python main.py <arquivo-com-links>
```
**OBS** O arquivo com links deve ter apenas os links, com uma quebra de linha entre eles.
Exemplo:
```
https://www.youtube.com/watch?v=vabnZ9-ex7o
https://www.youtube.com/watch?v=Gp7rGy0UkYU
https://www.youtube.com/watch?v=iyu04pqC8lE
```
Os arquivos ficarão salvos em uma pasta chamada "output"