from fabric.api import local

def test():
    local("./manage.py test my_app")

def commit(desc):
    local("git add -A && git commit -m %s" % desc)

def push(branch):
    local("git push origin %s" % branch)

def prepare_deploy(branch, desc):
    commit(desc)
    push(branch)