#!/bin/sh
#
# Copyright (c) 2017 Dell Inc. or its subsidiaries.  All Rights Reserved.
# Dell EMC Confidential/Proprietary Information
#

CONTAINERID=$(basename "$(cat /proc/1/cpuset)" | cut -c 1-12)
java -Xms64m -Xmx192m -cp /opt/dell/cpsd/api-gateway/lib/* -Dspring.profiles.active=production -Dcontainer.id=$CONTAINERID -jar /opt/dell/cpsd/api-gateway/lib/api-gateway.jar

