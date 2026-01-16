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
    scene daytime_shrine_outside 
    show 9
    e "你好，如果第一次使用请输入cookie，如果不知道怎么获取cookie请看{a=https://blog.csdn.net/weixin_44304729/article/details/150213074}如何获取B站cookie{/a}哦~"
    menu :
            "是第一次使用":
                call get_cookie from _call_get_cookie
                
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
