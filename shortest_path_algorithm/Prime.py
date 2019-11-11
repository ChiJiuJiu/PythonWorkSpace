MAX_VALUE = int(1e8)

class  Dis:
    def  __init__(self):
        self.path=None
        self.value=0
        self.visit=False

class  Graph_DG:


    def __init__(self, vex_num=6, edge_num=8):
        if not self.check_init(vex_num, edge_num):
            print('输入的数据有误，定点数为：{0}，边数为：{1}'.format(vex_num, edge_num))
            self.create_failed=True
            return
        self.create_failed=False
        self.vex_num=vex_num
        self.edge_num=edge_num
        self.arc=[[MAX_VALUE for _ in range(vex_num)] for _ in range(vex_num)]
        self.dis = []
        self.edge_list=[]

    def check_init(self,vexnum,edge):
        if vexnum<=0 or  edge<=0 or vexnum*(vexnum-1)//2<edge:
            return  False
        return  True



    def check_edge_value(self,start,end,weight):
        if start<0 or  end<0 or  start>=self.vex_num  or  end>=self.vex_num or  weight<0:
            return  False
        return  True


    def  create_graph_step(self,start,end,weight):
        print('起点：{0}，终点：{1},权重：{2}'.format(start, end, weight))
        while not self.check_edge_value(start, end, weight):
            print('输入的边的信息不合法，请重新输入')
            print(start, ' ', end, ' ', weight, ' ')
        self.arc[start][end] = weight
        self.arc[end][start]=weight   #对称矩阵
        self.edge_list.append((start,end,weight))


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

        my_creater.create_graph_step(0, 1, 7)
        my_creater.create_graph_step(0,5,5)
        my_creater.create_graph_step(1, 2,9)
        my_creater.create_graph_step(1,4,3)
        my_creater.create_graph_step(2, 3, 6)
        my_creater.create_graph_step(3,4,8)
        my_creater.create_graph_step(3,5,10)
        my_creater.create_graph_step(4,5,4)



        my_creater.graph_print()
        shortest_edge=my_creater.kruskal()
        print(shortest_edge)


        prime_edge=my_creater.prim(0)
        print(prime_edge)

        # my_creater.dijkstra(1)
        # my_creater.print_path()

    def kruskal(self):
        res=[]
        if  self.vex_num<=0 or  self.edge_num<self.vex_num-1:
            return   res
        self.edge_list.sort(key=lambda x:x[2])
        # print(self.edge_list)
        group=[[i]  for  i  in  range(self.vex_num)]
        for  i   in  range(self.edge_num):
            for  j   in  range(self.vex_num):
                if self.edge_list[i][0]  in  group[j]:
                    m=j
                if self.edge_list[i][1]  in  group[j]:
                    n=j
            if m!=n:
                res.append(self.edge_list[i])
                group[m]=group[m]+group[n]
                group[n]=[]
        return   res

    def prim(self,begin=0):
        res=[]
        if  self.vex_num<=0 or  self.edge_num<self.vex_num-1:
            return   res

        selected_node=[begin]
        candidate_node=[i for  i  in  range(1,self.vex_num)]
        while len(candidate_node)>0:
            start,end,min_weight=0,0,MAX_VALUE
            for  i  in  selected_node:
                for j   in  candidate_node:
                    if self.arc[i][j]<MAX_VALUE and  self.arc[i][j]<min_weight:
                        start=i
                        end=j
                        min_weight=self.arc[i][j]
            res.append((start,end,min_weight))
            selected_node.append(end)
            candidate_node.remove(end)


        return   res









    def graph_print(self):
        print('图的邻接矩阵为：')
        for  i  in  range(self.vex_num):
            for  j  in  range(self.vex_num):
                if self.arc[i][j]==MAX_VALUE:
                    print('∞',end=' ')
                else:
                    print(self.arc[i][j],end=' ')
            print()



    def print_path(self):
        for  i  in  range(self.vex_num):
            if self.dis[i].value==MAX_VALUE:
                print('{0}是无最短路径的'.format(self.dis[i].path))
            else:
                print('{0}最短路径是:{1}'.format(self.dis[i].path,self.dis[i].value))








if __name__ == '__main__':
    Graph_DG.create_graph_default()






