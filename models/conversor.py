from re import match
import os
import youtube_dl
import pathlib
import threading


class Conversor:
    __PATTERNS: dict[str, str] = {
        "NAVIGATOR_REDUCED_PATTERN": "/v/",
        "REDUCED_URL_PATTERN": "youtu.be/",
        "NAVIGATOR_URL_PATTERN": "/watch?v="
    }
    __YOUTUBE_URL_REGEX: str='^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$'
    __YOUTUBE_DEFAULT_URL: str="https://www.youtube.com/watch?v="


    def install_from_file(self, file_path: str) -> None:
        links: list[str] = []
        with open(pathlib.Path(file_path)) as file:
            for line in file.readlines():
                links.append(line.strip())
        self.install_links(links)


    def install_links(self, links: list[str], output_directory: str = "output/") -> None:
        for link in links:
            threading.Thread(target=self.__download, args=(link, output_directory)).start()


    def __download(self, link: str, output_directory: str="output/") -> None:
        if not self.__is_youtube_url_valid(link):
            print(f'The following youtube link is invalid: {link}')
            return
        video_id = self.__extract_id_from_link(link)
        if not video_id:
            print(f'Couldn\'t extract video ID from link {link}')
            return
        try:
            print(f'Installing {link}...')
            music_name=self.__download_file_from_youtube(video_id, output_directory)
            print(f'Installed "{music_name}" successfully.')
        except Exception as exception:
            print(f'An error occoured while converting the following link: {link}\nError:{exception}')

    def __is_youtube_url_valid(self, youtube_url: str) -> bool:
        return match(self.__YOUTUBE_URL_REGEX, youtube_url)


    def __extract_id_from_link(self, link: str) -> str:
        for (_, pattern) in self.__PATTERNS.items():
            if pattern in link:
                return link.split(pattern)[1][:11]
        return None

    def __download_file_from_youtube(self, video_id: str, output_directory: str="/output") -> str:
        video_url = self.__YOUTUBE_DEFAULT_URL + video_id
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_directory, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            "quiet": True
        }
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        music_name=ydl.prepare_filename(ydl.extract_info(video_url, download=False))
        audio_file = os.path.join(output_directory, music_name)
        name=str(music_name)
        return name[name.index('/')+1: name.index('.')]