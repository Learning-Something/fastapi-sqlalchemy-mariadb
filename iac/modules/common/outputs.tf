output "lb_dns_name" {
  value = module.alb.lb_dns_name
  description = "ALB DNS Name"
}

output "lb_zone_id" {
  value = module.alb.lb_zone_id
  description = "ALB Zone ID"
}

output "alb_security_group_id" {
  value = aws_security_group.nereswe_alb_sg.id
  description = "ALB Security Group"
}

output "listener_arn" {
  value = module.alb.https_listener_arns[0]
  description = "ALB Listener ARN"
}
