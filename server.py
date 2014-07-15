#!/usr/bin/env python

import sys
sys.path.append('gen-py')

from helloworld import HelloWorld
from helloworld.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class HelloWorldHandler:
  def __init__(self):
    self.log = {}

  def ping(self):
    print "ping()"

  def sayHello(self):
    print "sayHello()"
    return "say hello from client"

  def sayMsg(self, msg):
    print "sayMsg(" + msg + ")"
    return "say " + msg + " from client"

handler = HelloWorldHandler()
processor = HelloWorld.Processor(handler)
socket = TSocket.TServerSocket(port=30303)
transport = TTransport.TBufferedTransportFactory()
protocol = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, socket, transport, protocol)

print "Starting python server..."
server.serve()
print "done!"