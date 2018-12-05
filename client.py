import asyncio
import grpc

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

from functools import partial

def get_call(loop, number):
    # open a gRPC channel
    channel = grpc.insecure_channel('localhost:50051')
    # create a stub (client)
    stub = calculator_pb2_grpc.CalculatorStub(channel)
    number = calculator_pb2.Number(value=number)
    response = stub.SquareRoot(number)
    print(response)
    return response

loop = asyncio.get_event_loop()

# tasks = asyncio.gather(get_call(loop, 5), get_call(loop, 4))
response = loop.run_in_executor(None, partial(get_call, loop, 9))
response = loop.run_in_executor(None, partial(get_call, loop, 4))
loop.run_until_complete(response)


# et voilà
