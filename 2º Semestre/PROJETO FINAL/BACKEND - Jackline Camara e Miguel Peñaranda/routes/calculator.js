var express = require('express');
var router = express.Router();
const calculatorController = require('../controllers/calculatorController');
const { authenticateTokenFromHeaders } = require('../jwtFunctions');


router.use(authenticateTokenFromHeaders);

// Para preencher o formulario caso seja a primeira vez

router.post('/habits', calculatorController.fillHabits);

router.post('/home', calculatorController.fillInfoHome);

router.post('/transport', calculatorController.fillHabitsTransport);

// Para preencher o formulario caso não seja a primeira vez

router.put('/habits', calculatorController.updateHabits);

router.put('/home', calculatorController.UpdateInfoHome);

router.put('/transport', calculatorController.UpdateHabitsTransport);




module.exports = router;