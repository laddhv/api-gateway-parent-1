#!/bin/bash
#
# Copyright © 2016 Dell Inc. or its subsidiaries. All Rights Reserved.
# Dell Confidential/Proprietary Information
#

RETVAL=0

SERVICE_BASE=/opt/dell/api-gateway

echo "Installing API Gateway service."

if [ ! -d "$SERVICE_BASE" ]; then
    echo "Could not find directory - [$SERVICE_BASE] does not exist."
    exit 1
fi

systemctl enable api-gateway-services
systemctl start api-gateway-services

echo "Dell Inc. API Gateway install has completed successfully."

exit $RETVAL