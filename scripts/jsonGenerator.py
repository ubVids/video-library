import json
from os import listdir

def list_of_files(dirHere,ext):
    files = []
    for f in listdir(dirHere):
        if f.endswith('.' + ext):
            files.append(f)
    return (files)
fileArr = list_of_files('../dist', "mp4")
distName = "https://cdn.jsdelivr.net/gh/ubVids/video-library@latest/dist/"
sourceArray = []

for f in fileArr:
    source = f
    title = f.split('.mp4')[0]
    thumb = title+'.jpg'
    sourceArray.append({
        "source": distName+source,
        "thumb": distName+thumb,
        "title": title
    })

extraFunction = 'function randomNoRepeats(e){let t=e.slice(0);return function(){t.length<1&&(t=e.slice(0));let o=Math.floor(Math.random()*t.length),n=t[o];t.splice(o,1);let r=document.getElementById("video-source"),c=document.getElementById("content_video");return r.setAttribute("src",n.sources[0]),c.setAttribute("poster",n.thumb[0]),n}}let changeVideoSource=randomNoRepeats(sourceArray);changeVideoSource(),changeVideoSource();'

f = open("library.js", "w")
f.write("let sourceArray = "+ json.dumps(sourceArray))
f.write("\n"+extraFunction)
f.close()