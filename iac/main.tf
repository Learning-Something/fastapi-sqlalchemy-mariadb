terraform {
  required_version  = ">= 1.1.0"

  backend "remote" {
    hostname = "app.terraform.io"
    organization = "NereSWE"

    workspaces {
      name = "terraform-aws"
    }
  }

  required_providers {
      aws = {
          source    = "hashicorp/aws",
          version   = "~> 3.27"
      }
  }
}

provider "aws" {
  # region  = "us-east-2"
  # profile = "nereswe"
}

module "common" {
  source = "./modules/common"

  certificate_arn   = var.certificate_arn
  environment       = var.environment
  vpc_id            = var.vpc_id
  public_subnet_ids = var.public_subnets

  tags              = var.tags
}

module "todo-list" {
  source = "./modules/todo-list"

  environment           = var.environment
  route_zone_id         = var.route_zone_id
  lb_dns_name           = module.common.lb_dns_name
  lb_zone_id            = module.common.lb_zone_id
  region                = var.region
  subnet_ids            = var.public_subnets
  doppler_token         = var.doppler_token
  alb_security_group_id = module.common.alb_security_group_id
  vpc_id                = var.vpc_id
  listener_arn          = module.common.listener_arn
  account_id            = var.account_id

  tags                  = var.tags

  depends_on            = [module.common]
}
