import grpc
import analysis_gdp_pb2 as gr
import analysis_gdp_pb2_grpc as gp

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = gp.GdpDataServiceStub(channel)
        
        response = stub.GdpData(gr.GdpDataRequest())
        
        print("Client received response:")
        for data in response.data:
            print(f"Quarter: {data.quarter}, Number: {data.number}")

if __name__ == '__main__':
    run()
