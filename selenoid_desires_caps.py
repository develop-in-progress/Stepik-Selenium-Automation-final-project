import datetime as datetime

selenoid_chrome_caps = {
    "browserName": "chrome",
    "version": "87.0",
    "enableVNC": True,
    "enableVideo": True,
    "enableLog": True,
    "videoScreenSize": "1024x768",
    "videoName": f"Chrome {datetime.datetime.now()}.mp4",
    "logName": f"Chrome {datetime.datetime.now()}.log",
    "name": "Chrome",
    "tmpfs": {"/tmp": "size = 512m",
              "screenResolution": "2048x1024x24"
              }
}
selenoid_ff_caps = {
    "browserName": "firefox",
    "browserVersion": "83.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": True,
        "videoName": f"Firefox {datetime.datetime.now()}.mp4",
        "enableLog": True,
        "logName": f"Firefox {datetime.datetime.now()}.log",
    }
}

selenoid_chrome_caps_old = {
    "browserName": "chrome",
    "version": "86.0",
    "enableVNC": True,
    "enableVideo": True,
    "videoScreenSize": "1024x768",
    "videoName": f"Chrome {datetime.datetime.now()}.mp4",
    "name": "Chrome",
    "tmpfs": {"/tmp": "size = 512m",
              "screenResolution": "2048x1024x24"
              }
}
selenoid_ff_caps_old = {
    "browserName": "firefox",
    "browserVersion": "82.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}