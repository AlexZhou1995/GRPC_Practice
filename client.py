import grpc
import DisStorage_pb2
import os

def run():
    channel = grpc.insecure_channel("localhost:50050")
    stub = DisStorage_pb2.CtrServerStub(channel)
    usrName = ''
    pw = ''
    usrPath = r'ClientDisk/'
    while True:
        sin = raw_input("##:")
        if sin=='exit':
            break;
        if sin=='reconnect':
            try:
                channel = grpc.insecure_channel("localhost:50050")
                stub = DisStorage_pb2.CtrServerStub(channel)
                print 'reconnect done'
            except Exception as err:
                print err
        if sin=='login':
            usrName = raw_input('user name:')
            pw = raw_input('password:')
            res = stub.usrLogin(DisStorage_pb2.usrInfo(
                name = usrName,
                pw = pw,
                mess = ''
            ))
            if res.mess:
                print res.mess

        if sin=='logout':
            res = stub.usrLogout(DisStorage_pb2.usrInfo(
                name = usrName,
                pw = pw,
                mess = ''
            ))
            if res.mess:
                print res.mess
            else:
                print "order done"

        if sin=='ls':
            res = stub.getFileList(DisStorage_pb2.usrInfo(
                name = usrName,
                pw = pw,
                mess=''
            ))
            if res.mess:
                print res.mess
            else:
                print res.nameList
        if sin=='upload':
            fname = raw_input('file name:')
            f = open(usrPath+fname,'rb')
            cnt = 0
            lst = []
            while True:
                s = f.readline()
                cnt+=1
                if s:
                    lst.append(DisStorage_pb2.fileData(
                        fileName=fname,
                        block = s,
                        blockNum = cnt,
                        usrName = usrName,
                        mess = ''
                    ))
                else:
                    break;
            res = stub.uploadFile(lst)
            if res.mess:
                print res.mess
            else:
                print ('upload done')
        if sin=='download':
            fname=raw_input('file name:')
            cnt = 0
            downFlag=1
            f = open(usrPath+fname,'wb')
            for each in stub.downloadFile(DisStorage_pb2.fileInfo(
                fileName = fname,
                blockNum=0,
                usrName = usrName,
                mess = ''
            )):
                if each.mess:
                    print each.mess
                    f.close()
                    os.remove(usrPath+fname)
                    downFlag=0
                    break
                f.write(each.block)
                cnt+=1
            f.close()
            if downFlag==1:
                print "done"
        if sin=='node_info':
            res = stub.getNodeInfo(DisStorage_pb2.usrInfo(
                name=usrName,
                pw = pw,
                mess = ''
            ))
            if res.mess:
                print res.mess

if __name__ == "__main__":
    run()
