package main

import (
	"context"
	"gdp/protos/gdp"
	"log"
	"net"

	"google.golang.org/grpc"
)

type server struct {
	gdp.UnimplementedGdpDataServiceServer
}

func (s *server) GdpData(ctx context.Context, req *gdp.GdpDataRequest) (*gdp.GdpDataResponse, error) {
	data := []*gdp.GdpData{
		{Quarter: "test1", Number: 2019},
		{Quarter: "test2", Number: 2020},
		{Quarter: "test3", Number: 2021},
		{Quarter: "test4", Number: 2022},
		{Quarter: "test5", Number: 2023},
	}

	return &gdp.GdpDataResponse{Data: data}, nil
}

func main() {
	listener, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("Failed to listen: %v", err)
	}

	srv := grpc.NewServer()
	gdp.RegisterGdpDataServiceServer(srv, &server{})

	log.Println("gRPC server listening on port :50051")
	if err := srv.Serve(listener); err != nil {
		log.Fatalf("Failed to serve: %v", err)
	}
}
