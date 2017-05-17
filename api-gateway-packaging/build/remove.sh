#!/bin/bash
#
# Copyright (c) 2017 Dell Inc. or its subsidiaries.  All Rights Reserved.
# Dell EMC Confidential/Proprietary Information
#

echo "Removing Dell Inc. API Gateway components"

systemctl stop dell-api-gateway

systemctl disable dell-api-gateway

/bin/sh /opt/dell/cpsd/api-gateway/image/api-gateway/remove.sh

echo "Dell Inc. API Gateway components removal has completed successfully."

exit 0
