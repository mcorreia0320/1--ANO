var express = require('express');
var router = express.Router();
const landingPageController = require('../controllers/landingPageController');


router.get('/counter', landingPageController.totalFootPrint);

router.get('/historial', landingPageController.getAllFootPrints);

router.get('/transports', landingPageController.getAllTransports);

router.get('/diets', landingPageController.getAllDiets);

router.get('/gasValues', landingPageController.getAllGasValues);

router.get('/electricityValues', landingPageController.getAllElectricityValues);





module.exports = router;