terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "4.62.0"
    }
  }
}

provider "aws" {
  # Configuration options
  shared_config_files      = ["~/.aws/config"]
  shared_credentials_files = ["~/.aws/credentials"]
  profile                  = "default"
}

# uses env var: "TF_VAR_avail_zone"
# variable "avail_zone" {}

variable "environment" {
  description = "Deployment Environment"
  type = string
}

variable "cidr_blocks" {
  description = "CIDR Blocks for VPC & Subnets"
  type = list(object({
    cidr_block = string
    name = string
  }))
}

resource "aws_vpc" "dev-vpc" {
    cidr_block = var.cidr_blocks[0].cidr_block
    
    tags = {
      Name = var.cidr_blocks[0].name
    }
}

resource "aws_subnet" "dev-subnet-1" {
    vpc_id = aws_vpc.dev-vpc.id
    #cidr_block = "10.0.1.0/24"
    cidr_block = var.cidr_blocks[1].cidr_block
    availability_zone = "eu-central-1c"
    
    tags = {
      Name = var.cidr_blocks[1].name
    }
}

data "aws_vpc" "existing_vpc" {
    default = true
}

resource "aws_subnet" "dev-subnet-2" {
    vpc_id = data.aws_vpc.existing_vpc.id
    cidr_block = var.cidr_blocks[2].cidr_block
    availability_zone = "eu-central-1b"
    
    tags = {
      Name = var.cidr_blocks[2].name
    }
}

output "dev-vpc-id" {
    value = aws_vpc.dev-vpc.id
}

output "dev-subnet-id" {
    value = aws_subnet.dev-subnet-1.id
}

output "dev-vpc-cidr_block" {
    value = aws_vpc.dev-vpc.cidr_block
}

output "dev-subnet-cidr_block" {
    value = aws_subnet.dev-subnet-1.cidr_block
}