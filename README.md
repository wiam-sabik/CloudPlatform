# \## IAM \& Security

# \- MFA enabled on the AWS Builder ID that owns the account

# \- IAM role `cloudplatform-ec2-role` attached to the EC2 instance (CloudWatchAgentServerPolicy), so no access keys are stored on the server

# \- Custom least-privilege policy `monitoring-readonly-policy`: read-only access to EC2 and CloudWatch (Describe/Get/List actions only)

# \- Practice IAM user `viewer-test` with only that policy, no console access and no access keys

# \- Note: user groups and IAM Access Analyzer were unavailable on the Free-plan account (blocked by an organization service control policy)

