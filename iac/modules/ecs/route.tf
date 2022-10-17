resource "aws_route53_record" "www" {
  zone_id = var.route_zone_id
  name    = var.domain
  type    = "A"

  alias {
    name                   = var.lb_dns_name
    zone_id                = var.lb_zone_id
    evaluate_target_health = true
  }
}
