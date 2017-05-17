#!/bin/bash
#
# Copyright (c) 2017 Dell Inc. or its subsidiaries.  All Rights Reserved.
# Dell EMC Confidential/Proprietary Information
#

echo "Installing Dell Inc. API Gateway components"

RETVAL=0

SERVICE_BASE=/opt/dell/cpsd/api-gateway

if [ ! -d "$SERVICE_BASE" ]; then
    echo "Could not find directory - [$SERVICE_BASE] does not exist."
    exit 1
fi

usermod -aG docker apigw

/bin/sh /opt/dell/cpsd/api-gateway/image/api-gateway/install.sh -s

systemctl enable dell-api-gateway

systemctl start dell-api-gateway

echo "Dell Inc. API Gateway components install has completed successfully."

exit 0
