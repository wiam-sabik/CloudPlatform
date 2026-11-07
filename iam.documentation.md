# IAM Documentation - CloudPlatform

This document describes the AWS Identity and Access Management (IAM) setup for the CloudPlatform project: what was configured, why, how, and which features were limited by the AWS account type.

## 1. Context

- **Project:** CloudPlatform, a Flask monitoring API (CPU, RAM, disk, status) running in a Docker container on an AWS EC2 instance (Ubuntu).
- **Account type:** AWS Free plan created through the newer sign-up experience. The account is owned by an AWS Builder ID (there is no classic root user with an email and password), and it runs on free credits.
- **Goal:** apply least-privilege access and avoid storing credentials on the server.

## 2. Summary of what was built

| Item | Name | Purpose |
|---|---|---|
| MFA | Authenticator app on the AWS Builder ID | Protects the identity that owns the account |
| IAM role | `cloudplatform-ec2-role` | Gives the EC2 instance permissions without stored access keys |
| Managed policy | `CloudWatchAgentServerPolicy` | Lets the instance send metrics and logs to CloudWatch (used in the next phase) |
| Custom policy | `monitoring-readonly-policy` | Read-only visibility into EC2 and CloudWatch |
| IAM user | `viewer-test` | Practice identity with only the custom policy |

## 3. Implementation

### 3.1 MFA on the Builder ID

1. Opened the AWS Builder ID security page (Profile, then Security).
2. Chose **Register device** and selected an authenticator app.
3. Scanned the QR code, entered the verification code, and named the device.

**Why:** the Builder ID owns the account, so protecting it with a second factor is the highest-impact security step.

### 3.2 IAM role for the EC2 instance

1. IAM, then **Roles**, then **Create role**.
2. Trusted entity type: **AWS service**, use case: **EC2**.
3. Attached the managed policy `CloudWatchAgentServerPolicy` (and nothing else).
4. Named the role `cloudplatform-ec2-role`.
5. Attached it to the instance: EC2, then **Instances**, then **Actions**, then **Security**, then **Modify IAM role**.
6. Verified in the instance's **Security** tab that the IAM Role field shows `cloudplatform-ec2-role`.

**Why:** an EC2 instance that needs to call AWS services should use a role. The role provides temporary credentials automatically, so no access keys are written into code, environment files, or the repository.

### 3.3 Custom least-privilege policy

`monitoring-readonly-policy`:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ReadOnlyEC2AndCloudWatch",
      "Effect": "Allow",
      "Action": [
        "ec2:Describe*",
        "cloudwatch:Get*",
        "cloudwatch:List*",
        "cloudwatch:Describe*"
      ],
      "Resource": "*"
    }
  ]
}
```

**Design notes:**
- Every action is a read action (`Describe`, `Get`, `List`). There are no write, modify, or delete permissions.
- `"Resource": "*"` is used because these particular actions do not support restricting access to a single resource. The least-privilege control is in the **Action** list.

### 3.4 IAM user

- Created `viewer-test` with only `monitoring-readonly-policy`, attached directly to the user (user groups were unavailable, see section 4).
- No console access and no access keys were created.

**Why:** a read-only identity demonstrates a narrowly scoped permission set. It can be deleted at any time without affecting the project.

## 4. Limitations found on this account type

| Feature | What happened | Cause |
|---|---|---|
| IAM user groups | "Feature unavailable. To use this feature, activate advanced features." | Advanced features require upgrading to a paid plan first |
| IAM Access Analyzer | `access-analyzer:CreateAnalyzer` was denied, with the message that a service control policy explicitly denies the action | Organization-level service control policy applied to Free-plan accounts |
| Console login for IAM users | Not supported on this account type (IAM users are for programmatic use only, according to AWS documentation) | Account type design |

These are plan limits, not configuration mistakes. Upgrading is irreversible, requires a payment method, and removes spend limits, so it was deliberately not done for the sake of these features.

## 5. Concepts applied

- **Least privilege:** grant only the permissions needed for a task.
- **Roles instead of access keys:** services get temporary credentials, so there is nothing to leak or rotate.
- **Policies vs identities:** policies define permissions, and users or roles carry them.
- **MFA:** a second factor protects the identity that controls the account.

## 6. Security practices followed

- No access keys created for any user.
- No AdministratorAccess granted to any identity besides the account owner.
- No account IDs, keys, or secrets stored in this repository.
-SSH (port 22) restricted to a single IP in the instance’s security group.

## 7. Future work

- Add a custom policy limited to a single S3 bucket when S3 is added to the project.
- Revisit user groups and Access Analyzer if the account is upgraded in the future.
- Delete `viewer-test` once it is no longer needed.
