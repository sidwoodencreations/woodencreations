terraform {
  backend "s3" {
    bucket = "woodencreations-tfstate"
    key    = "terraform.tfstate"
    region = "af-south-1"
  }
}