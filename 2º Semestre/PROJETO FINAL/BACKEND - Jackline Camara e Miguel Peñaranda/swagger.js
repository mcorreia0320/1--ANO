const swaggerAutogen = require('swagger-autogen')();

const doc = {
    info: {
      title: 'PROJETO BACKEND',
      description: 'PROJETO BACKEND Swagger',
    },
    host: 'backendprojectapimj.azurewebsites.net',
    schemes: ['https'],
};

const outputFile = './swagger-output.json';
const endpointsFiles = ['./app.js'];

/* NOTE: if you use the express Router, you must pass in the 
   'endpointsFiles' only the root file where the route starts,
   such as index.js, app.js, routes.js, ... */

swaggerAutogen(outputFile, endpointsFiles, doc);