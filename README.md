# robotframework-mobileLibrary
RobotFramework-MobileLibrary is an modified library based on [robotframework-appiumlibrary](https://github.com/jollychang/robotframework-appiumlibrary), We add some fetures according to our project requirements.

Only support python 2.x.

## Install
### pip 
```pip install mobilelibrary```

### local
```
git clone  https://***
cd robotframework-mobilelibrary
python setup.py install

```

## Advenced Features
- **prefix** 
    - Add [ Mobile / Web ] prefix to distinguish the mobile/web library's KWs with each other.

- **KW Wrapper** 
    - Wrap detial inside the code.

- **auto scroll click** 
	- In some webview content,the element is out of screen.
    Mobile Click WebviewElement can auto scroll the target element into screen && click it.

- **generate Gif** 
	- Add a switch in library args.When fire up **mobile_gif='Ture'** in the library arguments.Test case's process gif will generate auto on the ${OUTPUT} dir.      


## Docs
[MobileLibrary](http://10.240.129.121/rfui/Mobile_Keywords.html)