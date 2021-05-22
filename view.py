import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from pymysql import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import smtplib
import email.message


def makeConnections():
    return connect(host='127.0.0.1', user='root', password='', database='rssnewsfeed',
                   cursorclass=cursors.DictCursor)


def login(request):
    if 'admin' in request.session:
        return redirect('dashboard')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['Password']
        query = f"select `email`, `username`, `name`, `mobile`, `type` from admin where email='{email}' and password='{password}'"
        conn = makeConnections()
        cr = conn.cursor()
        cr.execute(query)
        resut = cr.fetchall()
        print(resut)
        if len(resut) > 0:
            request.session['admin'] = resut[0]
            return redirect('dashboard')
        else:
            messages.warning(request, 'invalid Email or Password !!!')
            return redirect('loginPage')
    return render(request, 'adminWork/login.html')


def dashboard(request):
    if 'admin' not in request.session:
        return redirect('loginPage')
    return render(request, 'adminWork/index.html')


def signout(request):
    try:
        del request.session['admin']
    except:
        pass
    return redirect('loginPage')


def changePassword(request):
    """
    in this function we are workin for change password
    :param request:
    :return :
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        oldPassword = request.POST.get('oldPassword')
        newPassword = request.POST.get('newPassword')

        query = f"select * from admin where email='{email}' and password='{oldPassword}'"
        conn = makeConnections()
        cr = conn.cursor()
        cr.execute(query)
        resut = cr.fetchall()
        if len(resut) > 0:
            query = "UPDATE `admin` SET `password`='{}' WHERE `email`='{}'".format(newPassword, email)
            cr.execute(query)
            conn.commit()
            conn.close()
            messages.success(request, "Successfully Update password")

            return redirect('changePassword')
        else:
            messages.warning(request, 'Plz enter correct old Password!!!')
            return redirect('changePassword')
    return render(request, 'adminWork/changePassword.html')


# Category Work started
def addcateogry(request):
    if 'admin' not in request.session:
        return redirect('loginPage')
    return render(request, 'adminWork/AddCategory.html')


def addCategoryAction(request):
    if 'admin' not in request.session:
        return redirect('loginPage')
    name = request.GET['name']
    description = request.GET['description']

    query = "select * from category where name ='{}'".format(name)
    conn = makeConnections()
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    if len(result) > 0:
        messages.warning(request, 'All ready Exists {}'.format(name))
    else:
        query = "insert into category values('{}','{}')".format(name, description)
        cr.execute(query)
        conn.commit()
        messages.success(request, 'Success Fully Added {}'.format(name))
    return redirect('addcateogry')


def viewCategory(request):
    if 'admin' not in request.session:
        return redirect('loginPage')
    query = 'select * from category'
    conn = makeConnections()
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    return render(request, 'adminWork/viewCategory.html', {'data': result})


def editCategoryPage(request):
    if 'admin' not in request.session:
        return redirect('loginPage')
    name = request.GET['name']
    query = "select * from category where name ='{}'".format(name)
    conn = makeConnections()
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchone()
    return render(request, 'adminWork/editCategory.html', {'data': result})


def editCategoryAction(request):
    if 'admin' not in request.session:
        return redirect('loginPage')
    name = request.GET['name']
    description = request.GET['description']
    query = f"UPDATE `category` SET `description`='{description}' WHERE `name`='{name}'"
    conn = makeConnections()
    cr = conn.cursor()
    cr.execute(query)
    conn.commit()
    messages.success(request, 'Success Fully Update {}'.format(name))
    return redirect('viewCategory')


def deletCategroy(request):
    if 'admin' not in request.session:
        return redirect('loginPage')
    name = request.GET['name']
    query = "DELETE FROM `category` WHERE name='{}'".format(name)
    conn = makeConnections()
    cr = conn.cursor()
    cr.execute(query)
    conn.commit()
    messages.warning(request, 'Delete Successfully {}'.format(name))
    return redirect('viewCategory')


# end category work

# Add News
def addNewsPage(request):
    conn = makeConnections()
    query = "select name from category"
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()

    if request.method == 'POST':
        category = request.POST['category']
        title = request.POST['title']
        photo = request.FILES['photo']
        shortDesc = request.POST['shortDesc']
        description = request.POST['description']
        description = description.replace("'", "789987")
        description = description.replace('"', "789#987")
        print(category, title, shortDesc, description)
        create_at = datetime.datetime.now()

        fs = FileSystemStorage()
        filename = fs.save('news/' + photo.name, photo)
        query = f"INSERT INTO `news`(`title`, `photo`, `shortDescription`, `description`, `catName`, `created_at`) VALUES ('{title}','{filename}','{shortDesc}','{description}','{category}','{create_at}')"
        conn = makeConnections()
        cr = conn.cursor()
        cr.execute(query)
        conn.commit()
        messages.success(request, 'Success Fully Added {}'.format(title))

    return render(request, 'adminWork/addnews.html', {'data': result})


def viewNews(request):
    query = "SELECT `id`, `title`, `shortDescription`, `description`, `catName`, `created_at` FROM `news` "
    conn = makeConnections()
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    return render(request, 'adminWork/viewNews.html', {'data': result})


def deleteNews(request, id):
    query = "DELETE FROM `news` WHERE id='{}'".format(id)
    conn = makeConnections()
    cr = conn.cursor()
    cr.execute(query)
    conn.commit()
    messages.warning(request, 'Delete Success Fully!!!')
    return redirect('viewNews')


def viewNewsDescription(request):
    id = request.GET['id']
    query = "SELECT `id`, `title`, `shortDescription`, `description`, `catName`, `created_at` FROM `news` where id='{}'".format(
        id)
    conn = makeConnections()
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    description = result[0]['description'].replace("789987", "'")
    description = description.replace("789#987", '"')
    result[0]['description'] = description
    return render(request, 'adminWork/adminViewNewsDescription.html', {'data': result[0]})


def addNewsVedio(request):
    id = 'No'
    if 'id' in request.GET:
        id = request.GET['id']

    if id == 'No':
        query = "select * from videos"
    else:
        query = "select * from videos where id='{}'".format(id)

    conn = makeConnections()
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()

    for row in result:
        description = row['description'].replace("789987", "'")
        description = description.replace("789#987", '"')
        row['description'] = description
    return render(request, 'adminWork/newsVedio.html', {'id': id, 'data': result})


def addNewsVedioAction(request):
    id = request.GET.get('id')
    description = request.GET['description']
    description = description.replace("'", "789987")
    description = description.replace('"', "789#987")
    youTubeLink = request.GET['youTubeLink']
    print(id, description, youTubeLink)
    if id is not None:
        query = f"INSERT INTO `videos`(`description`, `YouTubeLink`, `newsid`) VALUES ('{description}','{youTubeLink}','{id}')"
    else:
        query = f"INSERT INTO `videos`(`description`, `YouTubeLink`) VALUES ('{description}','{youTubeLink}')"
    print(query)
    conn = makeConnections()
    cr = conn.cursor()
    cr.execute(query)
    conn.commit()
    messages.success(request, 'SuccessFully Added Vedio.')
    return redirect('addNewsVedio')


def deleteNewsVedio(request):
    id = request.GET['id']
    query = "DELETE FROM `videos` WHERE id='{}'".format(id)
    conn = makeConnections()
    cr = conn.cursor()
    cr.execute(query)
    conn.commit()
    messages.success(request, 'Vedio Delete Success Fully')
    return redirect('addNewsVedio')


# end of add news


# User InterFace
import rssFeed


def Home(request):
    if 'cat' in request.GET:
        news = rssFeed.trending(request.GET['cat'])
    else:
        news = rssFeed.trending('/')

    # category work
    query = "SELECT * FROM `category`"
    conn = makeConnections()
    cr = conn.cursor()
    cr.execute(query)
    cateogry = cr.fetchall()

    # AutoMobiles
    AutoMobiles = rssFeed.trending('AutoMobiles')

    # Tech
    techNews = rssFeed.trending('Tech')

    # Top Trending
    TopTrendingnews = rssFeed.trending('/')
    TopTrendingnews = TopTrendingnews[:12]

    # International
    International = rssFeed.trending('International')

    # video
    query = "SELECT * FROM `videos`"
    conn = makeConnections()
    cr = conn.cursor()
    cr.execute(query)
    video = cr.fetchall()
    for row in video[:8]:
        description = row['description'].replace("789987", "'")
        description = description.replace("789#987", '"')
        row['description'] = description

    # my news
    query = "SELECT * FROM `news`"
    cr.execute(query)
    myNews = cr.fetchall()
    for row in myNews:
        description = row['description'].replace("789987", "'")
        description = description.replace("789#987", '"')
        row['description'] = description

    content = {
        'techNews': techNews,
        'TopTrendingnews': TopTrendingnews,
        'International': International,
        'video': video,
        'myNews': myNews,
    }
    return render(request, 'users/index.html', content)


def viewMyNews(request):
    id = request.GET['id']
    query = "SELECT `id`, `title`, `shortDescription`, `description`, `catName`, `created_at` FROM `news` where id='{}'".format(
        id)
    conn = makeConnections()
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    description = result[0]['description'].replace("789987", "'")
    description = description.replace("789#987", '"')
    result[0]['description'] = description
    return render(request, 'users/viewmyNews.html', {'data': result[0]})


def navbarCategoryNews(request):
    cat = request.GET['cat']

    result = rssFeed.trending(cat)

    content = {
        'result': result[:4]
    }
    return JsonResponse(content)


def vedioNews(request):
    query = "SELECT * FROM `videos`"
    conn = makeConnections()
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    return render(request, 'users/newVideo.html', {'results': result})


def checkthis(name, emails, phone, subject, msgs):
    receiver = 'aashimab19@gmail.com'
    username = 'Admin'
    mobile = '6280995201'

    sender = 'python.vmm.2020@gmail.com'
    password = 'PythonVmm2021'

    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.login(sender, password)
    print("-----> Hello")
    body = f"""
                <html>
                <head>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                </head>
                <body>
                    <table  width="100%" cellpadding="0" cellspacing="0" bgcolor="e4e4e4"">
                    <tr>
                        <td>Name: </td>
                        <td> {name}</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td>Email: </td>
                        <td>{emails}</td>
                    </tr>
                    <tr>
                        <td></td>
                        <td>Phone: </td>
                        <td>{phone}</td>
                    </tr>
                    <tr>
                        <td></td>
                        <td>Subject: </td>
                        <td>{subject}</td>
                    </tr>
                    <tr>
                        <td></td>
                        <td>Message: </td>
                        <td>{msgs}</td>
                    </tr>
                </table>
            </body>
                """

    print(email.message.Message())
    msg = email.message.Message()
    msg['Subject'] = 'Rss News Feed'

    msg['From'] = sender
    msg['To'] = receiver
    password = password
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body)

    smtpserver.sendmail(sender, receiver, msg.as_string())
    print('Sent')
    smtpserver.close()
    return True



def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        msg = request.POST['msg']
        result = checkthis(name=name, emails=email, phone=phone, subject=subject, msgs=msg)
        if result:
            messages.success(request, 'Thank you we will reach you soon')
        else:
            messages.success(request, 'Fail due to some Tech ishu!!!!')
        return redirect('contactus')
    return render(request, 'users/contact.html')
