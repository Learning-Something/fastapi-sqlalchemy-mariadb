variable "tags" {
  description = "The tags to add to the new instance."
  type = map(string)
}

variable "certificate_arn" {
  description = "The ARN of the certificate to use for the instance."
  type = string
}

variable "route_zone_id" {
  description = "The ID of the route table zone to use for the instance."
  type = string
}

variable "environment" {
  description = "The environment to use for the instance."
  type = string
}

variable "doppler_token" {
  description = "The token to use for the Doppler instance."
  type = string
}

variable "region" {
  description = "The region to use for the instance."
  type = string
}

variable "vpc_id" {
  description = "The ID of the VPC to use for the instance."
  type = string
}

variable "public_subnets" {
  description = "The IDs of the public subnets to use for the instance."
  type = list(string)
}

variable "account_id" {
  description = "The account id"
  type = string
}
