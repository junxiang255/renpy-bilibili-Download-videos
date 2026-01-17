define e = Character("九条都")
image 9:
    "images/9_np (1).png"
    zoom 0.5
    yanchor 0.55
image daytime_shrine_outside:
    "images/daytime_shrine_outside.png"
    zoom 1.5
define input_bilibili_av = ""
define persistent.input_cookie = ""
define mpeg4 = False
define vp9 = False
define h264 = False
# 游戏在此开始。

label start:
    $ renpy.movie_cutscene("111.mp4")

    scene daytime_shrine_outside 
    show 9
    e "选择你要下载的视频平台"
    menu:
        "B站":
            pass
        "快手"  :
            jump ks_video
        
    e "你好，如果第一次使用请输入cookie，如果不知道怎么获取cookie请看{a=https://blog.csdn.net/weixin_44304729/article/details/150213074}如何获取B站cookie{/a}哦~"
    menu :
            "是第一次使用":
                call get_cookie 
                
            "不是第一次使用":
                pass
    e "选择编码器"
    menu:
        "mpeg4---快速，质量低":
            $ mpeg4 = True
        "libvpx-vp9----质量中，速度中":
            $ vp9 = True
        "H.264-----质量高，速度快，但无法在renpy里播放":
            $ h264 = True
    e "你好，欢迎使用bilibili视频下载器！"
    e "请输入视频bv号来下载视频吧~"
    $ input_bilibili_av = renpy.input("请输入bilibili视频av号：")
    $ renpy.say(e,"视频下载中...")
    python:
        bilibili(input_bilibili_av)
        
    
    e "视频保存到了[output_path]里哦~"
    jump video
    return 



label video:
    scene daytime_shrine_outside
    show 9
    e "[renpy_output_path]"
    $ renpy.movie_cutscene(renpy_output_path)
    return 



                
                
label get_cookie:
    scene daytime_shrine_outside
    $ persistent.input_cookie  = renpy.input("请输入你的B站cookie：")


label ks_get_cookie:
    scene daytime_shrine_outside
    $ persistent.input_ks_cookie  = renpy.input("请输入你的快手cookie：")
    return




label ks_video:
    scene daytime_shrine_outside
    show 9
    

    e "你好，欢迎使用快手视频下载器！"
    e "快手的cookie由作者junxiang233提供"
    e "请勿滥用，谢谢合作~"
    $ you_user_id  = renpy.input("请输入你要下载的用户id:")


    e "正在获取视频列表...id:[you_user_id]"
    $ ks()
    $ nov = int( renpy.input("一共有0-[i]视频，你要观看第几个视频:"))
    $ ks_video_download(nov)
    e "视频保存到了游戏目录里哦~"
    menu:
        "编译视频（因为爬取的视频renpy不支持）":
            jump ks_video_Play
        "不编译":
            pass
    
    return 

label ks_video_Play:
    scene daytime_shrine_outside
    show 9
    e "正在编译视频..."
    $ VideoCompilation()
    e "[ks_output_path]"
    $ renpy.movie_cutscene(Play_ks_video_path)
    return

