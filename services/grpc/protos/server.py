from concurrent import futures
import grpc
import analysis_gdp_pb2 as g
import analysis_gdp_pb2_grpc as gr

class GdpDataServiceServicer(gr.GdpDataServiceServicer):
    def GdpData(self, request, context):
        data = [
            g.GdpData(quarter="Q1 2021", number=1000),
            g.GdpData(quarter="Q2 2021", number=1500),
            g.GdpData(quarter="Q3 2021", number=1600),
            g.GdpData(quarter="Q4 2021", number=1800),
        ]
        return g.GdpDataResponse(data=data)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gr.add_GdpDataServiceServicer_to_server(GdpDataServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('gRPC server listening on port :50051')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
