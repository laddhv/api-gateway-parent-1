#
# Copyright &copy; 2017 Dell Inc. or its subsidiaries. All Rights Reserved.
# Dell EMC Confidential/Proprietary Information
#
Summary: Dell Inc. API Gateway Service
Name: cpsd-api-gateway-service
Version: %_version
Release: %_revision
License: Commercial
Vendor: Dell Inc.
Group: System Environment/Dell Inc. Applications
URL: http://www.dell.com
Requires: jre >= 1.8.0

%define _use_internal_dependency_generator 0
%define __find_requires %{nil}

%description
Dell Inc. API Gateway Service


##############################################################################
# build
##############################################################################
%build

# Creates directory if it doesn't exist
# $1: Directory path
init_dir ()
{
    [ -d $1 ] || mkdir -p $1
}

##############################################################################
# check and create the common directories
##############################################################################
init_dir ${RPM_BUILD_ROOT}/usr/lib/systemd/system


##############################################################################
# check and create the root directory
##############################################################################
init_dir ${RPM_BUILD_ROOT}/opt/dell
init_dir ${RPM_BUILD_ROOT}/opt/dell/cpsd
init_dir ${RPM_BUILD_ROOT}/opt/dell/cpsd/api-gateway


##############################################################################
# check and create the directories for the service
##############################################################################

SERVICE_BUILD_ROOT=${RPM_BUILD_ROOT}/opt/dell/cpsd/api-gateway

init_dir ${SERVICE_BUILD_ROOT}
init_dir ${SERVICE_BUILD_ROOT}/install
init_dir ${SERVICE_BUILD_ROOT}/image
init_dir ${SERVICE_BUILD_ROOT}/image/api-gateway


##############################################################################
# copy the image to the required directory
##############################################################################
cp -r ${RPM_SOURCE_DIR}/target/dependency/api-gateway/* ${SERVICE_BUILD_ROOT}/image/api-gateway


##############################################################################
# copy the scripts to the install directory
##############################################################################
cp -rf ${RPM_SOURCE_DIR}/build/install.sh ${SERVICE_BUILD_ROOT}/install
cp -rf ${RPM_SOURCE_DIR}/build/remove.sh ${SERVICE_BUILD_ROOT}/install
cp -rf ${RPM_SOURCE_DIR}/build/upgrade.sh ${SERVICE_BUILD_ROOT}/install


##############################################################################
# copy the unit file
##############################################################################
cp ${RPM_SOURCE_DIR}/build/dell-api-gateway.service ${RPM_BUILD_ROOT}/usr/lib/systemd/system

cp -rf ${RPM_SOURCE_DIR}/target/dependency/api-gateway/docker-compose.yml ${SERVICE_BUILD_ROOT}/install/.

##############################################################################
# pre
##############################################################################
%pre
getent group dell >/dev/null || /usr/sbin/groupadd -f -r dell
getent passwd apigw >/dev/null || /usr/sbin/useradd -r -g dell -s /sbin/nologin -M apigw
exit 0


##############################################################################
# post
##############################################################################
%post
if [ $1 -eq 1 ];then
    echo "Installing Dell Inc. API Gateway components"
    /bin/sh /opt/dell/cpsd/api-gateway/install/install.sh
#elif [ $1 -eq 2 ];then
#    echo "Updating Dell Inc. API Gateway components"
#    /bin/sh /opt/dell/cpsd/api-gateway/install/upgrade.sh
else
    echo "Unexpected argument passed to API Gateway %post script: [$1]"
    exit 1
fi
exit 0


##############################################################################
# preun
##############################################################################
%preun
#if [ $1 -eq 0 ];then
#    echo "Removing Dell Inc. API Gateway components"
#    /bin/sh /opt/dell/cpsd/api-gateway/install/remove.sh
#fi
#exit 0

##############################################################################
# configure directory and file permissions
##############################################################################
%files

%attr(644,root,root) /usr/lib/systemd/system/dell-api-gateway.service

%attr(0754,apigw,dell) /opt/dell/cpsd/api-gateway/
%attr(0754,apigw,dell) /opt/dell/cpsd/api-gateway/install
%attr(0754,apigw,dell) /opt/dell/cpsd/api-gateway/image
%attr(0754,apigw,dell) /opt/dell/cpsd/api-gateway/image/api-gateway
