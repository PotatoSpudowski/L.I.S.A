#!/bin/bash
nfc-poll>result.txt & 
sleep 2
pkill --signal SIGINT nfc