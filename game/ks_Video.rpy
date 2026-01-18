default you_user_id = ""
default url ="https://www.kuaishou.com/rest/v/profile/feed"
default head = {"User-Agent":"python-request/3.11.0"}
default headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
    "Referer":"https://www.kuaishou.com/",
    "cookie":cookie,}
default cookie ="kpf=PC_WEB; clientid=3; did=web_e08af7f540b78c8784fea8aee6da5939; kwpsecproductname=kuaishou-vision; kwpsecproductname=kuaishou-vision; kwssectoken=6BxjTdPPQz40NRY6PaUVeB46R46LzTYEyrEYS/0uUZLMInzALuJ/PV6Gn7EQuSO19Mgxa3I0SRsJBTyE70txQA==; kwscode=010115ebdbcf3ecc11856a43173b231fc02feec25611dca95de06c689ceb16ea; userId=5156510492; kuaishou.server.webday7_st=ChprdWFpc2hvdS5zZXJ2ZXIud2ViZGF5Ny5zdBKwAcVjvZuAIWjNdQJMpnX09rIKR2qckYbjAFkCyG0ZWmmpblfNqDZ43P3RZjPJ_lxiyZwcgeWfJZjCInNMeqEtUgmXuK-4rKW4T_3WWRLiMdu1XmMCjURUxNmPiZLgAGs-s865PIIQNL5q-qFXQ1wIlfDeO9UUeQd_ECXSFAxc491owLM5KFX52lMeiCuk4fQGZ1hKdADgHDV3S1GOPtS38G-2G7VHPAp5HxytLK63cbnPGhJD7YlmW-_sv6V67wWUp_0VYZkiIKoWo58YkD_2V64TBDsIy2-SA7FySOX7stQBK54RfUbaKAUwAQ; kuaishou.server.webday7_ph=3e2552107008bba7678e82190e5b251d44df; kwfv1=PnGU+9+Y8008S+nH0U+0mjPf8fP08f+98f+nLlwnrIP9+Sw/ZFGfzY+eGlGf+f+e4SGfbYP0QfGnLFwBLU80mYGASY+nc9G/GM80YjPAY0G/GUwnz08eG7+Bz08eLlP0chPfHMwBc9+/PMweZEGnGMGAzY8fLh8/DEP/rU+/cA+Ar9+AQjP9Ll+fHhG0WFw/zf8/cMG0qlP9bfG9pf8/zSPI==; kwssectoken=iwC6CAtMsJYVEk9bH9MbOSQ0sECsBjKf3veIgW3IP/Z+cNsjK8Y76keUAmU61uS7sRTeYMTLa3w59zWHdKJA0w==; kwscode=221e9b74fd391ece5b7009f34d24ccb1e330605d70e7fcab17150fd8c6f4f944; ktrace-context=1|MS44Nzg0NzI0NTc4Nzk2ODY5LjY4OTczODM5LjE3Njg2NTk1MTcwOTkuMjY3ODM2MDc=|MS44Nzg0NzI0NTc4Nzk2ODY5Ljg1NTY1ODg2LjE3Njg2NTk1MTcwOTkuMjY3ODM2MDg=|0|webservice-user-growth-node|webservice|true|src-Js; kpn=KUAISHOU_VISION"

init python:
   
    import json
    import requests
    import os
    import re
    import ffmpeg
    import subprocess
    # global you_user_id

    # 获取用户id
    # you_user_id = ""
    # 请求头
    
    # head = {"User-Agent":"python-request/3.11.0"}
    

    # 函数1，请求体，遍历视频
    def ks ():
        # 全局变量
        global i 
        global ks_Title_baseUrl
        global ks_video_baseUrl
        global json

        # 把josn拿下来，防止报错
        # 请求体
        json = {"user_id":you_user_id,"pcursor":"","page":"profile"}
        response = requests.get(url=url, headers=headers , json=json)
        json_data = response.json()
        ks_video_baseUrl = json_data['feeds']
        ks_Title_baseUrl = json_data['feeds']
        for i,item in enumerate(ks_video_baseUrl): 
            # 遍历标题
            title = ks_Title_baseUrl[i]['photo']['caption']
            print_title= f"{i}" + f"--{title}"
            # 去除标题中的#号
            ks_title = re.sub(r'#.*$', '', print_title).strip()
            
    
    # 第二个函数，下载视频
    def ks_video_download (b):
        # 全局变量
        global Serialnumber_ks_Title_baseUrl
        global Serialnumber_ks_video_baseUrl
        global ks_Folder
        global ks_video_path
        global ks_output_path
        global ks_audio_path
        global ks_output_audio
        global Play_ks_video_path
        # 文件夹路径
        ks_Folder = renpy.config.gamedir
        # 下载用户所需的视频
        if 0 <= b <= i:
            # 选择标题作为文件名
            Choosed_title = ks_Title_baseUrl[b]['photo']['caption']
            Choose_ks_title = re.sub(r'#.*$', '', Choosed_title).strip()
            Serialnumber_ks_Title_baseUrl = Choose_ks_title
            # 遍历图片


            Serialnumber_ks_video_baseUrl=ks_video_baseUrl[b]['photo']['photoUrls'][1]['url']
            video = requests.get(url=Serialnumber_ks_video_baseUrl,headers=headers).content
            with open( ks_Folder+ f"/{Serialnumber_ks_Title_baseUrl}"+ f"{b}" + '.mp4', mode='wb') as v:
                v.write(video)
        else:
            pass
        
        # 最终视频输出路径
        ks_output_path = ks_Folder + f"/{Serialnumber_ks_Title_baseUrl}" + f"{b}" + '-编译后' + '.mp4'
        # 视频路径
        ks_video_path = ks_Folder + f"/{Serialnumber_ks_Title_baseUrl}" + f"{b}" + '.mp4'
        # 音频路径
        ks_audio_path = Serialnumber_ks_Title_baseUrl + f"{b}"+ ".mp3"
        # 音频输出路径
        ks_output_audio = ks_Folder + f"/{ks_audio_path}"
        # 编译后视频播放路径
        Play_ks_video_path = Serialnumber_ks_Title_baseUrl + f"{b}" + '-编译后' + '.mp4'
        
            
    # 第三个函数，视频编译
    def VideoCompilation():
        # 全局变量
        # 音频输入路径
        ffmpeg_ks_audio_path = ffmpeg.input(ks_Folder+f"/{ks_audio_path}")
        # 无声视频输出路径
        sv_ks_output_path = ks_video_path+"--无声视频" + ".mp4"
        # 无声视频输入路径
        ffmpeg_ks_video_path = ffmpeg.input(sv_ks_output_path)
        # 提取音频和无声视频
        subprocess.run(['ffmpeg', '-i', ks_video_path, '-c:v', 'copy', '-an', sv_ks_output_path])
        (
            ffmpeg
            .input(ks_video_path)
            .output(ks_output_audio,format='mp3',acodec="libmp3lame",b='192k')
            .overwrite_output()
            .run()
        )
        ffmpeg.output(ffmpeg_ks_video_path,ffmpeg_ks_audio_path, ks_output_path, vcodec="libvpx-vp9",acodec="libmp3lame").run()
   

