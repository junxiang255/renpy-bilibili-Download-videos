screen ks_screens:
    python:
        import json
        import requests
        import os
        import re
        import ffmpeg
        import subprocess
        
        json = {"user_id":you_user_id,"pcursor":"","page":"profile"}
        response = requests.get(url=url, headers=headers , json=json)
        json_data = response.json()
        ks_Title_baseUrl = json_data['feeds']
        Title_List=[]
        for screen_i,item in enumerate(ks_Title_baseUrl):
            # 遍历标题
            screen_title = ks_Title_baseUrl[screen_i]['photo']['caption']
            screen_print_title= f"{screen_i}" + f"--{screen_title}"
            # 去除标题中的#号
            screen_ks_title = re.sub(r'#.*$', '', screen_print_title).strip()
            Title_List.append(screen_ks_title)
        

           
    frame:
        
        
        left_margin 100
        viewport:
            scrollbars "vertical"
            mousewheel True
        at Graduallyappear
        xpos 800
        ypos 100
        vbox:
            # viewport:
            #     draggable True
            for title in Title_List:
                text title
            
                

        


   

    
    


    pass