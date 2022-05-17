# dataplant-errorpages

This Repository generates error pages for the dataplant proxy. Error pages are build into dst folder.


## Getting started

Execute the build script to build error pages. Before that, build a fresh version of nfdi-webcomponents.js to get the latest version of the nfdi-navbar.

## Building the navbar

cd dataplant-keycloak-theme/navbar-building

npm install

rollup --config rollup.config.js
cp dst/nfdi-webcomponents.js ../dataplant-card-theme/login/resources/js/

## Adding HTTP Status Codes

To generate status pages add details for each HTTP status code to codes.json
