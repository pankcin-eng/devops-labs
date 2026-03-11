#!/usr/bin/env bash
# Simple log backup script for DevOps lab
LOG_DIR="/var/log"
BACKUP_DIR="$HOME/backups"
mkdir -p "$BACKUP_DIR"
tar -czf "$BACKUP_DIR/logs-$(date +%Y%m%d-%H%M%S).tgz" "$LOG_DIR"/*.log
echo "Backup created: $BACKUP_DIR/logs-$(date +%Y%m%d-%H%M%S).tgz"
