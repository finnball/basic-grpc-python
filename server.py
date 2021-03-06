import grpc
from concurrent import futures
import time

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# import the original calculator.py
import calculator

import asyncio
import concurrent

import async_hack

# create a class to define the server functions
# derived from calculator_pb2_grpc.CalculatorServicer
class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):

    def __init__(self, loop):
        self.__loop = loop
        super().__init__()

    # calculator.square_root is exposed here
    # the request and response are of the data types
    # generated as calculator_pb2.Number
    async def SquareRoot(self, request, context):
        #task = asyncio.ensure_future(__square_root(request, context))
        #response = self.__square_root(request, context)
        print(request)
        response = calculator_pb2.Number()
        response.value = await calculator.square_root(request.value)
        return response

    def __square_root(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.square_root(request.value)
        return response

# create a gRPC server
#server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
loop = asyncio.get_event_loop()
server = grpc.server(async_hack.AsyncioExecutor(loop=loop))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the created server

calculator_pb2_grpc.add_CalculatorServicer_to_server(
        CalculatorServicer(loop), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
