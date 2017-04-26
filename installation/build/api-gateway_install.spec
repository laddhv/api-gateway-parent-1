#
# Copyright &copy; 2017 Dell Inc. or its subsidiaries. All Rights Reserved.
# Dell EMC Confidential/Proprietary Information
#
Summary: Dell Inc. API Gateway Installer
Name: cpsd-api-gateway-service
Version: %_version
Release: %_revision
License: Commercial
Vendor: Dell Inc.
Group: System Environment/Dell Inc. Applications
URL: http://www.dell.com

%define _use_internal_dependency_generator 0
%define __find_requires %{nil}

%description
Dell Inc. API Gateway installer


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

##############################################################################
# check and create the directories for the service
##############################################################################
SERVICE_BUILD_ROOT=${RPM_BUILD_ROOT}/opt/dell/api-gateway

init_dir ${SERVICE_BUILD_ROOT}
init_dir ${SERVICE_BUILD_ROOT}/install
init_dir ${RPM_BUILD_ROOT}/usr/lib/systemd/system

##############################################################################
# copy the service script and logrotate to the respective directory
##############################################################################


##############################################################################
# copy the scripts to the required directories
##############################################################################


##############################################################################
# copy the configuration to the conf directory
##############################################################################


##############################################################################
# copy the logs configuration to the conf directory
##############################################################################


##############################################################################
# copy the install scripts
##############################################################################
cp -rf ${RPM_SOURCE_DIR}/build/install/* ${SERVICE_BUILD_ROOT}/install
cp -rf ${RPM_SOURCE_DIR}/usr/lib/systemd/system/* ${RPM_BUILD_ROOT}/usr/lib/systemd/system
cp -rf ${RPM_SOURCE_DIR}/opt/dell/api-gateway/install/docker-compose.yml ${SERVICE_BUILD_ROOT}/install

##############################################################################
# copy the libs to the required directories
##############################################################################


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
    /bin/sh /opt/dell/api-gateway/install/api-gateway_install.sh
#elif [ $1 -eq 2 ];then
#    echo "Updating Dell Inc. API Gateway components"
#    /bin/sh /opt/dell/api-gateway/install/api-gateway_upgrade.sh
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
#    /bin/sh /opt/dell/api-gateway/install/api-gateway_remove.sh
#fi
#exit 0

##############################################################################
# configure directory and file permissions
##############################################################################
%files

%attr(0754,apigw,dell) /opt/dell/api-gateway/
%attr(0754,apigw,dell) /opt/dell/api-gateway/install/

%config(noreplace) /usr/lib/systemd/system/api-gateway-services.service
%config(noreplace) /opt/dell/api-gateway/install/docker-compose.yml