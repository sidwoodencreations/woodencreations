resource "aws_instance" "SWC" {
  depends_on             = [aws_security_group.ec2_security_group]
  ami                    = "ami-0b7e05c6022fc830b"
  instance_type          = "t3.micro"
  vpc_security_group_ids = [aws_security_group.ec2_security_group.id]
  tags = {
    Name = "SidWoodenCreations"
  }
}