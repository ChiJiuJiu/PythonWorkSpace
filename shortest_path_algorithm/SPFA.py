from   queue  import  Queue
MAX_VALUE = int(1e8)

class  Dis:
    def  __init__(self):
        self.path=None
        self.value=0
        self.visit=False
        self.input_queue_time=0

class  Graph_DG:


    def __init__(self,vexnum=6,edge=8):
        if not self.check_init(vexnum,edge):
            print('输入的数据有误，定点数为：{0}，边数为：{1}'.format(vexnum,edge))
            self.create_failed=True
            return
        self.create_failed=False
        self.vexnum=vexnum
        self.edge=edge
        self.arc=[[MAX_VALUE for _  in  range(vexnum)] for _ in  range(vexnum)]
        self.dis = []



    def check_init(self,vexnum,edge):
        if vexnum<=0 or  edge<=0 or vexnum*(vexnum-1)//2<edge:
            return  False
        return  True



    def check_edge_value(self,start,end,weight):
        if start<1 or  end<1 or  start>self.vexnum  or  end>self.vexnum or  weight<0:
            return  False
        return  True


    def  create_graph_step(self,start,end,weight):
        print('起点：{0}，终点：{1},权重：{2}'.format(start, end, weight))
        while not self.check_edge_value(start, end, weight):
            print('输入的边的信息不合法，请重新输入')
            print(start, ' ', end, ' ', weight, ' ')
        self.arc[start - 1][end - 1] = weight


    def  create_graph(self):
        print('请输入每条边的起点和终点（顶点编号从1开始）以及其权重')

        count=0
        while count<self.edge:
            start,end,weight=(int(i) for i in input().split())
            self.create_graph_step(start,end,weight)
            count+=1

    @classmethod
    def create_graph_default(cls):
        my_creater=Graph_DG(6,8)
        if my_creater.create_failed:
            return
        my_creater.create_graph_step(1,3,10)
        my_creater.create_graph_step(1,5,30)
        my_creater.create_graph_step(1,6,100)
        my_creater.create_graph_step(2,3,5)
        my_creater.create_graph_step(3, 4, 50)
        my_creater.create_graph_step(4, 6, 10)
        my_creater.create_graph_step(5, 6, 60)
        my_creater.create_graph_step(5, 4, 20)

        my_creater.graph_print()

        my_creater.SPFA(1)
        my_creater.print_path()





    def  auto_create_graph(self,start,end,weight):
        print('起点：{0}，终点：{1},权重：{2}'.format(start, end, weight))
        while not self.check_edge_value(start, end, weight):
            print('输入的边的信息不合法，请重新输入')
            print(start, ' ', end, ' ', weight, ' ')
        self.arc[start - 1][end - 1] = weight





    def graph_print(self):
        print('图的邻接矩阵为：')
        for  i  in  range(self.vexnum):
            for  j  in  range(self.vexnum):
                if self.arc[i][j]==MAX_VALUE:
                    print('∞',end=' ')
                else:
                    print(self.arc[i][j],end=' ')
            print()

    def  SPFA(self,begin):
        self.begin=begin
        for i  in  range(self.vexnum):
            tmp_dis=Dis()
            tmp_dis.path='v{0}-->v{1}'.format(begin,i+1)
            tmp_dis.value=MAX_VALUE
            self.dis.append(tmp_dis)


        self.dis[begin-1].value=0
        self.dis[begin-1].visit=True
        self.dis[begin-1].input_queue_time+=1
        my_queue = Queue()
        my_queue.put(begin-1)


        while  not my_queue.empty():
            cur_vertix=my_queue.get()
            self.dis[cur_vertix].visit=False
            for i  in  range(self.vexnum):
                if  self.arc[cur_vertix][i]!=MAX_VALUE and \
                    self.dis[cur_vertix].value+self.arc[cur_vertix][i]<self.dis[i].value:
                    self.dis[i].value=self.dis[cur_vertix].value+self.arc[cur_vertix][i]
                    self.dis[i].path='{0}-->v{1}'.format(self.dis[cur_vertix].path,i+1)
                    if not self.dis[i].visit:
                        self.dis[i].visit=True
                        self.dis[i].input_queue_time+=1
                        my_queue.put(i)
                        if self.dis[i].input_queue_time>self.vexnum:
                            print('图中有负环')
                            return





    def print_path(self):
        print('以v{0}为起点的图的最短路径为：'.format(self.begin))
        for  i  in  range(self.vexnum):
            if self.dis[i].value==MAX_VALUE:
                print('{0}是无最短路径的'.format(self.dis[i].path))
            else:
                print('{0}最短路径是:{1}'.format(self.dis[i].path,self.dis[i].value))

        for  i  in  range(self.vexnum):
            print('顶点进入队列的次数为：',self.dis[i].input_queue_time)








if __name__ == '__main__':
    Graph_DG.create_graph_default()






