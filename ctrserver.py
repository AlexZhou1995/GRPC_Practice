import grpc
import DisStorage_pb2
import time
from concurrent import futures
import os
import copy

_ONE_DAY_IN_SECONDS = 60*60*24


class CtrServer():
    def __init__(self):
        self.loginNum = 0
        self.activeNum = 0
        self.DisServerNum=3
        self.loginDict = {}
        self.IP = '127.0.0.10'
        self.DisServerStress = [0,0,0]
        self.stubs = [0,0,0]
        self.linkNodes()
        self.flstAll, self.flsts, self.paths = self.updateFileList()
        self.sync()
        print self.flstAll

    def linkNodes(self):
        try:
            channel = grpc.insecure_channel("localhost:50051")
            self.stubs[0]=DisStorage_pb2.DisServerStub(channel)
        except Exception as err:
            print 'linkNodes: can not connect to node 1'

        try:
            channel = grpc.insecure_channel("localhost:50052")
            self.stubs[1]=DisStorage_pb2.DisServerStub(channel)
        except Exception as err:
            print 'linkNodes: can not connect to node 2'

        try:
            channel = grpc.insecure_channel("localhost:50053")
            self.stubs[2]=DisStorage_pb2.DisServerStub(channel)
        except Exception as err:
            print 'linkNodes: can not connect to node 3'
        accessCnt = 0
        for i in range(0,self.DisServerNum):
            try:
                res = self.stubs[i].usrLogin(DisStorage_pb2.usrInfo(
                    name = '__root__',
                    pw = '__root__',
                    mess = ''
                ))
                if res.mess:
                    print res.mess
                else:
                    accessCnt+=1
            except Exception as err:
                print 'linkNode: can not login to node %d'%i
        print "link to %d DiskServer"%accessCnt

    def updateFileList(self):
        path = [r"ServerDisk/1/",r"ServerDisk/2/",r"ServerDisk/3/"]
        flsts = []
        flstAll = []
        for i in range(0,self.DisServerNum):
            flsts.append(os.listdir(path[i]))
            flstAll.extend(os.listdir(path[i]))
        flstAll = list(set(flstAll))
        return flstAll,flsts,path

    def sync(self,param='ALL'):
        #info sync
        if param=='ALL':
            self.loginDict={}
            for i in range(0,self.DisServerNum):
                try:
                    res = self.stubs[i].getState(DisStorage_pb2.usrInfo(
                    name = '__root__',
                    pw = '__root__',
                    mess=''
                ))
                    if res.mess:
                        print res.mess
                    else:
                        self.DisServerStress[i] = len(res.usrs)-1
                        for each in res.usrs:
                            self.loginDict[each]=i
                except Exception as err:
                    print 'sync: can not connect to node %d'%i
        #data sync
        for i in range(0,self.DisServerNum):
            try:
                tmp = list(set(self.flstAll)-set(self.flsts[i]))
                if tmp:
                    for each in tmp:
                        for j in range(0,self.DisServerNum):
                            if each in self.flsts[j]:
                                fp = open(self.paths[j]+each,'rb')
                                blockCnt = 0
                                lst = []
                                while True:
                                    s = fp.readline()
                                    if not s:
                                        break;
                                    blockCnt += 1
                                    lst.append(DisStorage_pb2.fileData(
                                        fileName = each,
                                        block=s,
                                        blockNum = blockCnt,
                                        usrName = '__root__',
                                        mess = ''
                                    ))
                                res = self.stubs[i].uploadFile(lst)
                                if res.mess:
                                    print res.mess
            except Exception as err:
                print 'sync: can not connect to node %d'%i
        return None

    def usrLogin(self,request,context):
        for i in range(0,self.DisServerNum):
            if self.DisServerStress[i]<5:
                res = self.stubs[i].usrLogin(request);
                if res.loginFlag==1:
                    self.loginNum += 1
                    self.activeNum += 1
                    self.loginDict[request.name] = i
                    self.DisServerStress[i]+=1
                return res
        return DisStorage_pb2.loginInfo(
            loginFlag = 0,
            IP = '-1',
            accessNum=-1,
            mess='no free node'
        )

    def usrLogout(self,request,context):
        if request.name not in self.loginDict:
            return DisStorage_pb2.logoutInfo(
                logoutFlag=0,
                mess = 'Login First!'
            )
        res = self.stubs[self.loginDict[request.name]].usrLogout(request)
        if res.logoutFlag==1:
            self.DisServerStress[self.loginDict[request.name]]-=1
            self.loginDict.pop(request.name)
            self.activeNum-=1
        return res

    def getFileList(self,request,context):
        self.flstAll, self.flsts, self.paths = self.updateFileList()
        if request.name in self.loginDict:
            return DisStorage_pb2.fileList(fileNum=len(self.flstAll),
                                           nameList = self.flstAll,
                                           mess = '')
        else:
            return DisStorage_pb2.fileList(fileNum=-1,
                                           nameList = [],
                                           mess='Login First!')

    def uploadFile(self,request,context):
        blockCnt=0
        uname = ''
        fname = ''
        lst = []
        for each in request:
            fname = each.fileName
            uname = each.usrName
            if each.usrName not in self.loginDict:
                return DisStorage_pb2.fileInfo(
                    fileName='',
                    blockNum=-1,
                    usrName = each.usrName,
                    mess = 'Login First'
                )
            else:
                lst.append(DisStorage_pb2.fileData(
                    fileName = each.fileName,
                    block = each.block,
                    blockNum = each.blockNum,
                    usrName = '__root__',
                    mess = each.mess
                ))
        try:
            res=self.stubs[self.loginDict[uname]].getState(DisStorage_pb2.usrInfo(
                name = '__root__',
                pw = '__root__',
                mess=''
            ))
            res = self.stubs[self.loginDict[uname]].uploadFile(lst)
        except Exception as err:
            print 'can not connect to node %d'%self.loginDict[uname]
            for i in range(0,self.DisServerNum):
                try:
                    res=self.stubs[i].getState(DisStorage_pb2.usrInfo(
                        name='__root__',
                        pw='__root__',
                        mess=''
                    ))
                    res = self.stubs[i].uploadFile(lst)
                    print 'change to node %d, upload done'%i
                    break
                except Exception as err:
                    print 'can not connect to node %d'%i

        if res.mess:
            print res.mess
        else:
            self.flstAll,self.flsts,self.paths = self.updateFileList()
            self.sync()
            return res

    def downloadFile(self,request,context):
        self.flstAll,self.flsts,self.paths = self.updateFileList()
        self.sync('dataOnly')

        if request.usrName not in self.loginDict:
            yield DisStorage_pb2.fileData(fileName='',
                                          block='',
                                          blockNum=-1,
                                          usrName='',
                                          mess='Login First!')
        else:
            try:
                res = self.stubs[self.loginDict[request.usrName]].getState(DisStorage_pb2.usrInfo(
                    name='__root__',
                    pw = '__root__',
                    mess=''
                ))
                for each in self.stubs[self.loginDict[request.usrName]].downloadFile(request):
                    yield DisStorage_pb2.fileData(
                        fileName = each.fileName,
                        block = each.block,
                        blockNum = each.blockNum,
                        usrName = each.usrName,
                        mess = each.mess
                    )
            except Exception as err:
                print 'download: can not connect to node %d'%self.loginDict[request.usrName]
                for i in range(0,self.DisServerNum):
                    try:
                        res = self.stubs[i].getState(DisStorage_pb2.usrInfo(
                            name='__root__',
                            pw='__pw__',
                            mess=''
                        ))
                        print 'change to node %d'%i
                        for each in self.stubs[i].downloadFile(DisStorage_pb2.fileInfo(
                            fileName = request.fileName,
                            blockNum = request.blockNum,
                            usrName = '__root__',
                            mess = request.mess
                        )):
                            yield DisStorage_pb2.fileData(
                                fileName = each.fileName,
                                block = each.block,
                                blockNum = each.blockNum,
                                usrName = request.usrName,
                                mess = each.mess
                            )
                        break
                    except Exception as err:
                        print 'download: can not connect to node %d'%i



    def getNodeInfo(self,request,context):
        if request.name not in self.loginDict:
            return DisStorage_pb2.nodeInfo(
                mess='Login First'
            )
        else:
            nodeID = self.loginDict[request.name]
            s = 'You are now in node '+str(nodeID)
            s += '\nThis node have '+str(self.DisServerStress[nodeID])+' active users\n'
            s += 'All node active users: '
            for i in range(0,self.DisServerNum):
                s+=str(self.DisServerStress[i])
                s+=', '
            return DisStorage_pb2.nodeInfo(
                mess = s[:-1]
            )

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=15))
  DisStorage_pb2.add_CtrServerServicer_to_server(CtrServer(),server)
  server.add_insecure_port('[::]:50050')
  server.start()
  while True:
    order = raw_input("")
    if order=='exit':
        server.stop(0)
        break

if __name__ == '__main__':
  serve()
