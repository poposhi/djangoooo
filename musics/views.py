#要先Import 架構 httpresponse
from django.template.loader import get_template
from musics.models import Music #引入資料庫結構
from musics.serializers import MusicSerializer
from django.shortcuts import render  #回傳http用的
    #render的第三個是用context  ,A dictionary of values
from django.shortcuts import render_to_response
from rest_framework import viewsets
from .models import Post
import datetime
from datetime import datetime as dt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas #for web
from matplotlib.figure import Figure #for web

def hello_view(request):
    template = get_template('hello_django.html')

    try:
        facility_A = request.GET['facility_A']
    except:
        facility_A = 'exceptA'
    try:
        facility_B = request.GET['facility_B']
    except:
        facility_B = 'exceptB'

    html=template.render(locals())
    return HttpResponse(html)
    '''1214暫時遮蔽
    template = get_template('hello_django.html')
    #下面是要找出datetime的range，有一個__range的東西搞不懂，到底IMPORT到長DATETIME還是短DATETIME??
    #combine(date物件,時間) 所以現在要做出時間物件給combine
    #用完下面要把它分開，
    #COMBINEA =datetime(2017,10,15) #第一個arg需要date 物件 ，第二個需要 datetime.time
    rangea= dt(2017,11,3,10)#year, month, day, hour=0, minute=0, second=0, microsecond=0,#datetime.combine(COMBINEA, datetime.time(0,0))
    rangeb = dt(2017,11,3,23)# datetime.combine(COMBINEA, datetime.max))
    objecttttt = Post.objects.filter(name='test_facility_name_1103_z').filter(pub_date__range=(rangea,rangeb )) #用range再放入dt物件
    objecttttt_y = Post.objects.filter(name='test_facility_name_1103_y').filter(pub_date__range=(rangea,rangeb )) #用range再放入dt物件
    time_date = objecttttt.exists()
    #顯示queryset>>html
    #知道有幾個queryset  x軸是時間(小時，分) y軸是vavg
    long =objecttttt.count()
    #畫出來 1把所有vavg都放進去array ，x軸先用普通array
    vavg = np.zeros((long,1))#為了要疊代用21*1的矩陣
    vavg_y = np.zeros((long,1))#為了要疊代用21*1的矩陣
    timeee = np.zeros((long, 1))
    title ='object id'
    count=0
    for i in objecttttt:
        vavg[count]=i.Vavg
        timeee[count] =i.id
        count=count+1
        title=title+str(i.id)+','
    count=0
    for i in objecttttt_y:
        vavg_y[count] = i.Vavg
        count = count + 1
    fig = Figure()
    canvas = FigureCanvas(fig) #canvas是把figure 轉換後的物件
    ax = fig.add_subplot(111)
    x=timeee#new
    y =vavg
    y_y=vavg_y
    #ax.set_title(title)
    ax.set_ylabel('vavg')
    ax.set_xlabel(str(rangea)+' to '+str(rangeb) )
    #y = np.fromiter(posts, dtype=('i4'))  # 取出來是object
    ax.plot(x, y)
    ax.plot(x,y_y)
    response=django.http.HttpResponse(content_type='image/png')  #這個變數是用http傳圖片
    canvas.print_png(response) #讓他可以嵌入網頁

    #html=template.render(locals())
    #return HttpResponse(html)
    return response
'''
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


def post_test(request):
    from .models import Post
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from datetime import datetime as dt
    from django.shortcuts import render

    template = get_template('post_test.html')

    status_date = '還沒取資料'
    status_facility = '還沒取資料'  # 最後用exist當作狀態顯示
    a_exist = 99  # 99代表還沒做
    b_exist = 99
    try:  # 直接變成int
        start_month = int(request.GET['start_month'])
        start_day = int(request.GET['start_day'])
        start_hour = int(request.GET['start_hour'])
        end_month = int(request.GET['end_month'])
        end_day = int(request.GET['end_day'])
        end_hour = int(request.GET['end_hour'])
        status_date = 'get date ok'
        try:
            facility_A = request.GET['facility_A']
            a_exist = 1
        except:
            facility_A = 'null'
            a_exist = 0
        try:
            facility_B = request.GET['facility_B']
            b_exist = 1
        except:
            facility_B = 'null'
            b_exist = 0
    except:
        status_date = 'get date failure'
        html = template.render(locals())
        return HttpResponse(html)
    # fetch_Vavg_from_page =int(fetch_Vavg_from_page)
    # fetch_object = Post.objects.get(id=fetch_Vavg_from_page)
    a = int('2017')
    rangea = dt(a, start_month, start_day, start_hour)
    rangeb = dt(a, end_month, end_day, end_hour)
    # status ='正常的結束try'
    ''' 寫一個傳入兩個物件可以回傳圖的>>還沒寫'''

    fig = Figure()
    canvas = FigureCanvas(fig)  # canvas是把figure 轉換後的物件
    ax = fig.add_subplot(111)
    ax.set_ylabel('vavg')
    ax.set_xlabel(str(rangea) + ' to ' + str(rangeb))

    if (a_exist == 1):
        objecttttt = Post.objects.filter(name='facility_A').filter(
            pub_date__range=(rangea, rangeb))  # 用range再放入dt物件
        long = objecttttt.count()
        # 畫出來 1把所有vavg都放進去array ，x軸先用普通array
        vavg = np.zeros((long, 1))  # 為了要疊代用21*1的矩陣
        timeee = np.zeros((long, 1))
        title = 'object id'
        count = 0
        for i in objecttttt:
            vavg[count] = i.Vavg
            timeee[count] = i.id
            count = count + 1
            title = title + str(i.id) + ','
        x = timeee  # new
        y = vavg
        ax.plot(x, y,color='blue',label='facility_A')

    if (b_exist == 1):
        objecttttt_y = Post.objects.filter(name='facility_B').filter(
            pub_date__range=(rangea, rangeb))  # 用range再放入dt物件
        long = objecttttt.count()
        vavg_y = np.zeros((long, 1))  # 為了要疊代用21*1的矩陣
        timeee = np.zeros((long, 1))
        title = 'object id'
        count = 0
        for i in objecttttt_y:
            vavg_y[count] = i.Vavg
            count = count + 1
        x = timeee  # new
        y_y = vavg_y
        ax.plot(x, y_y,color='red',label='facility_B')

    ax.legend()
    response = django.http.HttpResponse(content_type='image/png')  # 這個變數是用http傳圖片
    canvas.print_png(response)  # 讓他可以嵌入網頁
    return response


'''
        # 知道有幾個queryset  x軸是時間(小時，分) y軸是vavg
        long = objecttttt.count()
        # 畫出來 1把所有vavg都放進去array ，x軸先用普通array
        vavg = np.zeros((long, 1))  # 為了要疊代用21*1的矩陣
        vavg_y = np.zeros((long, 1))  # 為了要疊代用21*1的矩陣
        timeee = np.zeros((long, 1))
        title = 'object id'
        count = 0
        for i in objecttttt:
            vavg[count] = i.Vavg
            timeee[count] = i.id
            count = count + 1
            title = title + str(i.id) + ','
        count = 0
        for i in objecttttt_y:
            vavg_y[count] = i.Vavg
            count = count + 1

        x = timeee  # new
        y = vavg
        y_y = vavg_y
 '''



def base_test(request):
    template = get_template('base_test.html')

    try:
        #if 'Vavg' in request.GET:
        fetch_Vavg_from_page = str( request.GET['Vavg'] )
    except:
        fetch_Vavg_from_page = '跑到except'

    html = template.render(locals())
    return HttpResponse(html)
    '''base 不需要的code
    if 'Vavg' in request.GET:
        return HttpResponse('Welcome!~'+request.GET['Vavg'])
    else:
        return render_to_response('base_test.html', locals())
    if 'user_name' in request.GET:
        return HttpResponse('Welcome!~'+request.GET['user_name'])
    else:
        return render_to_response('base_test.html',locals())'''''
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