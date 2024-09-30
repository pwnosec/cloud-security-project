# Cloud Security Project Description
Solusi keamanan siber untuk infrastruktur cloud dengan fitur-fitur seperti pengaturan firewall, deteksi intrusi, enkripsi data, autentikasi user dengan 2FA, serta sistem logging dan monitoring. Proyek ini bertujuan untuk menyediakan solusi keamanan cloud dengan fitur-fitur berikut:
- Pengaturan firewall yang ketat
- Deteksi intrusi berbasis anomaly
- Enkripsi data dalam transit dan saat disimpan
- Sistem autentikasi user dengan otentikasi dua faktor
- Logging dan monitoring aktivitas keamanan

## Cara deploy
1. Install Terraform dan Python.
2. Setup infrastruktur dengan menjalankan `./scripts/deploy.sh`.
3. Monitor keamanan dengan script di `./scripts/monitor_alerts.sh`.

### Features:
- Secure firewall rules setup via Terraform.
- Intrusion Detection System (IDS) to identify unusual activities.
- Data encryption for sensitive information both at rest and in transit.
- User authentication system with password hashing and token-based verification.
- Two-factor authentication (2FA) for enhanced security.
- Logging and monitoring system to track user activities and potential threats.
