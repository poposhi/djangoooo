#要先Import 架構 httpresponse
from django.template.loader import get_template
from musics.models import Music #引入資料庫結構
from musics.serializers import MusicSerializer
from django.shortcuts import render  #回傳http用的
    #render的第三個是用context  ,A dictionary of values
from rest_framework import viewsets
from .models import Post
import datetime
from datetime import datetime as dt
def hello_view(request):

    template = get_template('hello_django.html')
    #休息一下，下面是要找出datetime的range，有一個__range的東西搞不懂，到底IMPORT到長DATETIME還是短DATETIME??
    #combine(date物件,時間) 所以現在要做出時間物件給combine
    #用完下面要把它分開，
    COMBINEA =datetime(2017,10,15) #第一個arg需要date 物件 ，第二個需要 datetime.time
    rangea= dt(2017,10,30,10)#year, month, day, hour=0, minute=0, second=0, microsecond=0,#datetime.combine(COMBINEA, datetime.time(0,0))
    rangeb = dt(2017,10,30,23)# datetime.combine(COMBINEA, datetime.max))
    objecttttt = Post.objects.filter(name='test_facility_name2').filter(pub_date__range=(rangea,rangeb )) #用range再放入dt物件
    time_date = objecttttt.exists()
    #顯示queryset>>html
    #知道有幾個queryset  x軸是時間(小時，分) y軸是vavg
    long =objecttttt.count()
    #畫出來 1把所有vavg都放進去array ，x軸先用普通array
    vavg = np.zeros((long,1))#為了要疊代用21*1的矩陣
    timeee = np.zeros((long, 1))
    count=0
    for i in objecttttt:
        vavg[count]=i.Vavg
        timeee[count] =i.id
        count=count+1

    fig = Figure()
    canvas = FigureCanvas(fig) #canvas是把figure 轉換後的物件
    ax = fig.add_subplot(111)
    x=timeee#new
    #x = np.arange(-2, 1.5, .01)
    y =vavg# np.sin(2 * x)

    #y = np.fromiter(posts, dtype=('i4'))  # 取出來是object
    ax.plot(x, y)
    response=django.http.HttpResponse(content_type='image/png')  #這個變數是用http傳圖片
    canvas.print_png(response) #讓他可以嵌入網頁
    return response

    #html=template.render(locals())
    #return HttpResponse(html)

# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import redirect
from datetime import datetime
from .models import Post
import pymysql .cursors
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
# Create your views here.
def homepage(request):
    template = get_template('index.html')
    id =1
    posts = Post.objects.all()
    posts2 = Post.objects.get(pk=3) #取出來是object
    #把取出來的string 轉成 array 再轉str(才能看)
    #fromstring 可以自己偵測
    #posts2_type =str(np.array(posts2.body,dtype=float))

    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='qwerqwer',
                                 db='test',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:  # 再給表格名 與資料名稱
        with connection.cursor() as cursor:
            cursor.execute("SELECT body FROM musics_post WHERE id = 7")
            data = cursor.fetchall()#知道 fetchall 是dic:[{'body': '[ 0.00000000e+00e++03]'}
            #data = np.array(cursor.fetchall().body, dtype=float) 先研究fetch all
            #id =data.id()
            aaaa=data[0]['body']  # 從fetchall 取出來的是list 再取出是dic再取出來是str
            #aaaa= ' '.join(map(bin, bytearray(aaaa, 'utf8')))
            #array =np.load(aaaa) #to binary type ' '.join(map(bin,bytearray(st,'utf8')))
            #array=np.asarray(aaaa,dtype =float)
            dddd =str(type(aaaa))#np.fromstring(aaaa, dtype=float))  用array就可以轉array
            '''fig = Figure()
            canvas = FigureCanvas(fig)  # canvas是把figure 轉換後的物件
            ax = fig.add_subplot(111)
            x = np.arange(0, 10000, 1)
            ax.plot(x, array)
            response = django.http.HttpResponse(content_type='image/png')  # 這個變數是用http傳圖片
            canvas.print_png(response)  # 讓他可以嵌入網頁'''

    finally:
        connection.close()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
import django
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from .models import Post
import numpy as np

def mplimage(request):


    #posts = Post.objects.all()
    vavg = np.zeros((21,1))#為了要疊代用21*1的矩陣
    for i in range(20,41):
        objecttt=Post.objects.get(id =i)
        vavg[i-20]=objecttt.Vavg
    #print(posts)
    #for i in posts:
    #   vavg[i.id]=i.Vavg


    #########################
    fig = Figure()
    canvas = FigureCanvas(fig) #canvas是把figure 轉換後的物件
    ax = fig.add_subplot(111)
    x=np.arange(21)#new
    #x = np.arange(-2, 1.5, .01)
    y =vavg# np.sin(2 * x)
    post2=Post.objects.get(pk=1)
    posts = Post.objects.all()

    #y = np.fromiter(posts, dtype=('i4'))  # 取出來是object
    ax.plot(x, y)
    response=django.http.HttpResponse(content_type='image/png')  #這個變數是用http傳圖片
    canvas.print_png(response) #讓他可以嵌入網頁
    return response