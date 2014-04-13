#!/usr/bin/python

import web
import subprocess

urls = (
  '/status', 'status',
  '/(.*)', 'index'
)

app = web.application(urls, globals())

render = web.template.render('templates')

proc = None
mode = None

def stat():
    global proc
    global mode
    if proc is None:
        return 0
    if proc.returncode is None:
         return mode
    return 0
         

class index:
    def GET(self, inmode = None):
        global proc
        global mode
        if inmode is None or inmode == '':
            if stat():
                return render.invalid('Program is running in ' + mode + ' mode!')
            return render.index('')
        
        if stat():
            return render.invalid('Program is already running in ' + mode + ' mode!')
        if inmode == 'drum':
            mode = 'drum'
        elif inmode == 'theremin':
            mode = 'theremin'
        elif inmode == 'gesture':
            mode = 'gesture'
        else:
            return render.invalid('Unknown mode!')
        proc = subprocess.Popen(["/usr/bin/python", "/root/hack/code.py", mode])
        if stat():
            return render.valid('Program was successfully started in ' + mode + ' mode!')
        else:
            return render.index('Error: program wasn\'t started!')

class status:
    def GET(self):
        global proc
        global mode
        if stat():
            return render.invalid('Program is running in ' + mode + ' mode!')
        return render.index('')
    def POST(self):
        global proc
        global mode
        proc.terminate()
        proc.kill()
	proc = None
        if stat():
            return render.invalid('Program was not terminated!')
        return render.index('Program was stopped successfully!')


if __name__ == "__main__":
    app.run()
