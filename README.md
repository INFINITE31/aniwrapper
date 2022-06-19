## A Simple python api wrapper

[API Here](https://anime-api.hisoka17.repl.co/)

### How to install
```
pip install aniwrapper
```

### How to use

This api has many endpoints and the wrapper uses them all.
For example if you want to generate an 'hug' image use can use;

```py
from aniwrapper import anime
anime hug(link=True)
#For generating a link of the image
```

OR

```py
from aniwrapper import anime
anime.hug(link=False)
#For generating the image
```

### However it also has nsfw endpoints

```py
from aniwrapper imprt nsfw
nsfw.hentai(link=True)
#Will generate a nsfw image
```


If you have any problems regarding this package mail me at work4infinite@gmail.com.
