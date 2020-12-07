import datetime

chrome_caps = {
    "browserName": "chrome",
    "version": "87.0",
    "enableVNC": True,
    "enableVideo": True,
    "videoScreenSize": "1024x768",
    "videoName": "{0}.mp4".format(datetime.datetime.now()),
    "name": "Chrome",
    "tmpfs": {"/tmp": "size = 512m",
              "screenResolution": "2048x1024x24"
              }
}
ff_caps = {
    "browserName": "firefox",
    "browserVersion": "83.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}
