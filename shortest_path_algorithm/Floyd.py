MAX_VALUE = int(1e8)


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
        self.dis = [] ##距离
        self.path=[]  ##路径

    def check_init(self,vexnum,edge):
        if vexnum<=0 or  edge<=0 or vexnum*(vexnum-1)//2<edge:
            return  False
        return  True



    def check_edge_value(self,start,end,weight):
        if start<1 or  end<1 or  start>self.vexnum  or  end>self.vexnum or  weight<0:
            return  False
        return  True


    def  create_graph_step(self,start,end,weight,kind=2):
        print('起点：{0}，终点：{1},权重：{2}'.format(start, end, weight))
        while not self.check_edge_value(start, end, weight):
            print('输入的边的信息不合法，请重新输入')
            print(start, ' ', end, ' ', weight, ' ')
        self.arc[start - 1][end - 1] = weight
        if kind==2:  ##如果是无向图则对角矩阵赋值
            self.arc[end-1][start-1]=weight


    def  create_graph(self):
        print('请输入每条边的起点和终点（顶点编号从1开始）以及其权重')

        count=0
        while count<self.edge:
            start,end,weight=(int(i) for i in input().split())
            self.create_graph_step(start,end,weight)
            count+=1



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


    def  Floyd(self):
        for i  in  range(self.vexnum):
            step_dis=[]
            step_path=[]
            for j  in  range(self.vexnum):
                step_dis.append(self.arc[i][j])
                step_path.append(j)
            self.dis.append(step_dis)
            self.path.append(step_path)


        for k   in  range(self.vexnum):
            for i  in range(self.vexnum):
                for j  in  range(self.vexnum):
                    select=MAX_VALUE if self.dis[i][k]==MAX_VALUE or self.dis[k][j]==MAX_VALUE else (self.dis[i][k]+self.dis[k][j])
                    if self.dis[i][j]>select:
                        self.dis[i][j]=select
                        self.path[i][j]=self.path[i][k]



    def print_path(self):
        print('各个顶点对的最短路径：')
        for i  in  range(self.vexnum):
            for j  in  range(i+1,self.vexnum):
                base_format='v{0}---v{1},weight:{2},path:{3}'
                path_str='v{0}'.format(i+1)
                tmp=self.path[i][j]
                while tmp!=j:
                    path_str+='-->v{0}'.format(tmp+1)
                    tmp=self.path[tmp][j]
                path_str+='--v{0}'.format(j+1)
                print(base_format.format(i+1,j+1,self.dis[i][j],path_str))
            print()



    @classmethod
    def create_graph_default(cls):
        my_creater=Graph_DG(7,12)
        if my_creater.create_failed:
            return
        my_creater.create_graph_step(1,2,12)
        my_creater.create_graph_step(1,6,16)
        my_creater.create_graph_step(1,7,14)
        my_creater.create_graph_step(2,3,10)
        my_creater.create_graph_step(2, 6, 7)
        my_creater.create_graph_step(3, 4, 3)
        my_creater.create_graph_step(3, 5, 5)
        my_creater.create_graph_step(3, 6, 6)
        my_creater.create_graph_step(4, 5, 4)
        my_creater.create_graph_step(5, 6, 2)
        my_creater.create_graph_step(5, 7, 8)
        my_creater.create_graph_step(6, 7, 9)

        my_creater.graph_print()

        my_creater.Floyd()
        my_creater.print_path()






if __name__ == '__main__':
    Graph_DG.create_graph_default()






