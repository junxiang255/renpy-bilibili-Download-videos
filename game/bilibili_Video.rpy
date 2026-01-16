init python:
    import json
    import requests
    import re
    import os
    import ffmpeg

    cookie = persistent.input_cookie
    url = "https://www.bilibili.com"
    head = {"User-Agent":"python-request/3.11.0"}
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
            "Referer":"https://www.bilibili.com/",
            "cookie":cookie,}
            
    def bilibili (bilibili_av):
        global title
        global output_path
        global title
        global bilibili_Folder
        bil_url = url + f"/{bilibili_av}"
        #请求和标题
        response = requests.get(url=bil_url, headers=headers)
        html = response.text
        title = re.findall('title="(.*?)"',html)[0]
        info = re.findall('window.__playinfo__=(.*?)</script>', html)[0]
        json_data = json.loads(info)


        #解析视频和音频url
        video_baseUrl= json_data['data']['dash']['video'][0]['baseUrl']
        audio_baseUrl = json_data['data']['dash']['audio'][0]['baseUrl']
        # 下载视频和音频
        video = requests.get(url=video_baseUrl, headers=headers).content
        audio= requests.get(url=audio_baseUrl, headers=headers).content
        # 文件夹路径
        bilibili_Folder = renpy.config.gamedir
        # 保存视频和音频
        with open(bilibili_Folder + f"/{title}" + '.mp4', mode='wb') as v:
            v.write(video)
        with open(bilibili_Folder+ f"/{title}"+ '.mp3', mode='wb') as a:
            a.write(audio)
        # 合并视频和音频
        
        
        video_path = ffmpeg.input(bilibili_Folder + f"\{title}" + '.mp4')
        audio_path = ffmpeg.input(bilibili_Folder+ f"\{title}"+ '.mp3')
        output_path = bilibili_Folder +  f"\{title}" +"合并" +'.avi'
        global renpy_output_path 
        renpy_output_path = title + "合并.avi"
        Encoder = ""
        if mpeg4 == True:
            Encoder = "mpeg4"
        elif vp9 == True:
            Encoder = "libvpx-vp9"
        elif h264 == True:
            Encoder = "libx264"
            

        ffmpeg.output(video_path, audio_path, output_path, vcodec=Encoder, acodec="pcm_s16le").run()
        
        return 
    
        
    
    