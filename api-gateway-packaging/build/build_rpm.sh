#!/bin/bash
#
# Copyright &copy; 2017 Dell Inc. or its subsidiaries. All Rights Reserved.
# Dell EMC Confidential/Proprietary Information
#

# script to create RPM file which contains anything needed for installing and
# running the service

REL_VER=$1

echo "Build Number - ${BUILD_NUMBER}"

if [ -z "${BUILD_NUMBER}" ]; then
    SVN_REVISION=$2
else
    SVN_REVISION=${BUILD_NUMBER}
fi

TARGET_DIR=${PWD}/target
BUILD_ROOT=${TARGET_DIR}/rpmbuild

[ -d ${BUILD_ROOT} ] || mkdir -p ${BUILD_ROOT}

ARCH=x86_64

if [ -z "${GPG_PASSPHRASE}" ]; then
    rpmbuild -bb build/api-gateway.spec --buildroot ${BUILD_ROOT} --target ${ARCH}-linux --define "_topdir ${BUILD_ROOT}" --define "_rpmdir ${TARGET_DIR}" --define '_builddir %{_topdir}' --define "_sourcedir ${PWD}" --define "_revision ${SVN_REVISION}" --define "_version ${REL_VER}"
else
    echo ${GPG_PASSPHRASE} | rpmbuild -bb build/api-gateway.spec --sign --buildroot ${BUILD_ROOT} --target ${ARCH}-linux --define "_topdir ${BUILD_ROOT}" --define "_rpmdir ${TARGET_DIR}" --define '_builddir %{_topdir}' --define "_sourcedir ${PWD}" --define "_revision ${SVN_REVISION}" --define "_version ${REL_VER}"
fi

echo

rpm -qpli ${TARGET_DIR}/${ARCH}/*.rpm