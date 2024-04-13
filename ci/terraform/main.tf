provider "aws" {
  region  = "eu-west-2"
}

resource "aws_db_instance" "barnardine_dev" {
  identifier         = "barnardine-dev"
  engine             = "postgres"
  engine_version     = "12.4"
  instance_class     = "db.t3.micro" 
  allocated_storage  = 20 

  db_subnet_group_name = "default" 
  username             = var.postgres_username
  password             = var.postgres_password

  vpc_security_group_ids = [data.aws_security_group.remote_server.id]

  publicly_accessible = true
  skip_final_snapshot = true 

  tags = {
    Name = "barnardine-dev psql"
  }
}

data "aws_security_group" "remote_server" {
  name = "remote-server"
}