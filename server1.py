import grpc
import DisStorage_pb2
import time
from concurrent import futures
import os

_ONE_DAY_IN_SECONDS = 60*60*24

class DsServer():
    def __init__(self):
        self.loginNum = 0
        self.loginDict = {}
        self.path = r"ServerDisk/1/"
        self.IP = '127.0.0.1'

    def usrLogin(self,request,context):
        if request.name=='__root__':
            self.loginDict[request.name]=1
            return DisStorage_pb2.loginInfo(
                loginFlag=1,
                IP=self.IP,
                accessNum = self.loginNum,
                mess = ''
            )
        if request.name in self.loginDict:
            return DisStorage_pb2.loginInfo(loginFlag=0,
                                            IP=self.IP,
                                            accessNum=self.loginNum,
                                            mess='You have logined')
        self.loginDict[request.name] = 1
        self.loginNum += 1
        return DisStorage_pb2.loginInfo(loginFlag = 1,
                                        IP = self.IP,
                                        accessNum=self.loginNum,
                                        mess = 'Login! you are the '+str(self.loginNum)+'th visitor\nServer time : '+time.strftime("%Y-%m-%d-%H:%M:%S",time.localtime(time.time()))+'\nIP : 127.0.0.1')

    def usrLogout(self,request,context):
        if request.name not in self.loginDict:
            return DisStorage_pb2.logoutInfo(logoutFlag=0,
                                             mess = 'Login First!')
        self.loginDict.pop(request.name)
        return DisStorage_pb2.logoutInfo(logoutFlag=1,
                                         mess='')

    def getFileList(self,request,context):
        if request.name in self.loginDict:
            lst = os.listdir(self.path)
            return DisStorage_pb2.fileList(fileNum=len(lst),
                                           nameList = lst,
                                           mess = '')
        else:
            return DisStorage_pb2.fileList(fileNum=-1,
                                           nameList = [],
                                           mess='Login First!')

    def uploadFile(self,request,context):
        blockCnt = 0
        s = ''
        filename = ''
        for each in request:
            if each.usrName not in self.loginDict:
                return DisStorage_pb2.fileInfo(fileName='',
                                               blockNum=-1,
                                               usrName=each.usrName,
                                               mess='Login First!')
            blockCnt+=1
            s += each.block
            filename = each.fileName
        f = open(self.path+filename,'wb')
        f.write(s)
        f.close()
        return DisStorage_pb2.fileInfo(fileName=filename,
                                       blockNum = blockCnt,
                                       usrName='done',
                                       mess = '')

    def downloadFile(self,request,context):
        if request.usrName not in self.loginDict:
            yield DisStorage_pb2.fileData(fileName='',
                                          block='',
                                          blockNum=-1,
                                          usrName='',
                                          mess='Login First!')
        else:
            flst = os.listdir(self.path)
            if request.fileName in flst:
                f = open(self.path+request.fileName,'rb');
                blockCnt=0
                while True:
                    s = f.readline()
                    blockCnt+=1
                    if s:
                        yield DisStorage_pb2.fileData(fileName=request.fileName,
                                                  block=s,
                                                  blockNum=blockCnt,
                                                  usrName=request.usrName,
                                                  mess='')
                    else:
                        break;
            else:
                yield DisStorage_pb2.fileData(
                    fileName = request.fileName,
                    block = '',
                    blockNum=-1,
                    usrName = request.usrName,
                    mess='file not exist'
                )


    def getState(self,request,context):
        if request.name!="__root__":
            return DisStorage_pb2.nodeState(
                usrs=[],
                mess='Permission Denied!'
            )
        return DisStorage_pb2.nodeState(
            usrs = self.loginDict.keys(),
            mess = ''
        )

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  DisStorage_pb2.add_DisServerServicer_to_server(DsServer(),server)
  server.add_insecure_port('[::]:50051')
  server.start()
  while True:
    order = raw_input("")
    if order=="exit":
        server.stop(0)
        break

if __name__ == '__main__':
  serve()
