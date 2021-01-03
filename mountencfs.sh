#!/bin/bash
mount="/home/peter/mounts/private"
encdir="/home/peter/pCloudDrive/pCloudSync/encrypted/"

if grep -qs "$mount" /proc/mounts; then
  echo "Encrypted drive is already mounted."
  echo "Unmount?"
  select yn in "No" "Yes"; do
    case $yn in
        No )  exit
              ;;
        Yes ) fusermount -u $mount
              if [ $? -eq 0 ]; then
                echo "Unmount successful."
              else
                echo "Unmount failed."
              fi
              break
              ;;
    esac
  done
else
  echo "Mounting encrypted drive..."
  encfs $encdir $mount
  if [ $? -eq 0 ]; then
    echo "success."
  else
    echo "fail."
  fi
  
fi
  

