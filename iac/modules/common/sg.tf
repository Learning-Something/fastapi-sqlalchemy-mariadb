resource "aws_security_group" "nereswe_alb_sg" {
  name        = "nereswe-production-alb-security-group"
  description = "Public security group"
  vpc_id      = var.vpc_id

  tags = var.tags
}

resource "aws_security_group_rule" "nsg_lb_ingress_rule" {
  description = "Allows SG to receive connections to all resources"
  type        = "ingress"
  from_port   = "0"
  to_port     = "0"
  protocol    = "-1"
  cidr_blocks = ["0.0.0.0/0"]

  security_group_id = aws_security_group.nereswe_alb_sg.id

  depends_on = [aws_security_group.nereswe_alb_sg]
}

resource "aws_security_group_rule" "nsg_lb_egress_rule" {
  description = "Allows SG to establish connections to all resources"
  type        = "egress"
  from_port   = "0"
  to_port     = "0"
  protocol    = "-1"
  cidr_blocks = ["0.0.0.0/0"]

  security_group_id = aws_security_group.nereswe_alb_sg.id

  depends_on = [aws_security_group.nereswe_alb_sg]
}
