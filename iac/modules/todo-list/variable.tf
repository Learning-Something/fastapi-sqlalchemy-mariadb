
variable "environment" {
  description = "The environment to deploy to"
  type = string
}

variable "route_zone_id" {
  description = "The route zone id"
  type = string
}

variable "lb_dns_name" {
  description = "The dns name of the load balancer"
  type = string
}

variable "lb_zone_id" {
  description = "The zone id of the load balancer"
  type = string
}

variable "doppler_token" {
  description = "The token to use for the Doppler instance."
  type = string
}

variable "region" {
  description = "The region to deploy to"
  type = string
}

variable "subnet_ids" {
  description = "The subnet ids to deploy to"
  type = list(string)
}

variable "tags" {
  description = "The tags to apply to the service"
  type = map(string)
}

variable "alb_security_group_id" {
  description = "The security group id to use for the load balancer"
  type = string
}

variable "vpc_id" {
  description = "The vpc id to deploy to"
  type = string
}

variable "listener_arn" {
  description = "The arn of the listener to use"
  type = string
}

variable "account_id" {
  description = "The account id to use for the load balancer roles"
  type = string
}
