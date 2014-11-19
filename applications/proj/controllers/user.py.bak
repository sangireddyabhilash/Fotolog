# coding: utf8
# try something like
def login():
    f=dbhome().select(dbhome.viewpics.ALL)
    return dict(form=auth.login(),f=f)

def register():
    f=dbhome().select(dbhome.viewpics.ALL)
    return dict(form=auth.register(),f=f)

def index():
    f=dbhome().select(dbhome.viewpics.ALL)
    return dict(f=f)

@auth.requires_login()

def about():
    f=dbhome().select(dbhome.viewpics.ALL)
    #l={}
    p=db(db.auth_user.first_name==session.auth.user.first_name).select()
    #l[0]=p[0] + '.' + p[1] + '.' + p[2]
    #print 'p--->',p.displayimage
   # print 'user',session.auth.user.first_name
    return dict(f=f,p=p)

def friends():
    f1=db().select(db.auth_user.ALL)
    f=dbhome().select(dbhome.viewpics.ALL)
    return dict(f1=f1,f=f)

def upload():
    f=dbhome().select(dbhome.viewpics.ALL)
    form=SQLFORM(dbhome.pics)
    if form.process().accepted:
        response.flash = 'form accepted'
        dbhome(dbhome.pics.id == form.vars.id).update(name=session.auth.user.first_name)
        dbhome.commit()
    else:
        response.flash = 'please fill the form'
    return dict(f=f,form=form)

def grid():
    f=dbhome().select(dbhome.viewpics.ALL)
    cont=dbhome(dbhome.pics.name==request.args[0]).select()
    for i in cont:
        print i.image
    return dict(cont=cont,f=f)

def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, dbhome)
def download1():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

def display_form():
   form = SQLFORM(dbhome.pics,upload=URL('download'))
   if form.process().accepted:
       response.flash = 'form accepted'
   elif form.errors:
       response.flash = 'form has errors'
   return dict(form=form)
        
def vote():
    print 'req.vars',request.vars
    item=dbhome.post[request.vars.id]
    new_votes = item.likes + 1
    item.update_record(likes=new_votes)
    return str(new_votes)

def likes():
    input= request.get_vars['start']
    k1= list(input.split(','))[0]
    k2= list(input.split(','))[1]
    k3= list(input.split(','))[2]
    k4= list(input.split(','))[3]
    print 'type',k3
    print 'id',k1
    if k3=='pics' and k4=='1':
        dbhome(dbhome.pics.id==k1).update(likes=int(k2))
    else:
        dbhome(dbhome.post.id==k1).update(likes=int(k2))

def comments():
    form1=SQLFORM(dbhome.post)
    f=dbhome().select(dbhome.viewpics.ALL)
    if form1.process().accepted:
        response.flash = 'form accepted'
        dbhome(dbhome.post.id == form1.vars.id).update(author=session.auth.user.first_name)
        dbhome(dbhome.post.id == form1.vars.id).update(imgid=request.args[0])
        dbhome.commit()
    else:
        response.flash='form rejected'
    if len(request.args)==1:
        l= int(request.args[0])
        n1=1
        k=dbhome().select(dbhome.pics.ALL)
        post=dbhome().select(dbhome.post.ALL)
        comm={}
        for i in k:
            if int(i.id) == l:
                break
        for p in post:
            if int(p.imgid)==l :
                comm[n1]=p
                n1=n1+1
        sel1=dbhome(dbhome.post.imgid==request.args[0]).select()
    else:
        n1=1
        post=dbhome().select(dbhome.post.ALL)
        comm={}
        l= int(request.args[0])
        for i in post:
            if int(i.id) == l:
                break
        for p in post:
            if int(p.imgid)==l:
                comm[n1]=p
                n1=n1+1
        sel1=dbhome(dbhome.post.imgid==request.args[0]).select()
    return dict(form1=form1,k=i,comm=comm,sel1=sel1,f=f)
