[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://img.shields.io/badge/License-GPL%20v2-blue.svg)
# api-gateway-parent
## Description
This repository provides an API gateway to project Symphony. This service is automatically started on the Symphony OVA. 
## Documentation
## API overview
http://[symphony-ova]:10000

## Before you begin
Refer to the symphony-ova repo to install the Symphony OVA.
The system should have Java Runtime Environment installed. The system should have RabbitMQ installed.
## Building
For compilation, Java and Maven should be installed.

Then run the following command:- mvn clean compile
## Packaging
For packaging Java and Maven should be installed.

Then run the following command:- mvn clean install

## Deploying
The output of the build for this repository is a docker container. See /parent-boot-docker-app sub-folder.
## Testing
Unit tests are run as part of the mvn packaging 
## Contributing

The Symphony project is a collection of services and libraries housed at https://github.com/dellemc-symphony.
Contribute code and make submissions at the relevant GitHub repository level. See our documentation for details on how to contribute.

## Community and Support


Reach out to us on Slack #symphony channel. Request an invite at http://community.codedellemc.com.
You can also join [Google Groups] (https://groups.google.com/d/forum/dellemc-symphony) and start a discussion. 

## Licensing
See [LICENSE.md][licence] provided in project root.

[licence]:https://github.com/dellemc-symphony/api-gateway-parent/blob/master/LICENSE.md


