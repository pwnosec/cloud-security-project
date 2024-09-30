resource "aws_kms_key" "my_key" {
  description             = "KMS key for encrypting data"
  deletion_window_in_days = 10
}

resource "aws_kms_alias" "my_key_alias" {
  name          = "alias/my_key"
  target_key_id = aws_kms_key.my_key.id
}

resource "aws_s3_bucket" "encrypted_bucket" {
  bucket = "my-encrypted-bucket"

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm     = "aws:kms"
        kms_master_key_id = aws_kms_key.my_key.id
      }
    }
  }
}
