import yt_dlp

def download_video( video_url , output_folder="Downloads" ):
    print(f"Analysing video link :{video_url}....")

    options={
        'format':'bestvideo+bestaudio/best',
        'outtmpl':f'{output_folder}/%(title)s.%(ext)s',
        'quiet': False,
        'no_warnings': False,
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([video_url])
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)
    
