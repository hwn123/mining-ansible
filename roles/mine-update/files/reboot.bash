#!/bin/bash
logger -t miner Forced restart
echo 1 > /proc/sys/kernel/sysrq 
echo b > /proc/sysrq-trigger
