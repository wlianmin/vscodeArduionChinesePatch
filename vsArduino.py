import os

base_dir=os.environ['USERPROFILE']+"\\.vscode\\extensions\\"
path=""

aa=os.listdir(base_dir)
for dir in aa:
    if dir.find("vsciot-vscode.vscode-arduino")>-1:
        
        path=base_dir+dir+"\\out\\src\\common\\util.js"
        print("PATH="+path)

        tmp=""
        with open(path,'r+') as f:
            tmp=f.readlines()
            for i in range(0,len(tmp)):
                if tmp[i].find("os.platform() === \"win32\"")>-1:
                    print("got it")
                    tmp[i]=tmp[i].replace("os.platform() === \"win32\"","0")
                    break
            f.seek(0)
            f.writelines(tmp)