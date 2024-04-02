package main

import (
	"context"
	"log"
	"net"

	"google.golang.org/grpc"

	pb "barnardine/internal.api/protos/gdp" // Import generated Go code
)

type server struct {
}

func (s *server) GetTopFiveYears(ctx context.Context, req *pb.TopFiveYearsRequest) (*pb.TopFiveYearsResponse, error) {
	// Implement the logic to get the top five years
	// You can replace the sample data with your actual logic
	topFiveYears := []*pb.YearData{
		{Index: 1, Number: 2019},
		{Index: 2, Number: 2020},
		{Index: 3, Number: 2021},
		{Index: 4, Number: 2022},
		{Index: 5, Number: 2023},
	}

	return &pb.TopFiveYearsResponse{TopFiveYears: topFiveYears}, nil
}

func main() {
	listener, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("Failed to listen: %v", err)
	}

	srv := grpc.NewServer()
	pb.RegisterTopFiveYearsServiceServer(srv, &server{})

	log.Println("gRPC server listening on port :50051")
	if err := srv.Serve(listener); err != nil {
		log.Fatalf("Failed to serve: %v", err)
	}
}
