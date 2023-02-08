provider "aws" {
    region = var.aws_region
}

# Centralizar o arquivo de controle de estado do terraform
terraform {
  backend "s3" {
    bucket = "terraform_bucket_state"
    key    = "path_state/terraform.tfstate"
    region = "us-east-2"
  }
}