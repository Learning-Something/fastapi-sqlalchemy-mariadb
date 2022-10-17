/*
 * variables.tf
 * Common variables to use in various Terraform files (*.tf)
 */

# Name of the application. This value should usually match the application tag below.
variable "certificate_arn" {
  description = "Certificate ARN"
  type        = string
}

variable "tags" {
  description = "Tags"
  type        = map(string)
}

variable "environment" {
  description = "The environment to deploy to"
  type        = string
}

variable "vpc_id" {
  description = "The VPC ID"
  type        = string
}

variable "public_subnet_ids" {
  description = "The public subnet IDs"
  type        = list(string)
}
