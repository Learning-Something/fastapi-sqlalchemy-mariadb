module "ecs" {
  source = "../ecs"

  app = "todo-list"
  environment = var.environment
  spot = true
  ecs_cpu = 256
  ecs_memory = 512
  image = "854605138489.dkr.ecr.us-east-2.amazonaws.com/nereswe/todo-list:latest"
  container_port = 5000
  container_env = [
    {
      "name": "DOPPLER_TOKEN",
      "value": var.doppler_token
    }
  ]
  region = var.region
  replicas = 1
  subnet_ids = var.subnet_ids
  logs_retention_in_days = 7
  tags = var.tags
  deregistration_delay = 300
  health_check = "/"
  health_check_matcher = "200"
  health_check_interval = 30
  health_check_timeout = 5
  route_zone_id = var.route_zone_id
  domain = "todo-list.nereswe.com"
  lb_dns_name = var.lb_dns_name
  lb_zone_id = var.lb_zone_id
  alb_security_group_id = var.alb_security_group_id
  vpc_id = var.vpc_id
  listener_arn = var.listener_arn
  assign_public_ip = true
  account_id = var.account_id
}
