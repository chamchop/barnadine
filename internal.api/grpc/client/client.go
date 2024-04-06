package main

import (
	"context"
	"fmt"
	"gdp/protos/gdp"
	"log"

	"google.golang.org/grpc"
)

func main() {
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		log.Fatalf("Failed to connect to gRPC server: %v", err)
	}
	defer conn.Close()

	client := gdp.NewGdpDataServiceClient(conn)

	response, err := client.GdpData(context.Background(), &gdp.GdpDataRequest{})
	if err != nil {
		log.Fatalf("Error calling GdpData: %v", err)
	}

	for _, gdp := range response.GetData() {
		fmt.Printf("%s: %d\n", gdp.Quarter, gdp.Number)
	}
}
