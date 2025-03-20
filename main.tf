provider "aws" {
  region = "us-west-1" 
}

resource "aws_vpc" "my_vpc" {
  cidr_block = "10.0.0.0/16"
  enable_dns_support = true
  enable_dns_hostnames = true
}

resource "aws_subnet" "my_subnet" {
  vpc_id     = aws_vpc.my_vpc.id
  cidr_block = "10.0.1.0/24"
  map_public_ip_on_launch = true
}

resource "aws_security_group" "my_sg" {
  vpc_id = aws_vpc.my_vpc.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "my_instance" {
  ami             = "ami-004374a3d56f732a6"
  instance_type   = "t2.micro"
  subnet_id       = aws_subnet.my_subnet.id
  vpc_security_group_ids = [aws_security_group.my_sg.id]  # Correct argument

  tags = {
    Name = "Myfirst_Terraform_Instance"
  }
}


